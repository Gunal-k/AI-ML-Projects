# Real-Time Pose Estimation Module

This project provides a robust, reusable Python module for real-time human pose estimation using **OpenCV** and Google's **MediaPipe** library. It's designed to be easily integrated into larger computer vision applications, such as fitness trackers, augmented reality experiences, or gesture recognition systems.



---

## 🚀 Features

-   **Real-Time Performance**: Efficiently processes video streams to detect and track human poses.
-   **High-Fidelity Tracking**: Utilizes MediaPipe to identify 33 distinct 3D landmarks on the body.
-   **Modular Class Structure**: The `PoseEstimationModule` class is self-contained and easy to import into other projects.
-   **Customizable**: Easily adjust parameters like model complexity, detection confidence, and tracking confidence to balance performance and accuracy.
-   **Performance Monitoring**: Includes a built-in FPS (Frames Per Second) counter to monitor real-time performance.

---

## 🛠️ Technologies Used

-   **Python**: The core programming language.
-   **OpenCV**: Used for video capture, processing, and rendering.
-   **MediaPipe**: Powers the underlying machine learning model for pose landmark detection.

---

## ⚙️ Setup and Installation

Follow these steps to get the project running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/Your-Repo-Name.git](https://github.com/YourUsername/Your-Repo-Name.git)
    cd Your-Repo-Name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install opencv-python mediapipe
    ```

---

## ▶️ How to Run

1.  Place a video file you want to process inside the project directory (e.g., in a `Stocks` folder).
2.  Update the video path inside the `main()` function in `PoseEstimationModule.py`:
    ```python
    # In the main() function
    cap = cv2.VideoCapture("./Path/To/Your/Video.mp4")
    ```
3.  Run the script from your terminal:
    ```bash
    python PoseEstimationModule.py
    ```

---

## 💡 How to Use the Module in Your Own Project

The `PoseEstimationModule` class is designed for easy integration.

```python
import cv2
from PoseEstimationModule import PoseEstimationModule

# Initialize video capture and the detector
cap = cv2.VideoCapture(0) # Use 0 for webcam
detector = PoseEstimationModule(detection_conf=0.7)

while True:
    success, img = cap.read()
    if not success:
        break

    # Find the pose and draw landmarks
    img = detector.findPose(img)

    # (Optional) Get the list of landmark positions
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        # Example: Print the coordinates of the right elbow (landmark 14)
        print(lmList[14])
        # Draw a circle on the right elbow
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

    cv2.imshow("My Pose Detector", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

This module serves as the foundational computer vision engine for my upcoming **AI Gym Trainer** application!