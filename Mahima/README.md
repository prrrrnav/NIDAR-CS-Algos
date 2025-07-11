✅ 2. GCS (Ground Control Station) Software by Mahima
📂 Path: Mahima/

Goal:
Central control architecture that orchestrates drone coordination, clustering, planning, and battery safety.

Main Files:

main_gcs.py: Initializes and starts planner/controller/monitor threads.

planner_thread.py: Mission logic (area division, clustering, decision making).

drone_controller.py: Executes commands via MAVSDK (waypoints, payload).

battery_monitor.py: Monitors battery and triggers Return-to-Launch if needed.

detection_listener.py: Monitors .kml inputs and shares coordinates for planning.

Design:
Threaded architecture with centralized state and individual mission pipelines for each drone.