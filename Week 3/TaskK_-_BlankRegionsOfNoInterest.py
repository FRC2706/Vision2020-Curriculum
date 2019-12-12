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
import time #check how fast code is running

black = (0, 0, 0)
white = (255, 255, 255) 

# Define string variable for path to file
strImage = "/Users/rachellucyshyn/Documents/GitHub/Vision2020-Curriculum/CalibrationImages/Cube11.jpg"

# load color image with string
imgBGRInput = cv2.imread(strImage)


intBinaryHeight,intBinaryWidth = imgBGRInput.shape[:2]
cv2.rectangle(imgBGRInput, (0,0), (intBinaryWidth, int(intBinaryHeight/2-10)), black, -1)


# display the color image to screen
cv2.imshow('imgCutOff',imgBGRInput)


# wait for user input to close
k = cv2.waitKey(0) #will close when key is pressed

# clean and exit
cv2.destroyAllWindows()