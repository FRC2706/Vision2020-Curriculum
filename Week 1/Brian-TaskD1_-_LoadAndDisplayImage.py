#// This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
#// This is task D1 - > Load and Display Images
#// Using Java or Python and OpenCV, write a small bit of code to load an image and display it on your screen.
#// Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
#// Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
#// Pseudo code to do this is below

#// Imports!
#// Python - import modules of code as required (OpenCV here)
#// Java - import classes or packages as required (certain ones)

import numpy as np
import cv2
from pathlib import Path

#// Java only - instantiate any required classes and main
#// Java only - load.Library (OpenCV here)  

#// define a string variable for the path to the file

strImageInput = str(Path(__file__).parent.parent) + '/CalibrationImages/Cube01.jpg'

#// load a color image using string

imgImageInput = cv2.imread(strImageInput)

#// display the color image to screen

cv2.imshow('image-title-frame',imgImageInput)

#// wait for user input to close

k = cv2.waitKey(0)

#// cleanup and exit

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()

