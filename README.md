# Smart Traffic Light System Using Image and Signal Processing

This project simulates a **Smart Traffic Light System** using real-time traffic density analysis based on image and signal processing techniques. The primary objective of this system is to optimize traffic flow in urban settings by adjusting traffic light timings based on current traffic conditions.

## Overview

The system uses the following steps:
1. **Capture Traffic Images** – Using a camera or an existing dataset of traffic images.
2. **Grayscale Conversion and Edge Detection** – Preprocessing the images to highlight vehicle edges and analyze traffic density.
3. **Fourier Transform** – Analyzing traffic patterns in the frequency domain to identify congestion.
4. **Traffic Light Control Algorithm** – Adjusting the light timings based on vehicle density.
5. **System Simulation** – The entire system is simulated using Python.

## Getting Started

### Prerequisites

To run this project, you need to have Python installed along with some libraries for image and signal processing. You can install the required libraries using pip:

```bash
pip install opencv-python numpy scipy matplotlib picamera

