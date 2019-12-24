# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task N - > Sample Filter Contours. 
# Over the weeks, we have explored ways to understand Contours visual and using
# OpenCV functions.  Now lets put these to work and really get down to the 
# challenge of finding FRC vision targets.  Basic idea is to loop through
# sorted contours keeping desired contours only

# use task G
#bigger range (40)


# imports
import numpy as np
import cv2 
from pathlib import Path
import sys

#colours
blue  = (255, 0, 0)
green = (0, 255, 0)
red   = (0, 0, 255)
purple = (128, 0, 128)

# Define string variable for path to file
strImage = "/Users/rachellucyshyn/Documents/GitHub/Vision2020-Curriculum/CalibrationImages/Cube11.jpg"

# load color image with string
imgBGRInput = cv2.imread(strImage)

# display color image to screen
cv2.imshow('Original Image', imgBGRInput) #window-title= what the window says at top

# Convert BGR to HSV
imgHSVinput = cv2.cvtColor(imgBGRInput, cv2.COLOR_BGR2HSV)


# Define range of colour in HSV (colour wheel- hue divide by 2 cause python is weird)
lower_yellow = np.array([28,128,128]) #hue/saturation/value (how much black or white)
upper_yellow = np.array([40,255,255]) # 255= zero black zero white

# Threshold the HSV image to get only yellow colors-mask
imgBinaryMask = cv2.inRange(imgHSVinput, lower_yellow, upper_yellow)

# display masked images
cv2.imshow('Binary Mask',imgBinaryMask)

# Bitwise-AND mask and original image
imgColorMask = cv2.bitwise_and(imgHSVinput,imgHSVinput, mask = imgBinaryMask) # frame = OG image
cv2.imshow('maskedimg',imgColorMask)

#contours
contours, hierarchy = cv2.findContours(imgBinaryMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print('found contours = ', len(contours))
print(contours)

cv2.drawContours(imgBGRInput, contours, -1, (0,255,0), 3)
cv2.imshow('imgBGRInput', imgBGRInput)

cv2.drawContours(imgBinaryMask, contours, -1, (0,255,0), 3)
cv2.imshow('imgBinaryMask', imgBinaryMask)


#find closest cube by height
maxLength = 0
contourLengths = []


contourLengths = [cv2.arcLength(contour, True) for contour in contours]
cutoffLength = 0.1 * max(contourLengths)
    
filteredContours = [];
for i in range(len(contourLengths)):
    if contourLengths[i] >= cutoffLength:
        filteredContours.append(contours[i])

filteredContours = [contour for contour in contours]

print("Number filtered contours:", len(filteredContours))

#wait for user input to close
cv2.waitKey(0)

#cleanup and exit
cv2.destroyAllWindows()
