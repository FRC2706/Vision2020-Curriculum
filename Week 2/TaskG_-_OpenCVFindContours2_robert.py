# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task G - > Find Contours.  This is a seemingly simple command. But is where the real math begins.  
# The command basically converts the masked image into arrays of coordinates that we do math on.  Make sure
# you can do this in your code.  You need to end up with a set of contours!  If you print them to the console
# you will see pages and pages of coordinates go by.  Do that at least once.

# useful links
# https://docs.opencv.org/3.4.7/d4/d73/tutorial_py_contours_begin.html

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
filename = 'C:\Bob\FRC\FRC-2020\Vision2020-Curriculum\CalibrationImages\Cube09.jpg'

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

#im2 = img.copy()
contours,hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow('im2', im2)

print("contours:", contours)
print("hierarchy:", hierarchy)
print("number of contours:", len(contours))

cv2.drawContours(img, contours, -1, (0,0,255), 10)
cv2.imshow('image with contours', img)

# wait for user input to close
cv2.waitKey(0)

#// cleanup and exit
cv2.destroyAllWindows()

