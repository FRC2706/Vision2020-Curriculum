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

# This code is based on the link at:
#    https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/visionPi.py

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

# Compute the mask

# Convert BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Pull out the H, S, and V parts separately
hue = hsv[:,:,0]
sat = hsv[:,:,1]
val = hsv[:,:,2]

# Display the H, S, and V components
cv2.imshow('hue', hue)
cv2.imshow('sat', sat)
cv2.imshow('val', val)

# Initialize binary thresholded image matrices
hueBin = np.zeros(hue.shape, dtype=np.uint8)
satBin = np.zeros(sat.shape, dtype=np.uint8)
valBin = np.zeros(val.shape, dtype=np.uint8)

# Set ranges for H, S, and V that represent yellow 
hueMin = 28
hueMax = 32
satMin = 128
satMax = 255
valMin = 128
valMax = 255

# Perform thresholding for H, S, and V separately
cv2.inRange(hue, hueMin, hueMax, hueBin)
cv2.inRange(sat, satMin, satMax, satBin)
cv2.inRange(val, valMin, valMax, valBin)

# Display the binary thresholded images for H, S, and V
cv2.imshow('hueBin', hueBin)
cv2.imshow('satBin', satBin)
cv2.imshow('valBin', valBin)

# The final mask is the one that satifies the threshold for H, S, and V
mask = np.copy(hueBin)
cv2.bitwise_and(satBin, mask, mask)
cv2.imshow('hueBin & satBin', mask)
cv2.bitwise_and(valBin, mask, mask)
cv2.imshow('mask = hueBin & satBin & valBin', mask)

# Take the bitwise and of the original image and the mask 
imgMasked = cv2.bitwise_and(img, img, mask = mask)
cv2.imshow('imgMasked', imgMasked)

# wait for user input to close
cv2.waitKey(0)

#// cleanup and exit
cv2.destroyAllWindows()
