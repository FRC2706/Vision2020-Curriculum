# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task D2 - > Load Display Mask Display Image
# Using Java or Python and OpenCV, write a small bit of code to load an image and display it on your screen.  Then mask it to green or yellow and display that.
# Recommeded starting points -> https:opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
# using https://docs.opencv.org/3.4.7/df/d9d/tutorial_py_colorspaces.html
# Pseudo code to do this is below

# Imports!
# Python - import modules of code as required (OpenCV here)

import numpy as np
import cv2
from pathlib import Path

# define a string variable for the path to the file
strImageInput = str(Path(__file__).parent.parent / 'CalibrationImages' / 'Cube01.jpg')

# load a color image using string
imgImageInput = cv2.imread(strImageInput)

# display the color image to screen
cv2.imshow('input-image-title-bar', imgImageInput)

# Convert BGR to HSV
hsvImageInput = cv2.cvtColor(imgImageInput, cv2.COLOR_BGR2HSV)

# define range of yellow color in HSV
lower_yellow = np.array([29,150,150])
upper_yellow = np.array([31,255,255])

# Threshold the HSV image to get only yellow colors
binary_mask = cv2.inRange(hsvImageInput, lower_yellow, upper_yellow)

# mask the image to only show yellow or green images
# Bitwise-AND mask and original image
yellow_mask = cv2.bitwise_and(hsvImageInput, hsvImageInput, mask=binary_mask)

# display the masked images to screen
cv2.imshow('hsvImageInput', hsvImageInput)
cv2.imshow('binary_mask',binary_mask)
cv2.imshow('yellow_masked',yellow_mask)

# wait for user input to close
k = cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()
