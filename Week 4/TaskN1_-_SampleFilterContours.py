# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task N - > Sample Filter Contours. 
# Over the weeks, we have explored ways to understand Contours visualy and using
# OpenCV functions.  Now lets put these to work and really get down to the 
# challenge of finding FRC vision targets.  Basic idea is to loop through
# sorted contours keeping desired contous only

# let's use task G as a starting point, copied it in here.

# Imports
import numpy as np
import cv2
from pathlib import Path

# define colors for code readablility
purple = (165, 0, 120)
blue = (255, 0, 0)
green = (0, 255, 255)
red = (0, 0, 255)

# ask pathlib for python code file path and determine root of repository
posCodePath = Path(__file__).absolute()
strVisionRoot = posCodePath.parent.parent

# define a string variable for the path to the image file
strImageInput = str(strVisionRoot / 'CalibrationImages' / 'Cube09.jpg')
strImageInput = str(strVisionRoot / 'CalibrationImages' / 'Cube02.jpg')
strImageInput = str(strVisionRoot / 'CalibrationImages' / 'Cube06.jpg')
strImageInput = str(strVisionRoot / 'CalibrationImages' / 'Cube07.jpg')

#strImageInput = str(strVisionRoot / 'ProblemImages' / 'test-05.jpg')

# load a color image using string
imgImageInput = cv2.imread(strImageInput)

# display the color image to screen
# cv2.imshow('input-image-title-bar', imgImageInput)

# Convert BGR to HSV
hsvImageInput = cv2.cvtColor(imgImageInput, cv2.COLOR_BGR2HSV)

# define range of yellow color in HSV
lower_yellow = np.array([28,150,150])
upper_yellow = np.array([40,255,255])

# Threshold the HSV image to get only yellow colors
binary_mask = cv2.inRange(hsvImageInput, lower_yellow, upper_yellow)

# mask the image to only show yellow or green images
# Bitwise-AND mask and original image
yellow_mask = cv2.bitwise_and(hsvImageInput, hsvImageInput, mask=binary_mask)

# display the masked images to screen
# cv2.imshow('hsvImageInput', hsvImageInput)
# cv2.imshow('binary_mask',binary_mask)
# cv2.imshow('yellow_masked',yellow_mask)

# generate the contours
imgFindContours, contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# print number of contours found
intInitialContoursFound = len(contours)
print('Found', intInitialContoursFound, 'contours')

# add loop to display each contour

# sort contours by area, keep only largest
areaSortedContours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
print('Found', len(areaSortedContours), 'contours')

imgContours = yellow_mask.copy()
#cv2.drawContours(imgContours, areaSortedContours, -1, purple, 10)

# create a holder or array for contours we want to keep in first filter
heightSortedContours = []
floMaximumHeight = 0.0
intIndexMaximumHeight = 1

# loop through area sorted contours, i is index, indiv is single contour
for (i, indiv) in enumerate(areaSortedContours):

## determine minimum area rectangle
    rectangle = cv2.minAreaRect(indiv)
    (xm,ym),(wm,hm), am = rectangle
    print (i,hm)

## track tallest contour
    if hm > floMaximumHeight:
        floMaximumHeight = hm
        intIndexMaximumHeight = i

# approach 1
#cv2.drawContours(imgContours, areaSortedContours, intIndexMaximumHeight, purple, 10)

# since we are chosing only 1 tallest, store it to filtered array
heightSortedContours.append(areaSortedContours[intIndexMaximumHeight])

# approach 2
cv2.drawContours(imgContours, heightSortedContours, -1, purple, 10)

cv2.imshow('contours over yellow mask', imgContours)

# wait for user input to close
k = cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()