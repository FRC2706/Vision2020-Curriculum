# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task K - > Blank regions of no interest.  We have discussed the notion
# that there are areas of the image that will never contain information that we want
# our code to process.  Using online search engines find a way using OpenCV to
# modify a photo to contain black pixels in areas with no interest to our code

# Task D1 can be copied here and modified


import cv2
import numpy as np
import sys

print('Using python version {0}'.format(sys.version))
print('Using OpenCV Version = ', cv2.__version__)
print()

strImage = r'C:\Users\spice\Downloads\Robotics\Vision2020-Curriculum\Week 1\Cube11.jpg'

imgBGRInput = cv2.imread(strImage)

imgHVSInput = cv2.cvtColor(imgBGRInput, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([28,128,128])
upper_yellow = np.array([32,255,255])

imgBinaryMask = cv2.inRange(imgHVSInput, lower_yellow, upper_yellow)

imgColorMask = cv2.bitwise_and(imgHVSInput,imgHVSInput, mask = imgBinaryMask)

dimensions = imgColorMask.shape

height = imgColorMask.shape[0]
width = imgColorMask.shape[1]

print (height)
print (width)

cv2.rectangle(imgColorMask, (0,0), (int(width), int(height/2)), (0,0,0), -1)

cv2.imshow('imgColorMask', imgColorMask)

k = cv2.waitKey(0)
    
cv2.destroyAllWindows() 
