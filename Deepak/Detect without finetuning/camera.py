from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Input from camera
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening camera")
    exit()

# Set video properties
frame_width = 640
frame_height = 480
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)
fps = 20  # You can manually set an FPS for the webcam

# Output video path
output_path = "G:\\project\\Detection\\output_detected.mp4"

# Define codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Confidence threshold
CONFIDENCE_THRESHOLD = 0.4
human_detected = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for consistency
    frame_resized = cv2.resize(frame, (frame_width, frame_height))

    # Track humans
    results = model.track(source=frame_resized, persist=True, conf=CONFIDENCE_THRESHOLD, classes=[0], verbose=False)

    for result in results:
        for box in result.boxes:
            conf = float(box.conf[0])
            cls_id = int(box.cls[0])
            track_id = int(box.id[0]) if box.id is not None else -1

            if cls_id == 0 and conf >= CONFIDENCE_THRESHOLD:
                human_detected = True
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame_resized, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"Person:{track_id} Conf:{conf:.2f}"
                cv2.putText(frame_resized, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Write the frame to the output file
    out.write(frame_resized)

    # Display the frame
    cv2.imshow("Human Tracking", frame_resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()

# Final print
if human_detected:
    print("✅ Human(s) detected and saved in output_detected.mp4.")
else:
    print("❌ No human detected in the video.")
