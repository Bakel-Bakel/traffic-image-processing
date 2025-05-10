from flask import Flask, render_template, Response
from ultralytics import YOLO
import cv2
import time
import threading
from gpiozero import LED

# === GPIOZero LED Setup ===
RED = LED(17)
YELLOW = LED(27)
GREEN = LED(22)

def set_light(color):
    RED.off()
    YELLOW.off()
    GREEN.off()

    if color == 'red':
        RED.on()
    elif color == 'yellow':
        YELLOW.on()
    elif color == 'green':
        GREEN.on()

# === Flask App ===
app = Flask(__name__)
model = YOLO('yolov8s.pt')  # You can replace with your custom model
camera = cv2.VideoCapture(0)

# Shared state for traffic light
light_state = {
    'color': 'red',
    'countdown': 0,
    'vehicle_count': 0
}

# === Traffic Light Control Logic ===
def light_cycle():
    while True:
        count = light_state['vehicle_count']
        density = min(count / 4, 1.0)
        green_time = max(3, int(density * 10))  # 3 to 10 seconds

        # GREEN
        set_light('green')
        light_state['color'] = 'green'
        for i in range(green_time, 0, -1):
            light_state['countdown'] = i
            time.sleep(1)

        # YELLOW
        set_light('yellow')
        light_state['color'] = 'yellow'
        for i in range(1, 0, -1):
            light_state['countdown'] = i
            time.sleep(1)

        # RED
        set_light('red')
        light_state['color'] = 'red'
        for i in range(3, 0, -1):
            light_state['countdown'] = i
            time.sleep(1)

# Start light logic in background
threading.Thread(target=light_cycle, daemon=True).start()

# === YOLO Frame Stream ===
def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        results = model.predict(source=frame, imgsz=640, conf=0.3, verbose=False)
        boxes = results[0].boxes
        car_count = 0

        if boxes is not None:
            cls_ids = boxes.cls.cpu().numpy()
            car_ids = [2, 3, 5, 7]  # car, motorcycle, bus, truck
            car_count = sum(1 for cid in cls_ids if int(cid) in car_ids)

        light_state['vehicle_count'] = car_count
        annotated = results[0].plot()

        ret, buffer = cv2.imencode('.jpg', annotated)
        frame = buffer.tobytes()

        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# === Flask Routes ===
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/status')
def status():
    return {
        'color': light_state['color'],
        'countdown': light_state['countdown'],
        'vehicle_count': light_state['vehicle_count']
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
