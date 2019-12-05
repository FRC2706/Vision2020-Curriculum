# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task M - > Sample Mouse Clicks by Pixel. 
# We are going to continue towards our objective of a tool for season kickoff
# This pseudo file will allow us to determine a pixel color by clicking
# on it.  The purpose is to help calibration of the color filter.
# Using web searches for python and pixel color with a mouse, create your own
# code to deliver this capacity.

# online info we already know!
# https://docs.opencv.org/3.4.7/d3/df2/tutorial_py_basic_ops.html
# https://docs.opencv.org/3.4.7/db/d5b/tutorial_py_mouse_handling.html

# online definition of numpy addressing
# https://numpy.org/devdocs/user/quickstart.html

# copy in task D2, based on ideas in link above change it to use BGR and HSV images

# imports
import numpy as np
import cv2
from pathlib import Path

# add callback function for images we wish to query
# BGR pixel mouse callback function on imgImageInput
def onmouse_bgr_pixel_color(event,x,y,flags,params):
    global imgImageInput
    if event == cv2.EVENT_LBUTTONDOWN:
        print('coords',(x,y),'BGR =',imgImageInput[y,x])

# HSV pixel mouse callback function on hsvImageInput
def onmouse_hsv_pixel_color(event,x,y,flags,params):
    global hsvImageInput
    if event == cv2.EVENT_LBUTTONDOWN:
        print('coords',(x,y),'HSV =',hsvImageInput[y,x])

# mask pixel mouse callback function on yellow_mask
def onmouse_mas_pixel_color(event,x,y,flags,params):
    global yellow_mask
    if event == cv2.EVENT_LBUTTONDOWN:
        print('coords',(x,y),'HSV =',yellow_mask[y,x])

# ask pathlib for python code file path and determine root of repository
posCodePath = Path(__file__).absolute()
strVisionRoot = posCodePath.parent.parent

# define a string variable for the path to the image file
#strImageInput = str(strVisionRoot / 'CalibrationImages' / 'Cube01.jpg')
strImageInput = str(strVisionRoot / 'ProblemImages' / 'test-05.jpg')

# load a color image using string
imgImageInput = cv2.imread(strImageInput)

# name the window in advance and create callback
cv2.namedWindow('input-image-title-bar')
cv2.setMouseCallback('input-image-title-bar',onmouse_bgr_pixel_color)

# display the color image to screen
cv2.imshow('input-image-title-bar', imgImageInput)

# Convert BGR to HSV
hsvImageInput = cv2.cvtColor(imgImageInput, cv2.COLOR_BGR2HSV)

# define range of yellow color in HSV
lower_yellow = np.array([28,150,150])
upper_yellow = np.array([37,255,255])

# Threshold the HSV image to get only yellow colors
binary_mask = cv2.inRange(hsvImageInput, lower_yellow, upper_yellow)

# mask the image to only show yellow or green images
# Bitwise-AND mask and original image
yellow_mask = cv2.bitwise_and(hsvImageInput, hsvImageInput, mask=binary_mask)

# name the window in advance and create callback
cv2.namedWindow('hsvImageInput')
cv2.setMouseCallback('hsvImageInput',onmouse_hsv_pixel_color)
cv2.namedWindow('yellow_masked')
cv2.setMouseCallback('yellow_masked',onmouse_mas_pixel_color)

# display the masked images to screen
cv2.imshow('hsvImageInput', hsvImageInput)
cv2.imshow('binary_mask',binary_mask)
cv2.imshow('yellow_masked',yellow_mask)

# wait for user input to close
while(True):
    k = cv2.waitKey(0)
    if k == 27:
        break

# cleanup and exit
cv2.destroyAllWindows()
