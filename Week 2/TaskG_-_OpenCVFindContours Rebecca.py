# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task G - > Find Contours.  This is a seemingly simple command. But is where the real math begins.  
# The command basically converts the masked image into arrays of coordinates that we do math on.  Make sure
# you can do this in your code.  You need to end up with a set of contours!  If you print them to the console
# you will see pages and pages of coordinates go by.  Do that at least once.

# useful links
# https://docs.opencv.org/3.4.7/d4/d73/tutorial_py_contours_begin.html

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


