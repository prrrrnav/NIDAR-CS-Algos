from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolo11x.pt")  

# Open video source (use 0 for webcam)
cap = cv2.VideoCapture("vid_113.MP4")

# Confidence threshold
CONFIDENCE_THRESHOLD = 0.4
human_detected = False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_resized = cv2.resize(frame, (640, 480))

    # Track humans with persistent IDs
    results = model.track(
        source=frame_resized,
        persist=True,
        conf=CONFIDENCE_THRESHOLD,
        classes=[0],  # class 0 = person
        verbose=False
    )

    # Ensure results is iterable
    if not isinstance(results, list):
        results = [results]

    for result in results:
        if result.boxes is not None:
            for box in result.boxes:
                conf = float(box.conf[0])
                cls_id = int(box.cls[0])
                track_id = int(box.id[0]) if box.id is not None else -1

                if cls_id == 0 and conf >= CONFIDENCE_THRESHOLD:
                    human_detected = True
                    x1, y1, x2, y2 = map(int, box.xyxy[0])

                    # Draw bounding box
                    cv2.rectangle(frame_resized, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    label = f"Person ID:{track_id} Conf:{conf:.2f}"
                    cv2.putText(frame_resized, label, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show frame
    cv2.imshow("Human Tracking", frame_resized)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# Final status
if human_detected:
    print("✅ Human(s) detected and tracked with unique IDs.")
else:
    print("❌ No human detected.")
