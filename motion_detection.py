import cv2
import numpy as np

def main():

    w = 800
    h = 600

    cap = cv2.VideoCapture(0)

    cap.set(3, w)
    cap.set(4, h)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
        ret, frame = cap.read()

        cv2.imshow("original", frame)
        if cv2.waitKey(0) == 27:
            break
    cv2.destroyAllWindows()
    cap.release()

