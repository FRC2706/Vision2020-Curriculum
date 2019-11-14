# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task G - > Find Contours.  This is a seemingly simple command. But is where the real math begins.  
# The command basically converts the masked image into arrays of coordinates that we do math on.  Make sure
# you can do this in your code.  You need to end up with a set of contours!  If you print them to the console
# you will see pages and pages of coordinates go by.  Do that at least once.

# useful links
# https://docs.opencv.org/3.4.7/d4/d73/tutorial_py_contours_begin.html

# contours=a bunch of xy coordinates. len(contours)=how many points?

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

cv2.drawContours(imgBGRInput, contours, -1, (0,255,0), 3)
cv2.imshow('imgBGRInput', imgBGRInput)

cv2.drawContours(imgBinaryMask, contours, -1, (0,255,0), 3)
cv2.imshow('imgBinaryMask', imgBinaryMask)

# wait for user input to close
k = cv2.waitKey(0) #will close when key is pressed

# clean and exit
cv2.destroyAllWindows()