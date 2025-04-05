import time

# Simulate 10 iterations (for example)
for i in range(10):
    # Capture a new image from the camera or load a new dataset image
    # Here, we're using the same image for simplicity
    image = cv2.imread(image_path)

    # Convert to grayscale and apply edge detection
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 100, 200)

    # Count vehicles based on edges (density)
    vehicle_density = np.count_nonzero(edges)

    # Traffic light control based on density
    if vehicle_density > 5000:
        print(f"Iteration {i + 1}: High traffic density - Green light ON for 10 seconds")
        time.sleep(10)
    elif vehicle_density > 2000:
        print(f"Iteration {i + 1}: Medium traffic density - Green light ON for 5 seconds")
        time.sleep(5)
    else:
        print(f"Iteration {i + 1}: Low traffic density - Red light ON for 3 seconds")
        time.sleep(3)

