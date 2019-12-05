# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task G - > Find Contours.  This is a seemingly simple command. But is where the real math begins.  
# The command basically converts the masked image into arrays of coordinates that we do math on.  Make sure
# you can do this in your code.  You need to end up with a set of contours!  If you print them to the console
# you will see pages and pages of coordinates go by.  Do that at least once.

# useful links
# https://docs.opencv.org/3.4.7/d4/d73/tutorial_py_contours_begin.html

import numpy as np
import cv2
from pathlib import Path
import sys

print('Using python version {0}'.format(sys.version))
print('Using OpenCV Version = ', cv2.__version__)
print()

purple = (165, 0, 120)
blue = (255, 0, 0)
green = (0, 255, 255)
red = (0, 0, 255)

# ask pathlib for python code file path and determine root of repository
posCodePath = Path(__file__).absolute()
# print(posCodePath)
strVisionRoot = posCodePath.parent.parent
# print(strVisionRoot)

# define a string variable for the path to the image file
strImageInput = str(strVisionRoot / 'CalibrationImages' / 'Cube09.jpg')

# load a color image using string
imgImageInput = cv2.imread(strImageInput)

# display the color image to screen
cv2.imshow('input-image-title-bar', imgImageInput)

# Convert BGR to HSV
hsvImageInput = cv2.cvtColor(imgImageInput, cv2.COLOR_BGR2HSV)

# define range of yellow color in HSV
lower_yellow = np.array([28,150,150])
upper_yellow = np.array([32,255,255])

# Threshold the HSV image to get only yellow colors
binary_mask = cv2.inRange(hsvImageInput, lower_yellow, upper_yellow)

# mask the image to only show yellow or green images
# Bitwise-AND mask and original image
yellow_mask = cv2.bitwise_and(hsvImageInput, hsvImageInput, mask=binary_mask)

# display the masked images to screen
cv2.imshow('hsvImageInput', hsvImageInput)
cv2.imshow('binary_mask',binary_mask)
cv2.imshow('yellow_masked',yellow_mask)

# calculate contours
#im2 = imgImageInput.copy()
im2, contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# show im2
# cv2.imshow('im2',im2)

# print out contours
print(contours)
print(hierarchy)

# print count of contours
print('found contours = ',len(contours))
print()

cv2.drawContours(imgImageInput, contours, -1, purple, 10)
cv2.imshow('imgImageInput', imgImageInput)

# wait for user input to close
while(True):
    k = cv2.waitKey(0)
    if k == 27:
        break

# cleanup and exit
cv2.destroyAllWindows()
