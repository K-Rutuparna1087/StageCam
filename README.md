# 🎥 **StageCam**

**AI-powered face-tracking camera framing for Python projects**

---

## 🚀 Use Cases

StageCam is built for:

* 💻 **Virtual meetings** – Auto-center your face even if you move
* 🤖 **Robotics/Embedded Vision** – Add camera intelligence to your bots
* 🎬 **Livestreams & Screen Recording** – Look pro with automatic framing
* 🧠 **Python Apps** – Integrate real-time face tracking with ease

---

## ✨ Features

* 🧠 **MediaPipe-based Face Detection** (lightweight & accurate)
* 🎯 **Smooth Pan & Zoom** – No jerky motion
* 👥 **Multi-face Adaptive Framing**
* 🪞 **Lateral Inversion** – Just like standard webcams
* 🧩 **Modular API** – Import and customize as needed

---

## 📦 Installation

```bash
pip install git+https://github.com/K-Rutuparna1087/StageCam.git
```

**Dependencies** (auto-installed):

* `opencv-python`
* `mediapipe`
* `numpy`

---

## ⚡ Quick Usage

```python
import stagecam

stagecam.show()
```

**Optional Parameters:**

```python
stagecam.show(
    camera_index=0,
    detection_confidence=0.6,
    zoom_factor=2.5
)
```

---

## 🖼️ Compare: Original vs StageCam Feed

```python
import cv2
import stagecam

cap = cv2.VideoCapture(0)
stagecam_feed = stagecam.get_stagecam_feed(camera_index=0)

while True:
    ret, original = cap.read()
    staged = stagecam_feed(original.copy())
    combined = cv2.hconcat([original, staged])
    cv2.imshow("Original (left) | StageCam (right)", combined)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

---

## 🔧 Build Your Own System

Import core components and customize:

```python
from stagecam import FaceTracker, FrameTransformer
```

---

## 🛣️ Roadmap

* 📷 Virtual Webcam Output (via `v4l2loopback` / OBS)
* 🖱️ GUI toggle controls
* 📦 PyPI publishing (`pip install stagecam`)
* 📱 Mobile-friendly version (future goal)

---

## 👤 Author

Made with ❤️ by **K Rutuparna**
🔧 Mechatronics Engineer | 🤖 Robotics + AI Vision Enthusiast
🌐 GitHub: [K-Rutuparna1087](https://github.com/K-Rutuparna1087)

---

## ⚖️ License

**MIT License** – Free to use, modify, and distribute.

---
