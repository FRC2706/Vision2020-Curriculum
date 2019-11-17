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
strImageInput = str(strVisionRoot / 'CalibrationImages' / 'Cube01.jpg')

# load a color image using string
imgImageInput = cv2.imread(strImageInput)

# display the color image to screen
#cv2.imshow('input-image-title-bar', imgImageInput)

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
#cv2.imshow('hsvImageInput', hsvImageInput)
cv2.imshow('binary_mask',binary_mask)
#cv2.imshow('yellow_masked',yellow_mask)

# calculate contours
#im2 = imgImageInput.copy()
im2, contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# show im2
#cv2.imshow('im2',im2)

# print out contours
#print(contours)
#print(hierarchy)

# print count of contours
print('found contours = ',len(contours))
print()

imgShowMaths = imgImageInput.copy()

cv2.drawContours(imgShowMaths, contours, -1, purple, 10)

# calculate the moments and centroid
cnt = contours[0]
M = cv2.moments(cnt)
print(M)
print()

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

# cv2.line (begin coords, end coords, color, width)
cv2.line(imgShowMaths,(cx-10,cy-10),(cx+10,cy+10),red,2)
cv2.line(imgShowMaths,(cx-10,cy+10),(cx+10,cy-10),red,2)

# Area
area = cv2.contourArea(cnt)
print('area = ', area)

# 
cv2.imshow('imgShowMaths', imgShowMaths)

# wait for user input to close
while(True):
    k = cv2.waitKey(0)
    if k == 27:
        break

# cleanup and exit
cv2.destroyAllWindows()