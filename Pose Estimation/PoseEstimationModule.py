import cv2
import mediapipe as mp
import time

class PoseEstimationModule:

    def __init__(self,mode=False,model_complexity = 1,smooth_landmarks=True,detection_conf=0.5,track_conf=0.5):
        self.mode = mode
        self.model_complexity = model_complexity
        self.smooth_landmarks = smooth_landmarks
        self.detection_conf = detection_conf
        self.track_conf = track_conf

        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(static_image_mode=self.mode,
                                      model_complexity=self.model_complexity,
                                      smooth_landmarks=self.smooth_landmarks,
                                      min_detection_confidence=self.detection_conf,
                                      min_tracking_confidence=self.track_conf)
        self.mp_drawing = mp.solutions.drawing_utils

    def findPose(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
    
        if self.results.pose_landmarks:
            if draw:
                self.mp_drawing.draw_landmarks(img, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)

        return img
    
    def findPosition(self,img,draw=True):
        lmList = []

        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append((id, cx, cy))
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), -1)

        return lmList

def main():
    cap = cv2.VideoCapture("./Stocks/video-3.mp4")
    pTime=0
    detector = PoseEstimationModule()

    while True:

        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 20, (0, 255, 0), cv2.FILLED)
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

if __name__ == "__main__":
    main()