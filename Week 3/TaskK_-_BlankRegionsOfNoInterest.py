# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task K - > Blank regions of no interest.  We have discussed the notion
# that there are areas of the image that will never contain information that we want
# our code to process.  Using online search engines find a way using OpenCV to
# modify a photo to contain black pixels in areas with no interest to our code

# Task D1 can be copied here and modified
# based on ideas from https://datacarpentry.org/image-processing/04-drawing/

# Imports
import numpy as np
import cv2
from pathlib import Path
import time

black = (0,0,0)
white = (255,255,255)

# define a string variable for the path to the file
strImageInput = str(Path(__file__).parent.parent / 'CalibrationImages' / 'Cube10.jpg')

# load a color image using string variable
imgImageInput = cv2.imread(strImageInput)

floStartTimeA = time.perf_counter()
# print ('start = ',floStartTimeA)

# construct a special mask for only the lower portion of the image
binary_mask = np.zeros(shape = imgImageInput.shape, dtype = "uint8")

# draw a white rectangle on only the lower half of the binary mask
intBinaryHeight,intBinaryWidth = binary_mask.shape[:2]
cv2.rectangle(binary_mask, (0,int(intBinaryHeight/2-10)), (intBinaryWidth, intBinaryHeight), white, -1)

# bitwise and the binary mask and the Image Input to produce modified image
imgImageModified = cv2.bitwise_and(imgImageInput, binary_mask)

floDurationA = time.perf_counter() - floStartTimeA
print ('A duration = ' + '{:.2f}'.format(floDurationA * 1000.0) + ' ms')
print ('A frames per second = ' + '{:.1f}'.format(1.0 / floDurationA))
print()

floStartTimeB = time.perf_counter()

# draw a black rectangle on only the upper half of the input image
intBinaryHeight,intBinaryWidth = imgImageInput.shape[:2]
cv2.rectangle(imgImageInput, (0,0), (intBinaryWidth, int(intBinaryHeight/2-10)), black, -1)

floDurationB = time.perf_counter() - floStartTimeB
print ('B duration = ' + '{:.2f}'.format(floDurationB * 1000.0) + ' ms')
print ('B frames per second = ' + '{:.1f}'.format(1.0 / floDurationB))

# display the color image to screen
cv2.imshow('image-windows-title-bar',imgImageModified)

# wait for user input to close
k = cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()