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
from stagecam import FaceTracker, FrameTransformer

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("❌ Error: Cannot access camera.")
        return

    ret, frame = cap.read()
    if not ret:
        print("❌ Error: Cannot read from camera.")
        return

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

if __name__ == "__main__":
    main()

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
