Autonomous Multi-Drone System for Flood Relief

### NIDAR Challenge GCS Application

This repository contains the source code for a Ground Control Station (GCS) application designed to manage an autonomous, two-drone fleet for search-and-rescue missions. The system architecture is built on a robust, multi-threaded Python application to handle complex, simultaneous tasks with high reliability.

The mission workflow involves a **Scout Drone** for autonomous area surveillance and survivor detection, and a **Delivery Drone** for precise, dynamically-tasked delivery of emergency kits. This GCS acts as the central "brain," coordinating both drones to work in tandem for maximum operational efficiency.

---

## Current Status: Core GCS Framework Complete

This repository contains the complete, foundational software for the GCS. The core logic for autonomous mission planning, drone control, and safety monitoring is implemented and ready for integration.

### What is Done

*   **Multi-threaded Architecture:** The system runs four key processes concurrently using Python's `threading` and `queue` modules, ensuring a non-blocking and responsive application.
*   **Strategic Mission Planner:** A central planner thread manages the overall mission state. It implements logic for area division, greedy assignment of initial targets, and uses K-Means clustering to intelligently group remaining survivors for optimized delivery routes.
*   **Dedicated Drone Controllers:** Each drone is managed by its own controller thread, which translates high-level commands into low-level MAVSDK actions and includes complete logic for the dual-servo payload release mechanism.
*   **High-Priority Battery Failsafe:** An independent `BatteryMonitor` thread constantly checks the fleet's power levels and automatically triggers a Return-to-Launch (RTL) command if any drone's battery drops below a critical threshold.
*   **Modular Codebase:** The project is organized into a clean, modular structure, separating concerns for easy maintenance and future development.

### Next Steps

*   **Integrate Human Detection Module:** Connect the computer vision pipeline (developed by Rohith and Deepak) to feed real-time survivor detections into the `HumanDetectionListener` thread.
*   **SITL and Hardware Integration:**
    *   Test the GCS with the ArduPilot SITL (Software-in-the-Loop) simulator for full-system validation.
    *   Deploy and test the system on the physical drone hardware, including the NVIDIA Jetson and flight controller.
*   **KML Area Division:** Implement the geospatial logic within the `MissionPlanner` to parse the main operational area KML and generate sub-area mission files for the scout drones.


## Technology Stack

*   **Language:** Python
*   **Drone Control & Communication:** MAVSDK-Python
*   **Concurrency:** `threading`, `asyncio`, `queue`
*   **Data Science:** `scikit-learn`, `numpy`
*   **Geospatial Data:** `fastkml`