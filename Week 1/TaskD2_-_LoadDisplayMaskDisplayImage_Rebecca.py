#// This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
#// This is task D2 - > Load Display Mask Display Image
#// Using Java or Python and OpenCV, write a small bit of code to load an image and display it on your screen.  Then mask it to green or yellow and display that.
#// Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
#// Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
#// Pseudo code to do this is below

#// Imports!
#// Python - import modules of code as required (OpenCV here)
#// Java - import classes or packages as required (certain ones)
import numpy as np
import cv2

#define a string variable for the path to the file
file = 'Cube01.jpg'

#load a color image using string
img = cv2.imread(file, cv2.IMREAD_COLOR)

#display the color image to screen
cv2.imshow(file,img)

#mask the image to only show yellow or green images

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_yellow = np.array([0,150,150])
upper_green = np.array([120,255,255])

# Threshold the HSV image to get only yellow and green colors
mask = cv2.inRange(hsv, lower_yellow, upper_green)

# Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask= mask)   

#display the masked images to screen
cv2.imshow('mask',mask)
cv2.imshow('res',res)

#wait for user input to close
cv2.waitKey(0)
  
#cleanup and exit
cv2.destroyAllWindows()