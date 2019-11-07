#// This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
#// This is task D3 - > Load Display Mask Display Video
#// Using Java or Python and OpenCV, write a small bit of code to load an image from a webcam and display it on your screen.  Then mask it to green or yellow and display that.  Keep looping to make a video.  Find some green or yellow object in your house to practice on.
#// Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
#// Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
#// Pseudo code to do this is below

#// Imports!
#// Python - import modules of code as required (OpenCV here)
#// Java - import classes or packages as required (certain ones)

#// Java only - instantiate any required classes and main
#// Java only - load.Library (OpenCV here)  

#// define the camera

#// setup loop

#// load a color image from camera

#// display the color image to screen

#// mask the image to only show yellow or green images

#// display the masked images to screen

#// check for user input to exit loop and if not return to top of loop

#// cleanup and exit.

import cv2
import numpy as np

while(1):

    cap = cv2.VideoCapture(0)

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_yellow = np.array([25,52,75])
    upper_yellow = np.array([102,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()