#// This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
#// This is task D2 - > Load Display Mask Display Image
#// Using Java or Python and OpenCV, write a small bit of code to load an image and display it on your screen.  Then mask it to green or yellow and display that.
#// Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
#// Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
#// Pseudo code to do this is below

#// Imports!
#// Python - import modules of code as required (OpenCV here)
#// Java - import classes or packages as required (certain ones)
import cv2
import numpy as np

while(1):
    cap = cv2.VideoCapture(r"C:\Users\spice\Downloads\Robotics\Vision2020-Curriculum\Week 1\Cube02.jpg")

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
