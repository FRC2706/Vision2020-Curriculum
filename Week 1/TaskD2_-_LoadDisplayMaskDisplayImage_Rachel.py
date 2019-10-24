#// This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
#// This is task D2 - > Load Display Mask Display Image
#// Using Java or Python and OpenCV, write a small bit of code to load an image and display it on your screen.  Then mask it to green or yellow and display that.
#// Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
#// Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
#// Pseudo code to do this is below


#// Imports!
#// Python - import modules of code as required (OpenCV here)
import cv2
import numpy as np
print("ahah")

while(True):
    #// define a string variable for the path to the file
    cap = cv2.VideoCapture(r"/Users/rachellucyshyn/Documents/GitHub/Vision2020-Curriculum/Week 1/Cube01.jpg")

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of yellow color in HSV
    lower_yellow = np.array([0,150,150]) #values Jeremy found on Grip
    upper_yellow = np.array([120,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #// display the masked images to screen
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()