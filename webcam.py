import os
import cv2
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    qr_info = decode(frame)

    if len(qr_info) > 0:
        qr = qr_info[0]

        data = qr.data
        rect = qr.rect
        polygon = qr.polygon

        frame = cv2.rectangle(frame, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height),
                            (0, 255, 0), 5)

        frame = cv2.polylines(frame, [np.array(polygon)], True, (255, 0, 0), 5)

    cv2.imshow("webcam", frame)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()