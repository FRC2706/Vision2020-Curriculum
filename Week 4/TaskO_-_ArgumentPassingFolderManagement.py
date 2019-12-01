# 
# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task O - > Argument passing and Folder management. 
# We are going to continue towards our objective of a tool for season kickoff
# This pseudo file will allow us to pass instructions to our code from the
# command line about what folders to use and eventually other desired options.

# online search result
# https://levelup.gitconnected.com/the-easy-guide-to-python-command-line-arguments-96b4607baea1

# copy in task L, based on ideas in link above change it to take a folder from command line

# imports
import numpy as np
import cv2
from pathlib import Path
import sys
import os
import argparse

# define command line options, and read strFolderOfInterest
parser = argparse.ArgumentParser(description='Task O - Argument Passing for Folder Management')
parser.add_argument('--f', default='', type=str, help='This is the desired folder')
args = parser.parse_args()
strFolderOfInterest = args.f

print()
print(strFolderOfInterest)
print()

if not strFolderOfInterest:
    print()
    print('Directory argument --f missing, exiting ...')
    print()
    sys.exit()

# define colors
purple = (165, 0, 120)
blue = (255, 0, 0)
green = (0, 255, 255)
red = (0, 0, 255)

# select folder of interest
posCodePath = Path(__file__).absolute()
strVisionRoot = posCodePath.parent.parent
strImageFolder = str(strVisionRoot / strFolderOfInterest)
print (strImageFolder)

# read file names, and filter file names
photos = []
if os.path.exists(strImageFolder):
    for file in sorted(os.listdir(strImageFolder)):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".JPG") or file.endswith(".PNG"):
            photos.append(file)
    print (photos)
else:
    print
    print ('Directory', strImageFolder, 'contains no photos, exiting ...')
    print
    sys.exit

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
