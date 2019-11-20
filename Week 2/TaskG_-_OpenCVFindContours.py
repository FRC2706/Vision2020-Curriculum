# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task G - > Find Contours.  This is a seemingly simple command. But is where the real math begins.  
# The command basically converts the masked image into arrays of coordinates that we do math on.  Make sure
# you can do this in your code.  You need to end up with a set of contours!  If you print them to the console
# you will see pages and pages of coordinates go by.  Do that at least once.

# useful links
# https://docs.opencv.org/3.4.7/d4/d73/tutorial_py_contours_begin.html
# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task G - > Find Contours.  This is a seemingly simple command. But is where the real math begins.  
# The command basically converts the masked image into arrays of coordinates that we do math on.  Make sure
# you can do this in your code.  You need to end up with a set of contours!  If you print them to the console
# you will see pages and pages of coordinates go by.  Do that at least once.

# useful links
# https://docs.opencv.org/3.4.7/d4/d73/tutorial_py_contours_begin.html

# Imports!
# Python - import modules of code as required (OpenCV here)

import numpy as np
import cv2
from pathlib import Path
import sys

# define colors for code readablility
colour = (255, 255, 0)

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
# cv2.imshow('input-image-title-bar', imgImageInput)

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
# cv2.imshow('hsvImageInput', hsvImageInput)
cv2.imshow('binary_mask',binary_mask)
# cv2.imshow('yellow_masked',yellow_mask)

# generate the contours and display
contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
imgContours = yellow_mask.copy()
cv2.drawContours(imgContours, contours, -1, colour, 10)
cv2.imshow('contours over yellow mask', imgContours)
#cv2.imshow('findCountours Image result', imgFindCOutput)
print(contours)



cnt = contours [0]
M = cv2.moments(cnt)
print (M)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

cv2.line(imgShowMaths,(cx-10,cy-10),(cx+10,cy+10),(255,255,0),0)



# wait for user input to close
k = cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()