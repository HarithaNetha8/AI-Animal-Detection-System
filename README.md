
# 📘 AI-Based Detection and Alert Mechanism for Fixed Environments

## 📝 Project Description

This project is an **AI-powered safety system** designed to prevent accidents caused by animals hiding under parked vehicles. The system uses a **pre-trained YOLOv5 model** to detect animals such as cats and dogs from uploaded images. Upon detection, it triggers **visual and audio alerts** and simulates **engine start blocking** to ensure safety.

The project demonstrates practical applications of **Computer Vision, Deep Learning, and Web Technologies** for real-world safety solutions. It also lays the foundation for future integration with **IoT devices, vehicle sensors, and embedded systems**.

---

## 🎯 Key Features

* Real-time animal detection using YOLOv5
* Confidence-based alert system
* Audio alerts (beep/alarm)
* Engine start blocking simulation
* User-friendly Flask web interface
* Night vision simulation (optional)

---

## 💻 Technology Stack

* **Programming Language:** Python
* **AI Model:** YOLOv5 (PyTorch)
* **Backend:** Flask
* **Frontend:** HTML, CSS
* **Computer Vision:** OpenCV
* **Audio Alerts:** HTML5 `<audio>`

---

## 📂 Project Structure

```
AI_Animal_Detection_Project/
│
├── app.py                 # Flask application
├── detect.py              # YOLOv5 detection logic
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # HTML interface
├── static/
│   ├── style.css          # CSS styling
│   ├── alert.mp3          # Audio alert
│   └── uploads/           # Uploaded images folder
├── yolov5/                # YOLOv5 model files
└── README.md              # Project documentation
```

---

## ⚡ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone <https://github.com/HarithaNetha8/AI-Animal-Detection-System>
cd AI_Animal_Detection_Project
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

### 3️⃣ Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Flask app

```bash
python app.py
```

### 6️⃣ Open in browser

```
http://127.0.0.1:5000/
```
### OUTPUT 
<img width="1365" height="724" alt="Screenshot 2026-01-13 194655" src="https://github.com/user-attachments/assets/f7bf6841-5dfc-4b28-a0b6-9be540e0a7a9" />
<img width="1365" height="720" alt="Screenshot 2026-01-13 194619" src="https://github.com/user-attachments/assets/7a5e0d85-8e70-47ba-9ef4-3ae69915e5bf" />
<img width="1338" height="655" alt="Screenshot 2026-01-13 194538" src="https://github.com/user-attachments/assets/6c46a9c0-7a99-4541-9e47-1448a1ee77e3" />


---

## 🖼 Usage

1. Upload an image of the area under the vehicle.
2. If an animal is detected, a **visual warning** and **audio alert** will trigger, and the system will simulate **engine start blocking**.
3. If no animal is detected, a **green safe message** will appear.

---

## 🔧 Future Enhancements

* Live camera detection for real-time alerts
* Integration with **IoT devices** and vehicle sensors
* Mobile app notifications
* Infrared camera for **night vision detection**
* Direct **engine control** in vehicles

---

## 📝 Author

**Haritha, CSE 4th Year**

* Email: harithamacharla26@gmail.com
* GitHub: https://github.com/HarithaNetha8

---

## 📌 License

This project is for **educational purposes**.

---
