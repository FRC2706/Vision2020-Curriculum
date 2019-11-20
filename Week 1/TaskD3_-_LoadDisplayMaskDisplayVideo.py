# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task D3 - > Load Display Mask Display Video
# Using Java or Python and OpenCV, write a small bit of code to load an image from a webcam and display it on your screen.  Then mask it to green or yellow and display that.  Keep looping to make a video.  Find some green or yellow object in your house to practice on.
# Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
# Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
# Pseudo code to do this is below

# Imports!
# Python - import modules of code as required (OpenCV here)
import cv2;
import numpy as np;

# define the camera
cap = cv2.VideoCapture(0)

# setup loop
while True:

    # load a color image from camera
    ret, frame = cap.read();

    # display the color image to screen
    cv2.imshow('frame', frame)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # mask the image to only show yellow or green images
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    mask = cv2.inRange(hsv, low_green, high_green)
    frameMasked = cv2.bitwise_and(frame, frame, mask = mask)
    
    # display the masked images to screen
    cv2.imshow('mask', mask)
    cv2.imshow('frameMasked',frameMasked)

    # check for user input to exit loop and if not return to top of loop
    key = cv2.waitKey(1) # 1 means display for 1 ms then close
    if key == 27: # Esc key
        break

# cleanup and exit.
cap.release()
cv2.destroyAllWindows()
