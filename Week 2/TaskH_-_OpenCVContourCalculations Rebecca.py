# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task H - > OpenCV "Contour Calculations."  Not sure if it is clear by now, 
# but OpenCV can do a lot of things, we need to understand what it offers to complete 
# our vision code.  For a given single contour, (meaning it was imaged and masked and 
# converted to a coordinate array), you need to be able to use a number of OpenCV functions.
# Please experiment with the following, easiest is to simply draw them back to a blank image
# or on top of original.

# - moments, contour area, contour perimeter, contour approximation, bounding rectangles, 
# minimum enclosing circle, fitting elipse, fitting line, etc.

# useful links
# https://docs.opencv.org/3.4.7/dd/d49/tutorial_py_contour_features.html
# https://docs.opencv.org/3.4.7/d1/d32/tutorial_py_contour_properties.html

import numpy as np
import cv2
from pathlib import Path
import sys

print('Using python version {0}'.format(sys.version))
print('Using OpenCV Version =', cv2.__version__)
print()


strImage = '/Users/rebeccalucyshyn/Documents/Cube01 copy.jpg'

imgImageInput = cv2.imread(strImage)

cv2.imshow('Original Image', imgImageInput)

hsv = cv2.cvtColor(imgImageInput, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([28,128,128])
upper_yellow = np.array([32,255,255])


binary_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

yellow_mask = cv2.bitwise_and(hsv, hsv, mask= binary_mask)

cv2.imshow('Binary Mask', binary_mask,)

    
contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('found contours = ', len(contours))
print(contours)

cv2.drawContours(imgImageInput, contours, -1, (0,255,0), 3) 
cv2.imshow('imgImageInput', imgImageInput)

k = cv2.waitKey(0)

cv2.destroyAllWindows()


