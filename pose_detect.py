import cv2
import mediapipe as mp
import math

mp_pose = mp.solutions.pose

class PoseDetector:
    def __init__(self):
        self.pose = mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def process(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return self.pose.process(rgb)

    def calculate_angle(self, a, b, c):
        angle = math.degrees(
            math.atan2(c[1] - b[1], c[0] - b[0]) -
            math.atan2(a[1] - b[1], a[0] - b[0])
        )
        angle = abs(angle)
        if angle > 180:
            angle = 360 - angle
        return angle