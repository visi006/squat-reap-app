from fastapi import FastAPI
import cv2

from pose_detect import PoseDetector
from sessions import WorkoutSession

app = FastAPI()

cap = cv2.VideoCapture(0)
detector = PoseDetector()
session = WorkoutSession()

@app.get("/workout")
def workout():
    success, frame = cap.read()
    if not success:
        return {"error": "Camera not accessible"}

    frame = cv2.flip(frame, 1)
    results = detector.process(frame)

    feedback = "Stand straight"

    if results.pose_landmarks:
        lm = results.pose_landmarks.landmark
        h, w, _ = frame.shape

        hip = (int(lm[24].x * w), int(lm[24].y * h))
        knee = (int(lm[26].x * w), int(lm[26].y * h))
        ankle = (int(lm[28].x * w), int(lm[28].y * h))

        angle = detector.calculate_angle(hip, knee, ankle)

        if angle < 90:
            session.state = "SQUATTING"
            session.direction = 1
            feedback = "Good depth"

        elif angle > 160:
            session.state = "STANDING"
            if session.direction == 1:
                session.total_reps += 1
                session.correct_reps += 1
                session.direction = 0
            feedback = "Stand straight"

        else:
            session.state = "IMPROPER"
            feedback = "Go lower"

    return {
        "state": session.state,
        "reps": session.total_reps,
        "accuracy": session.accuracy(),
        "duration": session.duration(),
        "feedback": feedback
    }