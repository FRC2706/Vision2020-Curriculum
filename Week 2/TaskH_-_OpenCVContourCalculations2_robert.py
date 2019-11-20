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

# Imports!
# Python - import modules of code as required (OpenCV here)
import cv2
import numpy as np
import sys

print("Using python version {0}".format(sys.version))
print("Using OpenCV Version = ", cv2.__version__)
print()

# define a string variable for the path to the file
# This gives an error
# filename = 'C:\Bob\FRC\FRC-2020\Vision2020-Curriculum\Week 1\images_green_tape_rl\IMG_6593_green_tape_scaled.jpg'
filename = 'C:\Bob\FRC\FRC-2020\Vision2020-Curriculum\CalibrationImages\Cube01.jpg'

# load a color image using string
img = cv2.imread(filename, cv2.IMREAD_COLOR)

# display the color image to screen
cv2.imshow('image',img)

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Original
#low_green = np.array([25, 52, 72])
#high_green = np.array([102, 255, 255])
#Brian
low_green = np.array([28, 150, 150])
high_green = np.array([32, 255, 255])


mask = cv2.inRange(hsv, low_green, high_green)
imgMasked = cv2.bitwise_and(img, img, mask = mask)

# display the masked images to screen
cv2.imshow('mask', mask)
#cv2.imshow('imageMasked', imgMasked)

im2 = img.copy()
contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow('im2', im2)

print("contours:", contours)
print("hierarchy:", hierarchy)
print("number of contours:", len(contours))

cv2.drawContours(img, contours, -1, (0,0,255), 10)
cv2.imshow('image with contours', img)

cnt = contours[0]
M = cv2.moments(cnt)
print( M )

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

img2 = img.copy();

cv2.line(img2, (cx-10,cy-10), (cx+10,cy+10), (0,255,0),2)
cv2.line(img2, (cx-10,cy+10), (cx+10,cy-10), (0,255,0),2)

cv2.imshow('img2', img2)

area = cv2.contourArea(cnt)
print('area=',area)

# wait for user input to close
cv2.waitKey(0)

#// cleanup and exit
cv2.destroyAllWindows()

