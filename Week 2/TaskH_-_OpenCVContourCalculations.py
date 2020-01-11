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
#from pathLib import Path
import sys

print('Using python version {0}'.format(sys.version))
print('Using OpenCV Version = ', cv2.__version__)
print()

strImage = r'C:\Users\spice\Downloads\Robotics\Vision2020-Curriculum\Week 1\Cube03.jpg'

imgBGRInput = cv2.imread(strImage)

cv2.imshow('Original Image', imgBGRInput)

imgHVSInput = cv2.cvtColor(imgBGRInput, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([28,128,128])
upper_yellow = np.array([32,255,255])

imgBinaryMask = cv2.inRange(imgHVSInput, lower_yellow, upper_yellow)

imgColorMask = cv2.bitwise_and(imgHVSInput,imgHVSInput, mask = imgBinaryMask)

#cv2.imshow('Original',imgBGRInput)
#cv2.imshow('Masked Image',imgBinaryMask)
#cv2.imshow('Coloured Masked Image',imgColorMask)

contours, hierarchy = cv2.findContours(imgBinaryMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print ('found contours = ', len(contours))
print(contours)

imgShowMaths = imgBGRInput.copy()

cv2.drawContours(imgBGRInput, contours, -1, (0,255,0), 3) #Last parameter is for thiccness of contour
cv2.imshow('imgBGRInput', imgBGRInput)

#cv2.drawContours(imgBGRInput, contours, -1, (0,255,0), 3)
#cv2.imshow('imgBGRInput', imgBGRInput)

cnt = contours[0]
M = cv2.moments(cnt)
print( M )
print()

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

cv2.line(imgShowMaths,(cx-10,cy-10),(cx+10,cy+10), (0,255,0),3)
cv2.line(imgShowMaths,(cx-10,cy+10),(cx+10,cy-10), (0,255,0),3)
cv2.imshow('imgShowMaths', imgShowMaths)

area = cv2.contourArea(cnt)
print('area = ', area)

k = cv2.waitKey(0)  
    
cv2.destroyAllWindows() 