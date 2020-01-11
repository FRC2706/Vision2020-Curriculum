# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task G - > Find Contours.  This is a seemingly simple command. But is where the real math begins.  
# The command basically converts the masked image into arrays of coordinates that we do math on.  Make sure
# you can do this in your code.  You need to end up with a set of contours!  If you print them to the console
# you will see pages and pages of coordinates go by.  Do that at least once.

# useful links
# https://docs.opencv.org/3.4.7/d4/d73/tutorial_py_contours_begin.html

#import numpy as np
#import cv2 as cv
#im = cv.imread(r"C:\Users\spice\Downloads\Robotics\Vision2020-Curriculum\Week 1\Cube01.jpg")
#imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
#ret, thresh = cv.threshold(imgray, 127, 255, 0)
#im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#cv.drawContours(img, contours, -1, (0,255,0), 3)

import numpy as np
import cv2 
#from pathLib import Path
import sys

print('Using python version {0}'.format(sys.version))
print('Using OpenCV Version = ', cv2.__version__)
print()

strImage = r'C:\Users\spice\Downloads\Robotics\Vision2020-Curriculum\Week 1\Cube01.jpg'

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

cv2.drawContours(imgBGRInput, contours, -1, (0,255,0), 3)
cv2.imshow('imgBGRInput', imgBGRInput)

#cv2.drawContours(imgBGRInput, contours, -1, (0,255,0), 3)
#cv2.imshow('imgBGRInput', imgBGRInput)

k = cv2.waitKey(0)  
    
cv2.destroyAllWindows() 