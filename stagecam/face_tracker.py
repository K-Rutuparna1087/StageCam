import cv2 as cv
import mediapipe as mp

class FaceTracker:
    def __init__(self, min_detection_confidence=0.6):
        self.mp_face_detection = mp.solutions.face_detection
        self.face_detection = self.mp_face_detection.FaceDetection(
            model_selection=0,
            min_detection_confidence=min_detection_confidence
        )

    def detect(self, frame):
        rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        results = self.face_detection.process(rgb)
        bboxes = []

        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                x = int(bboxC.xmin * iw)
                y = int(bboxC.ymin * ih)
                w = int(bboxC.width * iw)
                h = int(bboxC.height * ih)
                bboxes.append((x, y, w, h))

        return bboxes
