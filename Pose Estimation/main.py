import cv2
import mediapipe as mp
import time
import PoseEstimationModule as pem

pTime = 0
cTime = 0
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("./Stocks/video-4.mp4")

detector = pem.PoseEstimationModule()

while True:

    success, img = cap.read()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=True)
    if len(lmList) != 0:
        print(lmList[14])  # Example: print the coordinates of landmark with id 14 total 33 points

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    # Resize the output window to be smaller
    # We are scaling it to 50% of its original size here. You can adjust the fx and fy values.
    resized_img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
    cv2.imshow("Image", resized_img)
    cv2.waitKey(1)
