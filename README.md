# 🎥 **StageCam**

**AI-powered face-tracking camera framing for Python projects**

---

## 🚀 Use Cases

StageCam is built for:

* 💻 **Virtual Meetings** – Auto-center your face, even when you move
* 🤖 **Robotics / Embedded Vision** – Add smart framing to robots or IoT cameras
* 🎬 **Livestreams & Screen Recording** – Look polished without manual setup
* 🧠 **Any Python App** – Easily integrate real-time face framing

---

## ✨ Features

* 🧠 **MediaPipe-based Face Detection** – Lightweight yet accurate
* 🎯 **Smooth Pan & Zoom** – Fluid, jitter-free movement
* 👥 **Multi-face Framing** – Dynamically adapts to multiple faces
* 🪞 **Lateral Inversion** – Natural webcam-like mirroring
* 🧩 **Modular API** – Use as a script or drop into your own project

---

## 📦 Installation

🔗 [PyPI: stagecam](https://pypi.org/project/stagecam)

```bash
pip install stagecam
```

Or install directly from GitHub:

```bash
pip install git+https://github.com/K-Rutuparna1087/StageCam.git
```

**Dependencies (auto-installed):**
`opencv-python`, `mediapipe`, `numpy`

---

## ⚡ Quick Usage

```python
import stagecam

stagecam.show()
```

With optional arguments:

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
from stagecam import FaceTracker, FrameTransformer

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

frame_height, frame_width = frame.shape[:2]
tracker = FaceTracker()
transformer = FrameTransformer(frame_width, frame_height)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    flipped = cv2.flip(frame, 1)
    bboxes = tracker.detect(flipped)
    staged = transformer.transform(flipped.copy(), bboxes)

    combined = cv2.hconcat([flipped, staged])
    cv2.imshow("Original (left) | StageCam (right)", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

---

## 🔧 Build Your Own System

Use the core modules independently:

```python
from stagecam import FaceTracker, FrameTransformer
```

---

## 🛣️ Roadmap

* 📷 Virtual webcam output (v4l2loopback / OBS)
* 🖱️ GUI controls for zoom/pan toggle
* 📦 Stable PyPI support and versioning
* 📱 Mobile device support

---

## 👤 Author

**K Rutuparna**
Mechatronics Engineer | Robotics + AI Vision Enthusiast
🌐 [GitHub – K-Rutuparna1087](https://github.com/K-Rutuparna1087)

---

## ⚖️ License

Licensed under the **MIT License** – Free to use, modify, and distribute.

---
