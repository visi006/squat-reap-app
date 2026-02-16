# 🏋️ AI Squat Rep Tracker – Full Stack Web Application

A **real-time AI-powered full-stack web application** that tracks **squat repetitions**, analyzes **exercise posture**, and provides **live feedback** using a webcam.  
The system is built with a **FastAPI backend** and a **browser-based frontend**, demonstrating real-world **full-stack + computer vision integration**.

---

## 🚀 Features

- 📷 Live webcam capture using browser APIs
- 🧠 AI-based human pose estimation using MediaPipe
- 📐 Joint angle calculation (Hip–Knee–Ankle)
- 🔢 Automatic squat repetition counting
- 🧍 Exercise state detection (Standing / Squatting / Improper)
- 💬 Real-time posture feedback
- 📊 Accuracy percentage calculation
- ⏱ Session duration tracking
- 🌐 Full-stack architecture (Frontend + Backend)

---

## 🛠 Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Browser Webcam API (`getUserMedia`)

### Backend
- Python
- FastAPI
- OpenCV
- MediaPipe
- NumPy

---

## 🏗 System Architecture

Browser (Frontend)
│
├── Webcam Capture
│
├── UI Dashboard (HTML/CSS/JS)
│
└── REST API Calls
↓
FastAPI Backend
│
├── Pose Detection (MediaPipe)
├── Business Logic (Reps, Accuracy, State)
└── Session Management


## 📂 Project Structure

SQUAT REP APP/
│
├── Backend/
│ ├── main.py # FastAPI backend
│ ├── pose_detector.py
│ ├── session.py
│ └── requirements.txt
│
├── Frontend/
│ ├── index.html
│ ├── style.css
│ └── script.js
│
└── README.md



## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/visi006/ai-squat-rep-tracker.git
cd ai-squat-rep-tracker/Backend
2️⃣ Create virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
▶️ Run the Backend
uvicorn main:app --reload
Backend runs at:

http://127.0.0.1:8000
🌐 Run the Frontend
Open Frontend/index.html in Google Chrome

Allow camera access

Start performing squats in front of the camera

🧠 How It Works
Frontend captures live video using the webcam

Backend processes frames using MediaPipe Pose

Joint angles are calculated using landmark coordinates

Squat logic:

Angle < 90° → SquATTING

Angle > 160° → STANDING

Full down → up = 1 repetition

Backend sends live analytics to frontend

UI updates in real time

🎯 Use Cases
Home workout posture correction

Beginner fitness monitoring

Injury prevention

AI-based virtual gym trainer

🚧 Limitations
Optimized for single-person detection

Requires proper lighting for best accuracy

Currently supports squat exercise only

🔮 Future Enhancements
WebSocket-based real-time streaming

Support for push-ups and lunges

Audio feedback for posture correction

User authentication & workout history

Deployment on cloud (AWS / Render)

👨‍💻 Author
Vismay Pradeep
B.Tech  Student
GitHub: https://github.com/visi006
