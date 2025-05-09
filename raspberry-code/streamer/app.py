from flask import Flask, Response, render_template
from ultralytics import YOLO
import cv2
import numpy as np

app = Flask(__name__)
model = YOLO('yolov8s.pt')  #

# Initialize webcam
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Run inference
        results = model.predict(source=frame, imgsz=640, conf=0.3, verbose=False)

        # Get bounding boxes
        boxes = results[0].boxes
        if boxes is not None:
            # Filter out class ID 7 = 'train'
            exclude_ids = [7]  # Add more like [6, 7, 8] to exclude bus, train, truck
            filtered_boxes = boxes[~np.isin(boxes.cls.cpu().numpy(), exclude_ids)]
            results[0].boxes = filtered_boxes  # Replace with filtered boxes

        # Annotate the frame
        annotated_frame = results[0].plot()

        # Encode the frame to JPEG
        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame = buffer.tobytes()

        # Yield frame for streaming
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
