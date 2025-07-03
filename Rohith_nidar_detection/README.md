# 👣 Human Detection and Tracking with YOLOv11

This project demonstrates real-time **human detection and tracking** from a video using [Ultralytics YOLOv11](https://github.com/ultralytics/ultralytics) and **OpenCV**. The script processes each frame of an input video, detects humans, assigns persistent tracking IDs, and displays + saves the annotated video output.

---

## ✨ Features

- ✅ **YOLOv8** for high-accuracy object detection  
- 🧠 **Tracking with persistent IDs** for each detected human  
- 🎥 **Real-time processing** of video streams  
- 🧾 **Annotated output** saved to a new video file  
- 🖼️ **Display with bounding boxes & confidence scores**

---

## 📁 File Structure


.
├── Main.py                # Main script (human detection & tracking)
├── vid_113.MP4            # Example input video (user provided)
└── README.md              # Project documentation (this file)

📦 Requirements
Python 3.7+
Ultralytics YOLOv8
OpenCV
Install dependencies using pip:
pip install ultralytics opencv-python

## 🚀Usage
1.Place your video file (e.g., vid_113.MP4) in the project directory.

2.Run the main script:
Main.py

3.The video window will show real-time human detection with tracking IDs.
Press q to exit early.


## How it works

from ultralytics import YOLO
import cv2

# Load model
model = YOLO("yolo11x.pt")  # Replace with your preferred YOLOv8 variant

# Open video source
cap = cv2.VideoCapture("vid_113.MP4")


## Configuration

| Parameter              | Default Value  | Description                             |
| ---------------------- | -------------- | --------------------------------------- |
| `model`                | `"yolo11x.pt"` | YOLOv8 model to use                     |
| `CONFIDENCE_THRESHOLD` | `0.4`          | Minimum confidence to count a detection |
| `classes`              | `[0]`          | Only detect 'person' class              |
| `frame size`           | `(640, 480)`   | Resize resolution for processing        |



## 🛠️ Troubleshooting
Issue: cv2.VideoWriter_fourcc errors
Solution: Ensure correct OpenCV version (opencv-python)

No detections?
Try lowering confidence threshold (e.g., 0.3) or switch to a more accurate model like yolov8m.pt or yolov8x.pt.


## Tech Stack

| Tool        | Purpose                     |
| ----------- | --------------------------- |
| YOLOv8      | Object detection + tracking |
| OpenCV      | Video I/O, image processing |
| Python 3.7+ | Scripting language          |

<p align="left"> <img src="https://img.shields.io/badge/Python-3.7+-blue?logo=python" /> <img src="https://img.shields.io/badge/OpenCV-4.x-green?logo=opencv" /> <img src="https://img.shields.io/badge/YOLOv8-ultralytics-orange?logo=yolov5" /> </p>



✅ Sample Output Message
At the end of execution:

✅ Human(s) detected and tracked with unique IDs.

or

❌ No human detected.


## 📬 Contact / Contributions
Feel free to raise an issue or contribute by forking this repo.
For queries, open a GitHub issue or message the maintainer.



## 🧾 Conclusion

This project showcases a practical implementation of real-time **human detection and tracking** using the powerful **YOLOv8 model** combined with **OpenCV**. It’s a great starting point for applications in:

- Surveillance systems 🛡️  
- Crowd analytics 📊  
- Smart cities 🏙️  
- Sports analysis 🏃  
- Human-robot interaction 🤖

With minimal setup and clear modularity, this code can be easily extended to:

- Use live webcam feeds or IP cameras
- Track additional object classes
- Integrate with real-time alert systems
- Improve accuracy by switching to more robust YOLO models

Whether you're a beginner learning about computer vision or an experienced developer prototyping a tracking pipeline, this project is designed to be clear, efficient, and adaptable.

> 🚀 *Explore. Build. Detect. Track.*
