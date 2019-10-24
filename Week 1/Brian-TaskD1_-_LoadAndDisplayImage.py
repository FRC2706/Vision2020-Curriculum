# This is a python code file for Merge Robotics, 2020, Infinite Recharge
# This is task D1 - > Load and Display Images
# Using Python and OpenCV, write a small bit of code to load an image and display it on your screen.
# Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
# Pseudo code to do this is below
# Link to tutorial code found -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_image_display/py_image_display.html#sum-it-up

# Imports!
# modules of code as required (OpenCV here)

import numpy as np
import cv2
from pathlib import Path

# define a string variable for the path to the file
strImageInput = str(Path(__file__).parent.parent / 'CalibrationImages' / 'Cube01.jpg')

# load a color image using string variable
imgImageInput = cv2.imread(strImageInput)

# display the color image to screen
cv2.imshow('image-windows-title-bar',imgImageInput)

# wait for user input to close
k = cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()

