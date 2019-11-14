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


# imports
import numpy as np
import cv2 
from pathlib import Path
import sys

print('Using python version {0}'.format(sys.version))
print('Using OpenCV Version = ', cv2.__version__)
print()

# Define string variable for path to file
strImage = "/Users/rachellucyshyn/Documents/GitHub/Vision2020-Curriculum/CalibrationImages/Cube01.jpg"

# load color image with string
imgBGRInput = cv2.imread(strImage)

# display color image to screen
cv2.imshow('Original Image', imgBGRInput) #window-title= what the window says at top


# mask image to only show yellow

# Convert BGR to HSV
imgHSVinput = cv2.cvtColor(imgBGRInput, cv2.COLOR_BGR2HSV)

#hue = imgHSVinput[:,:,0]
#sat = imgHSVinput[:,:,1]
#val = imgHSVinput[:,:,2]


# Define range of colour in HSV (colour wheel- hue divide by 2 cause python is weird)
lower_yellow = np.array([28,128,128]) #hue/saturation/value (how much black or white)
upper_yellow = np.array([32,255,255]) # 255= zero black zero white

# Threshold the HSV image to get only yellow colors
imgBinaryMask = cv2.inRange(imgHSVinput, lower_yellow, upper_yellow)

# Bitwise-AND mask and original image
imgColorMask = cv2.bitwise_and(imgHSVinput,imgHSVinput, mask = imgBinaryMask) # frame = OG image


# display masked images
#cv2.imshow('Rebecca',imgHSVinput)
cv2.imshow('Binary Mask',imgBinaryMask)
#cv2.imshow('ColorMask',imgColorMask)
    
#cv2.imshow('hue-title',hue)
#cv2.imshow('sat-title',sat)
#cv2.imshow('val-title',val)


contours, hierarchy = cv2.findContours(imgBinaryMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print('found contours = ', len(contours))
print(contours)

imgShowMaths = imgBGRInput.copy()

cv2.drawContours(imgBGRInput, contours, -1, (0,255,0), 20)# last parameter is width of line
cv2.imshow('imgBGRInput', imgBGRInput)

#calculate the moments and centroid
cnt = contours[0]
M = cv2.moments(cnt)
print( M )
print()

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

#parameters:begin coords, end coords, colour, width
cv2.line(imgShowMaths, (cx-10,cy-10), (cx+10, cy+10), (0,255,0),2) #draw lines from opposite corners
cv2.line(imgShowMaths, (cx-10,cy+10), (cx+10, cy-10), (0,255,0),2)
cv2.imshow('imgShowMaths', imgShowMaths)

area = cv2.contourArea(cnt)
print('area = ', area) #in square pixels

# wait for user input to close
k = cv2.waitKey(0) #will close when key is pressed

# clean and exit
cv2.destroyAllWindows()