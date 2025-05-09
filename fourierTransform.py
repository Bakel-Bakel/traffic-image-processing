import numpy as np
import cv2
from scipy.fft import fft2
import matplotlib.pyplot as plt

# Load the image in grayscale mode
gray_image = cv2.imread('grayimage.png', cv2.IMREAD_GRAYSCALE)

# Check if image is loaded properly
if gray_image is None:
    raise FileNotFoundError("Image 'grayimage.png' not found or could not be loaded.")

# Perform 2D Fourier Transform
f_transform = np.fft.fft2(gray_image)

    # Shift the zero-frequency component to the center of the spectrum
fshift = np.fft.fftshift(f_transform)

# Calculate the magnitude spectrum
magnitude_spectrum = np.abs(fshift)

# Use logarithmic scaling to enhance visualization
log_magnitude_spectrum = np.log(magnitude_spectrum + 1)

# Plot the results
plt.figure(figsize=(12, 6))

# Original Image
plt.subplot(1, 2, 1)
plt.imshow(gray_image, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis('off')

# Fourier Transform Magnitude Spectrum
plt.subplot(1, 2, 2)
plt.imshow(log_magnitude_spectrum, cmap='gray')
plt.title("Magnitude Spectrum (Log Scale)")
plt.axis('off')

plt.tight_layout()
plt.show()

