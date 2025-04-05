import cv2
import os

# Folder containing your images
image_folder = 'dataset/'

# List all images in the folder
image_files = os.listdir(image_folder)

# Loop through all images in the folder
for image_file in image_files:
    # Check if the file is an image (optional, based on your dataset)
    if image_file.endswith('.jpg') or image_file.endswith('.png'):
        # Load the image
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)

        # Process the image (you can add any processing you want here)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Display the processed image (optional)
        cv2.imshow(f"Processed Image: {image_file}", gray_image)
        cv2.waitKey(0)

# Close all OpenCV windows after processing all images
cv2.destroyAllWindows()

