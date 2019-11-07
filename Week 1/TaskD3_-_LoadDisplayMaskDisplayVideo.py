import cv2
import numpy as np

while(1):

    cap = cv2.VideoCapture(0)

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([28,128,128])
    upper_yellow = np.array([32,255,255])

    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('Original',frame)
    cv2.imshow('Masked Image',mask)
    cv2.imshow('Coloured Masked Image',res)
    k = cv2.waitKey(0) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()