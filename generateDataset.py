import time
import picamera
import os

# Create a directory to store the images
image_folder = 'dataset/generated_traffic_images/'
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# Initialize the camera
camera = picamera.PICamera()

# Set image resolution
camera.resolution = (640, 480)

# Wait for the camera to initialize
time.sleep(2)

# Loop to capture 1000 images
for i in range(1, 1001):
    # Capture image and save to file with a unique name
    image_filename = f'{image_folder}traffic_image_{i}.jpg'
    camera.capture(image_filename)
    
    # Print status
    print(f"Image {i} captured and saved as {image_filename}")
    
    # Optional: Wait for 1 second before capturing the next image (adjust as needed)
    time.sleep(1)

# Close the camera
camera.close()
print("Finished capturing 1000 images!")

