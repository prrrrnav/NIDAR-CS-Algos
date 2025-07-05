import threading
import time
from math import radians, cos, sin, asin, sqrt
from sklearn.cluster import KMeans
import numpy as np

def haversine(lon1, lat1, lon2, lat2):
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 
    return c * r * 1000

class MissionPlanner(threading.Thread):
    def __init__(self, survivor_queue, drone1_commands, drone2_commands, shared_state, state_lock):
        super().__init__()
        self.survivor_queue = survivor_queue
        self.d1_commands = drone1_commands
        self.d2_commands = drone2_commands
        self.state = shared_state
        self.lock = state_lock
        self.all_survivors = []
        self.processed_survivors = set()

    def run(self):
        print("Mission Planner Thread Started.")
        self.initial_scout_setup()

        while True:
            with self.lock:
                current_phase = self.state.get("mission_phase")

            if current_phase == "initial_scout":
                self.handle_initial_scout_phase()
            elif current_phase == "first_delivery":
                self.handle_first_delivery_phase()
            elif current_phase == "main_delivery":
                self.handle_main_delivery_phase()
            
            if current_phase == "complete":
                print("Planner: Mission complete. Exiting.")
                break

            time.sleep(5)

    def initial_scout_setup(self):
        print("Planner: Dividing area and tasking initial scout.")
        area_1_waypoints = [] # Placeholder: Populate with real waypoints
        area_2_waypoints = [] # Placeholder
        
        self.d1_commands.put({"command": "start_scout", "waypoints": area_1_waypoints})
        self.d2_commands.put({"command": "start_scout", "waypoints": area_2_waypoints})
        
        with self.lock:
            self.state["drone1_status"] = "scouting"
            self.state["drone2_status"] = "scouting"

    def handle_initial_scout_phase(self):
        with self.lock:
            d1_done = self.state.get("drone1_status") == "scout_complete"
            d2_done = self.state.get("drone2_status") == "scout_complete"

        if d1_done and d2_done:
            print("Planner: Both drones completed initial scout. Transitioning to first delivery.")
            with self.lock:
                self.state["mission_phase"] = "first_delivery"
    
    def handle_first_delivery_phase(self):
        while not self.survivor_queue.empty():
            survivor = self.survivor_queue.get()
            if survivor not in self.all_survivors:
                self.all_survivors.append(survivor)
        
        if len(self.all_survivors) < 4:
            return

        print("Planner: Assigning 4 initial targets.")
        
        with self.lock:
            pos1 = self.state.get("drone1_pos")
            pos2 = self.state.get("drone2_pos")
        
        if not pos1 or not pos2:
            return

        assignments = {1: [], 2: []}
        available_survivors = list(self.all_survivors)
        
        for _ in range(4):
            best_dist = float('inf')
            best_drone, best_survivor = None, None
            if not available_survivors: break

            if len(assignments[1]) < 2:
                for survivor in available_survivors:
                    dist = haversine(pos1[1], pos1[0], survivor[1], survivor[0])
                    if dist < best_dist:
                        best_dist, best_drone, best_survivor = dist, 1, survivor
            
            if len(assignments[2]) < 2:
                for survivor in available_survivors:
                    dist = haversine(pos2[1], pos2[0], survivor[1], survivor[0])
                    if dist < best_dist:
                        best_dist, best_drone, best_survivor = dist, 2, survivor
            
            if best_drone and best_survivor:
                assignments[best_drone].append(best_survivor)
                available_survivors.remove(best_survivor)
                self.processed_survivors.add(best_survivor)

        if assignments[1]:
            self.d1_commands.put({"command": "deliver_payloads", "targets": assignments[1]})
        if assignments[2]:
            self.d2_commands.put({"command": "deliver_payloads", "targets": assignments[2]})

        with self.lock:
            self.state["mission_phase"] = "main_delivery"
            print("Planner: First delivery tasked. Waiting for drones to return for main phase.")

    def handle_main_delivery_phase(self):
        with self.lock:
            d1_at_gcs = self.state.get("drone1_status") == "at_gcs"
            d2_at_gcs = self.state.get("drone2_status") == "at_gcs"

        if not (d1_at_gcs and d2_at_gcs):
            return

        print("Planner: Both drones at GCS. Planning main delivery phase.")
        remaining_survivors = [s for s in self.all_survivors if s not in self.processed_survivors]
        
        if not remaining_survivors:
            print("Planner: All known survivors have been tasked. Mission complete.")
            with self.lock: self.state["mission_phase"] = "complete"
            return
            
        X = np.array(remaining_survivors)
        
        n_clusters = min(2, len(remaining_survivors))
        kmeans = KMeans(n_clusters=n_clusters, random_state=0, n_init='auto').fit(X)
        
        cluster_1_targets = [tuple(coord) for coord in X[kmeans.labels_ == 0]]
        cluster_2_targets = [tuple(coord) for coord in X[kmeans.labels_ == 1]] if n_clusters > 1 else []

        if cluster_1_targets:
            self.d1_commands.put({"command": "deliver_payloads_optimized", "targets": cluster_1_targets})
        if cluster_2_targets:
            self.d2_commands.put({"command": "deliver_payloads_optimized", "targets": cluster_2_targets})

        for s in remaining_survivors: self.processed_survivors.add(s)
        with self.lock: self.state["mission_phase"] = "complete"