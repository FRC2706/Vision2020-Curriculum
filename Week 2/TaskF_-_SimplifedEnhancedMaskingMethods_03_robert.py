# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task F - > Simplified and/or Enhanced Masking.  The basic range based mask you probably found
# and used in step D last week is a simple and pure "range" based filter, likely in HSV.  There are 
# different methods out there, mostly based on what is called "Chroma-Key" or perhaps more widely called
# "Green-Screening" for television and movies.

# Checkout this explanation of green screen:
# - https://en.wikipedia.org/wiki/Chroma_key

# Checkout (and try out) these teams vision and masking code:
# - https://github.com/frc1418/2016-vision/blob/master/imgproc/findGreen.py
# - https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/visionPi.py
# - https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/vision.py
# - https://github.com/team3997/ChickenVision/blob/master/ChickenVision.py

# The idea is to experiment with a few lines of their code and use it with your own experiments.  
# Objective is to pick a method to use for making our mask.

# Post a few favourie links and code snippets into your copy of this file, then push to github.

# The code in this file is from the link
#     https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/vision.py

# Imports!
# Python - import modules of code as required (OpenCV here)
import cv2
import numpy as np

# define a string variable for the path to the file
# This gives an error
# filename = 'C:\Bob\FRC\FRC-2020\Vision2020-Curriculum\Week 1\images_green_tape_rl\IMG_6593_green_tape_scaled.jpg'
filename = 'C:\Bob\FRC\FRC-2020\Vision2020-Curriculum\ExtraImages\green_wreath.jpg'

# load a color image using string
img = cv2.imread(filename, cv2.IMREAD_COLOR)

# display the color image to screen
cv2.imshow('image',img)

# Extract green band
imgGreen = img[:,:,1]

# Produce mask by thresholding green in the image
ret, mask = cv2.threshold(imgGreen,200,255,0) # This is the one from the code that did not work well

# display the masked images to screen
cv2.imshow('mask', mask)

# Take the bitwise and of the original image and the mask 
imgMasked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow('imgMasked', imgMasked)

# wait for user input to close
cv2.waitKey(0)

#// cleanup and exit
cv2.destroyAllWindows()
