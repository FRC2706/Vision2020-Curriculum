# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task L1 - > Sample and Cycle Images in Folder. 
# We are going to continue towards our objective of a tool for season kickoff
# This pseudo file is a reasonable attempt at cycling through a folder and 
# displaying all the images (png or jpg only, our decision) navigating with up/down
# arrow keys, and exiting with esc key or q.

# imports
import numpy as np
import cv2
from pathlib import Path
import sys
import os

# define colors
purple = (165, 0, 120)
blue = (255, 0, 0)
green = (0, 255, 255)
red = (0, 0, 255)

# select folder of interest
posCodePath = Path(__file__).absolute()
strVisionRoot = posCodePath.parent.parent
strImageFolder = str(strVisionRoot / 'CalibrationImages')
print (strImageFolder)

# read file names, and filter file names
photos = []
if os.path.exists(strImageFolder):
    for file in sorted(os.listdir(strImageFolder)):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".JPG") or file.endswith(".PNG"):
            photos.append(file)
else:
    print
    print ('Directory', strImageFolder, 'does not exist, exiting ...')
    print
    sys.exit
print (photos)

# set index of files
i = 0
intLastFile = len(photos) -1

# begin main loop indent 1
while (True):

## set image input to indexed list
    strImageInput = strImageFolder + '/' + photos[i]
    print (i, ' ', strImageInput)

## read file
    imgImageInput = cv2.imread(strImageInput)

## display files
    cv2.imshow(strImageInput, imgImageInput)

## loop for user input to close - loop indent 2
    booReqToExit = False # true when user wants to exit
    while (True):

### wait for user to press key
        k = cv2.waitKey(0)
        if k == 27:
            booReqToExit = True # user wants to exit
            break
        if k == 82: # user wants to move down list
            if i - 1 < 0:
                i = intLastFile
            else:
                i = i - 1
            break
        if k == 84: # user wants to move up list
            if i + 1 > intLastFile:
                i = 0
            else:
                i = i + 1
            break
        print (k)

### end of loop indent 2

## test for exit main loop request from user
    if booReqToExit:
        break

## not exiting, close window before loading next
    cv2.destroyWindow(strImageInput)

## end of main loop indent 1

# cleanup and exit
cv2.destroyAllWindows()