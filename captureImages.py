import time
import picamera

# Initialize the camera
camera = picamera.PICamera()

# Set image resolution
camera.resolution = (640, 480)

# Wait for the camera to initialize
time.sleep(2)

# Capture image and save to file
camera.capture('traffic_image.jpg')

print("Image Captured!")
camera.close()

