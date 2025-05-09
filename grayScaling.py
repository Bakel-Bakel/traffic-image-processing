import cv2
import os

# Folder containing your images
image_folder = 'dataset_test/'

# List all images in the folder
image_files = os.listdir(image_folder)

# Loop through all images in the folder
for image_file in image_files:
    # Check if the file is an image
    if image_file.endswith('.jpg') or image_file.endswith('.png'):
        # Load the image
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)

        # Convert to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply Canny edge detection
        edges = cv2.Canny(gray_image, 100, 200)  # You can adjust thresholds

        # Display the edge-detected image
        cv2.imshow(f"Edges: {image_file}", edges)
        cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

