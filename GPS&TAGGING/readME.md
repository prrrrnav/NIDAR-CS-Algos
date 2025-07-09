📍 GPS & Tagging – NIDAR-CS-Algos
This module is part of the NIDAR Drone Intelligence System, specifically responsible for GPS coordination handling and human detection tagging logic. It plays a crucial role in locating detected humans using GPS data and preparing their coordinates for further processing—such as KML export, drone routing, or payload drop.

🚀 Objective
To track and tag the last two human detections made by the drone using GPS coordinates. This is important in the context of search-and-rescue missions, where only the two latest human locations are required for action (e.g., supply drops via drones).

🧠 What's Happening?
✅ main.py
This script:

Continuously receives GPS data (latitude, longitude, altitude) and human detection events.

Stores only the latest two detections (FIFO approach).

Writes them to a file or logs for tracking, display, or export to KML for visual mapping.

✅ getCurrentLocation.py
This file:

Simulates or retrieves live GPS coordinates from a device.

Provides the location data that will be attached to each human detection event.

📦 Folder Structure
graphql
Copy
Edit
GPS&TAGGING/
│
├── getCurrentLocation.py  # GPS coordinate retrieval module
├── main.py                # Main tagging logic (tracks 2 latest detections)
├── location.txt           # Output file with last 2 detection coordinates
🛰️ How It Works (Flow)
Human Detected ➤ getCurrentLocation() is called.

GPS Tagged ➤ Location (lat, long, alt) is stored with timestamp.

Queue Maintained ➤ Only last 2 detections are kept.

Export/Use ➤ The coordinates are saved to a text file or fed into the drone's KML/map planner.

🔧 Future Plans (Optional Section)
Integrate with KML file generator for Google Earth visualization.

Connect to payload dropping logic using these last two tags.

Sync with live drone telemetry using LRF and object detection modules.

🧑‍💻 Author
Made with 🔧 by @prrrrnav for the NIDAR drone project.