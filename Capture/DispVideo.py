import cv2
import numpy as np
from datetime import datetime as dt

vid = cv2.VideoCapture(2)


while True:
    ret, frame = vid.read()
    cv2.putText( frame, dt.now().strftime('%Y%m%d_%H%M%S.%f'),
            (10, frame.shape[0]-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.35,
            (125,125,125),
            )
    cv2.putText( frame, 'NOT RECORDING',
            (10, 25),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0,0,255),
            )
    cv2.putText( frame, 'Press q to quit',
            (frame.shape[1]-100, frame.shape[0]-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.35,
            (0,255,0),
            )
    cv2.imshow('Display', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break