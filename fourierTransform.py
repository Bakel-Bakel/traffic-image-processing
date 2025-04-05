import numpy as np
from scipy.fft import fft2, ifft2

# Perform 2D Fourier Transform on the grayscale image
f_transform = fft2(gray_image)

# Shift the zero-frequency component to the center
fshift = np.fft.fftshift(f_transform)

# Get the magnitude spectrum
magnitude_spectrum = np.abs(fshift)

# Display the magnitude spectrum
import matplotlib.pyplot as plt
plt.imshow(np.log(magnitude_spectrum + 1), cmap='gray')
plt.title('Magnitude Spectrum')
plt.show()

