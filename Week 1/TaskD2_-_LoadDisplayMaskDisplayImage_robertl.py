# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task D2 - > Load Display Mask Display Image
# Using Java or Python and OpenCV, write a small bit of code to load an image and display it on your screen.  Then mask it to green or yellow and display that.
# Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
# Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
# Pseudo code to do this is below

# Imports!
# Python - import modules of code as required (OpenCV here)
import cv2
import numpy as np

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
# Rebecca
low_green = np.array([35, 64, 77])
high_green = np.array([85, 255, 255])
mask = cv2.inRange(hsv, low_green, high_green)
imgMasked = cv2.bitwise_and(img, img, mask = mask)

# display the masked images to screen
cv2.imshow('mask', mask)
cv2.imshow('imageMasked', imgMasked)

# wait for user input to close
cv2.waitKey(0)

#// cleanup and exit
cv2.destroyAllWindows()
