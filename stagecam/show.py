import cv2 as cv
from .face_tracker import FaceTracker
from .frame_transformer import FrameTransformer

def show(camera_index=0, width=640, height=480, flip=True, window_name="StageCam"):
    cap = cv.VideoCapture(camera_index)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, height)

    if not cap.isOpened():
        print("❌ Cannot open webcam.")
        return

    tracker = FaceTracker()
    transformer = FrameTransformer(width, height)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if flip:
            frame = cv.flip(frame, 1)

        bboxes = tracker.detect(frame)
        transformed = transformer.transform(frame, bboxes)

        cv.imshow(window_name, transformed)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()
