import cv2, keyboard
import numpy as np 
import time

picVal = 1

while (True) :
    cap = cv2.VideoCapture("C:\VSCodeMain\Vision2019\Vision2020-Curriculum\CalibrationImages\Cube" + str(picVal) + ".jpg")
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of yellow color in HSV
    lower_yellow = np.array([20,150,150])
    upper_yellow = np.array([70,255,255])
    # Threshold the HSV image to get only yellow colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('hsv',hsv)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    if keyboard.is_pressed('d'):  
        if picVal == 11:
            picVal = picVal - 10
        else :
            picVal = picVal + 1
    if keyboard.is_pressed('a'):
        if picVal == 1:
            picVal = picVal + 10
        else:
            picVal = picVal - 1
    if keyboard.is_pressed('k'):
        cv2.destroyAllWindows()
        break

    
