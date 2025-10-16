# Real-Time Hand Tracking Module 🖐️

This project provides a simple, reusable Python module for real-time hand detection and landmark tracking using OpenCV and Google's MediaPipe library. The core logic is encapsulated in a `handDetector` class, making it easy to integrate into your own computer vision applications. A `main.py` file is included to demonstrate its usage.

-----

## Features

  * **Real-Time Performance**: Smoothly tracks hands from a live webcam feed.
  * **Multi-Hand Detection**: Capable of detecting and tracking multiple hands simultaneously.
  * **Landmark Identification**: Identifies and provides pixel coordinates for all 21 key points on the hand.
  * **Reusable Module**: Packaged into a simple `handDetector` class for easy integration.
  * **Visual Feedback**: Draws the hand skeleton and displays the Frames Per Second (FPS) for performance monitoring.

-----

## Project Structure

```
.
├── HandTrackingModule.py   # The core module containing the handDetector class
└── main.py                 # An example script demonstrating how to use the module
```

-----

## Requirements

To run this project, you'll need Python 3 and the following libraries:

  * `opencv-python`
  * `mediapipe`

-----

## Installation

1.  Clone or download this repository.
2.  Make sure you have Python 3 installed on your system.
3.  Install the required packages using pip:
    ```bash
    pip install opencv-python mediapipe
    ```

-----

## How to Use

### 1\. Running the Demo

To see the module in action, simply run the `main.py` script from your terminal:

```bash
python main.py
```

A window will open showing your webcam feed. When you show your hand to the camera, the script will draw the landmarks on it and print the thumb tip's coordinates to the console.

### 2\. Integrating into Your Own Project

To use the `handDetector` in your own Python script, follow these steps:

1.  Make sure the `HandTrackingModule.py` file is in the same directory as your project file.
2.  Import the class from the module.
3.  Create an instance of the class and use its methods on your OpenCV images.

Here is a basic example:

```python
import cv2
import HandTrackingModule as htm # Import the module

# Initialize webcam
cap = cv2.VideoCapture(0)

# Create a detector object
detector = htm.handDetector()

while True:
    success, img = cap.read()
    
    # 1. Find hands and draw them
    img = detector.findHands(img)
    
    # 2. Find the position of landmarks
    lmList = detector.findPosition(img)
    
    # You can now use the landmark list (lmList) for your application
    if len(lmList) != 0:
        print(lmList[4]) # Print coordinates of the thumb tip

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

-----

## Module Breakdown (`HandTrackingModule.py`)

The `handDetector` class is the core of this module.

#### `__init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5)`

The constructor initializes the MediaPipe Hands model.

  * **`mode`**: Set to `True` for static images.
  * **`maxHands`**: Maximum number of hands to detect.
  * **`detectionCon`**: Minimum detection confidence threshold (0.0 to 1.0).
  * **`trackCon`**: Minimum tracking confidence threshold.

#### `findHands(self, img, draw=True)`

Processes an OpenCV image (`img`) to find hand landmarks.

  * If `draw=True`, it draws the landmarks and connections onto the image.
  * Returns the image with the drawings.

#### `findPosition(self, img, handNo=0, draw=True)`

Finds all landmarks on a specific hand (`handNo`).

  * Returns a list of landmarks, where each element is `[id, x_coordinate, y_coordinate]`. For example, `[4, 250, 400]` represents the thumb tip at coordinates (250, 400).