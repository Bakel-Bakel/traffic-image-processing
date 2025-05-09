import cv2
from ultralytics import YOLO
import time

# Load the YOLOv8n model (lightweight for Raspberry Pi)
model = YOLO('yolov8n.pt')

# Open the USB webcam (usually /dev/video0)
cap = cv2.VideoCapture(0)  # Use 0 or 1 depending on your USB camera index

# Optional: Set frame resolution for performance (640x480 is good for Raspberry Pi)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Real-time loop
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Run YOLO inference on the frame
        results = model.predict(source=frame, imgsz=640, conf=0.5, verbose=False)

        # Draw detections
        annotated_frame = results[0].plot()

        # Show the frame with detections
        cv2.imshow("YOLOv8 Real-Time Detection", annotated_frame)

        # Break loop with 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrupted by user.")

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
