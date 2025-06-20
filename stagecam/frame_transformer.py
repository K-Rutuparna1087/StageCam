import cv2 as cv
import numpy as np
import time

class FrameTransformer:
    def __init__(self, frame_width, frame_height):
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.prev_cx = frame_width // 2
        self.prev_cy = frame_height // 2
        self.zoom_factor = 1.0
        self.target_zoom = 1.5
        self.start_time = time.time()
        self.smooth_speed = 0.1  # fluidity control

    def get_target_center_and_zoom(self, bboxes):
        if not bboxes:
            return self.prev_cx, self.prev_cy, self.zoom_factor

        x_min = min([x for x, y, w, h in bboxes])
        y_min = min([y for x, y, w, h in bboxes])
        x_max = max([x + w for x, y, w, h in bboxes])
        y_max = max([y + h for x, y, w, h in bboxes])

        cx = int((x_min + x_max) / 2)
        cy = int((y_min + y_max) / 2)

        return cx, cy, self.target_zoom

    def smooth_transition(self, current, target):
        return int(current + (target - current) * self.smooth_speed)

    def transform(self, frame, bboxes):
        elapsed = time.time() - self.start_time
        if elapsed < 3:
            return frame  # Wait 3 seconds before starting zoom

        cx, cy, target_zoom = self.get_target_center_and_zoom(bboxes)

        self.prev_cx = self.smooth_transition(self.prev_cx, cx)
        self.prev_cy = self.smooth_transition(self.prev_cy, cy)
        self.zoom_factor += (target_zoom - self.zoom_factor) * self.smooth_speed

        zoom_w = int(self.frame_width / self.zoom_factor)
        zoom_h = int(self.frame_height / self.zoom_factor)

        x1 = max(0, self.prev_cx - zoom_w // 2)
        y1 = max(0, self.prev_cy - zoom_h // 2)
        x2 = min(self.frame_width, x1 + zoom_w)
        y2 = min(self.frame_height, y1 + zoom_h)

        cropped = frame[y1:y2, x1:x2]
        resized = cv.resize(cropped, (self.frame_width, self.frame_height))

        return resized
