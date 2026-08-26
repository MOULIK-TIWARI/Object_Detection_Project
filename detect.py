import cv2
from ultralytics import YOLO
import os

# Load YOLOv8 model
model = YOLO("yolov8n.pt")   # you can use yolov8s.pt for better accuracy

# Open webcam
cap = cv2.VideoCapture(0)

# Create folder to save frames
os.makedirs("saved_frames", exist_ok=True)

count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO detection
    results = model(frame)

    # Draw bounding boxes on frame
    annotated_frame = results[0].plot()

    # Show output
    cv2.imshow("Real-Time Object Detection", annotated_frame)

    # ✅ Save ONLY when objects are detected
    if len(results[0].boxes) > 0:
        cv2.imwrite(f"saved_frames/frame_{count}.jpg", annotated_frame)
        print(f"Saved frame {count}")

    count += 1

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()