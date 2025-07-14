# Human Detection and Tracking with YOLOv8

This project demonstrates how to detect and track humans in a video using the YOLOv8 object detection model and OpenCV. The script processes an input video, detects people frame-by-frame, draws bounding boxes with tracking IDs, and saves the annotated video.

## Features
- Uses [Ultralytics YOLOv8](https://docs.ultralytics.com/) for human detection and tracking
- Processes video files frame-by-frame
- Draws bounding boxes and tracking IDs for detected people
- Saves the output as a new video file
- Displays the processed video in real-time

## Requirements
- Python 3.7+
- [ultralytics](https://pypi.org/project/ultralytics/)
- [opencv-python](https://pypi.org/project/opencv-python/)

Install dependencies with:
```bash
pip install ultralytics opencv-python
```

## Usage
1. Place your input video (e.g., `DJI_0760.MP4`) in the project directory.
2. Update the `input_path` and `output_path` variables in `Main.py` if needed.
3. Run the script:
   ```bash
   python Main.py
   ```
4. The script will display the video with detected humans in real-time. Press `q` to quit early.
5. The output video with bounding boxes will be saved as `output_detected.mp4`.

## File Structure
- `Main.py` - Main script for detection and tracking
- `DJI_0760.MP4` - Example input video
- `output_detected.mp4` - Output video with detections (generated after running the script)
- `camera.py` - (Not used in main script, for camera input if needed)

## Notes
- The script uses the YOLOv8 nano model (`yolov8n.pt`) by default. You can change the model for better accuracy or speed.
- Only the 'person' class (class 0) is detected and tracked.
- The confidence threshold is set to 0.4 by default.

## Troubleshooting
- If you get an error about `cv2.VideoWriter_fourcc`, ensure you have the correct version of OpenCV installed.
- If no humans are detected, try lowering the confidence threshold or using a higher quality model.

