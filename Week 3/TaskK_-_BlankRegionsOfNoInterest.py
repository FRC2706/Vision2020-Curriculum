# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task K - > Blank regions of no interest.  We have discussed the notion
# that there are areas of the image that will never contain information that we want
# our code to process.  Using online search engines find a way using OpenCV to
# modify a photo to contain black pixels in areas with no interest to our code

# Task D1 can be copied here and modified
#https://datacarpentry.org/image-processing/04-drawing/


# Imports!
# Python - import modules of code as required (OpenCV here)
import cv2
import numpy as np
import sys
from pathlib import Path

black = (0, 0, 0)
white = (255, 255, 255) 

# Define string variable for path to file
strImage = "/Users/rachellucyshyn/Documents/GitHub/Vision2020-Curriculum/CalibrationImages/Cube10.jpg"

# load color image with string
imgBGRInput = cv2.imread(strImage)


intBinaryHeight,intBinaryWidth = imgBGRInput.shape[:2] #2 is the number of inputs
#python allows to do this
#imgBGRInput.shape gives the outputs intBinaryHeight and intBinaryWidth right away
#.shape is the rows and colums of pixels in an image

cv2.rectangle(imgBGRInput, (0,0), (intBinaryWidth, int(intBinaryHeight/2)), black, -1)
#cv2.rectangle parameters: image, start point, end point, colour, thickness
#binary width=want the rectangle to stretch the width of the image
#binary height/2 is the height of image divided by 2, so it's only half the height of image. Used to have a -10, just subtracts 10 pixels to make rectangle go down less than half
#if thickness is positive, it's the outline of a rectangle, if negative it fills it in
#TL;DR draw black rectangle on image to cut off top


# display the color image to screen
cv2.imshow('imgCutOff',imgBGRInput)


# wait for user input to close
k = cv2.waitKey(0) #will close when key is pressed

# clean and exit
cv2.destroyAllWindows()