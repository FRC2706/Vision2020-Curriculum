#// This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
#// This is task D3 - > Load Display Mask Display Video
#// Using Java or Python and OpenCV, write a small bit of code to load an image from a webcam and display it on your screen.  Then mask it to green or yellow and display that.  Keep looping to make a video.  Find some green or yellow object in your house to practice on.
#// Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
#// Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
#// Pseudo code to do this is below

#// Imports!
#// Python - import modules of code as required (OpenCV here)
#// Java - import classes or packages as required (certain ones)

import numpy as np
import cv2

#// define the camera
cap = cv2.VideoCapture(0)


#// setup loop
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #// display the color image to screen
    cv2.imshow('someframe', frame)

    #// mask the image to only show yellow or green images
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_yellow = np.array([25,52,72])
    upper_green = np.array([102,255,255])

    # Threshold the HSV image to get only yellow and green colors
    mask = cv2.inRange(hsv, lower_yellow, upper_green)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)   

    #// display the masked images to screen
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    #// check for user input to exit loop and if not return to top of loop
    k = cv2.waitKey(1)
    if k == 27:         # wait for ESC key to exit
        break 

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
#// Java only - instantiate any required classes and main
#// Java only - load.Library (OpenCV here)  


#// cleanup and exit.
