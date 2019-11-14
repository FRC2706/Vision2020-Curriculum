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

import sys
import numpy as np
import cv2
import math


def threshold_range(im, lo, hi):
    unused, t1 = cv2.threshold(im, lo, 255, type=cv2.THRESH_BINARY)
    unused, t2 = cv2.threshold(im, hi, 255, type=cv2.THRESH_BINARY_INV)
    return cv2.bitwise_and(t1, t2)


img = cv2.imread()
cv2.imshow('image', img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)
a, b = 2, 1
h = threshold_range(h, 63, 105)
s = threshold_range(s, 7, 255)
v = threshold_range(v, 67, 242)
#cv2.imshow('s', s)
combined = cv2.bitwise_and(h, cv2.bitwise_and(s,v))


cv2.imshow('image', img)
cv2.waitKey(0)

