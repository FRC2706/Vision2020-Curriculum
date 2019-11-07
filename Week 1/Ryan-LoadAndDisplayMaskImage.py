import cv2
import numpy as np



while(1):
    cap = cv2.VideoCapture(r"C:\Users\spice\Downloads\Robotics\Vision2020-Curriculum\Week 1\Cube01.jpg")

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([0,150,150])
    upper_yellow = np.array([120,255,255])


    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    
    if k == 27:
        break
    
cv2.destroyAllWindows()