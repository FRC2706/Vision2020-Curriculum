# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task K - > Blank regions of no interest.  We have discussed the notion
# that there are areas of the image that will never contain information that we want
# our code to process.  Using online search engines find a way using OpenCV to
# modify a photo to contain black pixels in areas with no interest to our code

# Task D1 can be copied here and modified

# Imports
import numpy as np
import cv2
from pathlib import Path

# define a string variable for the path to the file
strImageInput = str(Path(__file__).parent.parent / 'CalibrationImages' / 'Cube01.jpg')

# load a color image using string variable
imgImageInput = cv2.imread(strImageInput)

# display the color image to screen
cv2.imshow('image-windows-title-bar',imgImageInput)

# wait for user input to close
k = cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()