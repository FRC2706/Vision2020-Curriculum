# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task N - > Sample Filter Contours. 
# Over the weeks, we have explored ways to understand Contours visualy and using
# OpenCV functions.  Now lets put these to work and really get down to the 
# challenge of finding FRC vision targets.  Basic idea is to loop through
# sorted contours keeping desired contous only

# let's use L2 as a starting point, copied it in here.

# imports
import numpy as np
import cv2
from pathlib import Path
import sys
import os
import time

# define colors
purple = (165, 0, 120)
blue = (255, 0, 0)
green = (0, 255, 255)
red = (0, 0, 255)
black = (0, 0, 0)

# definitions of ...
# from Merge ChickenVision 2019
def threshold_range(im, lo, hi):
    unused, t1 = cv2.threshold(im, lo, 255, type=cv2.THRESH_BINARY)
    unused, t2 = cv2.threshold(im, hi, 255, type=cv2.THRESH_BINARY_INV)
    return cv2.bitwise_and(t1, t2)

# select folder of interest
posCodePath = Path(__file__).absolute()
strVisionRoot = posCodePath.parent.parent
#strImageFolder = str(strVisionRoot / 'ProblemImages')
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

# define maskmethod as interger variable
intMaskMethod = 0
print()
print('Mask Method s = Simple In-Range')


# begin main loop indent 1
while (True):

## set image input to indexed list
    strImageInput = strImageFolder + '/' + photos[i]
    print (i, ' ', strImageInput)

## read file
    imgImageInput = cv2.imread(strImageInput)

## blank upper portion from Task K
    intBinaryHeight,intBinaryWidth = imgImageInput.shape[:2]
    cv2.rectangle(imgImageInput, (0,0), (intBinaryWidth, int(intBinaryHeight/2-10)), black, -1)

## display files
    cv2.imshow(strImageInput, imgImageInput)

## Convert BGR to HSV
    hsvImageInput = cv2.cvtColor(imgImageInput, cv2.COLOR_BGR2HSV)

### define range of yellow color in HSV
    lower_yellow = np.array([28,150,150])
    upper_yellow = np.array([40,255,255])

## Depending upon mask method create binary and yellow mask
    if intMaskMethod == 0:
        floStartTimeA = time.perf_counter()
#        print ('start = ',floStartTimeA)
### from 
### Threshold the HSV image to get only yellow colors
        binary_mask = cv2.inRange(hsvImageInput, lower_yellow, upper_yellow)

    elif intMaskMethod == 1:
        floStartTimeA = time.perf_counter()
#        print ('start = ',floStartTimeA)

### from https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/visionPi.py
### set low and high by HSV from         
        hueMin, satMin, valMin = lower_yellow
        hueMax, satMax, valMax = upper_yellow
        #print(hueMin,hueMax,satMin,satMax,valMin,valMax)

### split HSV into separate images
        imghue = hsvImageInput[:,:,0]
        imgsat = hsvImageInput[:,:,1]
        imgval = hsvImageInput[:,:,2]

### create blank images in advance because it's faster
        hueBin = np.zeros(imghue.shape, dtype=np.uint8)
        satBin = np.zeros(imgsat.shape, dtype=np.uint8)
        valBin = np.zeros(imgval.shape, dtype=np.uint8)

### do ranges on HSV separately
        cv2.inRange(imghue, int(hueMin), int(hueMax), hueBin)
        cv2.inRange(imgsat, int(satMin), int(satMax), satBin)
        cv2.inRange(imgval, int(valMin), int(valMax), valBin)

### finish off with the 'mask' extrodinare
        bin = np.copy(hueBin)
        cv2.bitwise_and(satBin, bin, bin)
        cv2.bitwise_and(valBin, bin, bin)

### in our terms this is the binary_mask
        binary_mask = bin.copy()

    elif intMaskMethod == 2:
        floStartTimeA = time.perf_counter()
#        print ('start = ',floStartTimeA)

### from https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/visionPi.py
### set low and high by HSV from         
        hueMin, satMin, valMin = lower_yellow
        hueMax, satMax, valMax = upper_yellow

        h, s, v = cv2.split(hsvImageInput)

        h = threshold_range(h, int(hueMin), int(hueMax))
        s = threshold_range(s, int(satMin), int(satMax))
        v = threshold_range(v, int(valMin), int(valMax))
        binary_mask = cv2.bitwise_and(h, cv2.bitwise_and(s,v))

    else:
        pass # for future methods

## mask the image to only show yellow or green images
## Bitwise-AND mask and original image
    yellow_mask = cv2.bitwise_and(hsvImageInput, hsvImageInput, mask=binary_mask)

    floDurationA = time.perf_counter() - floStartTimeA
    print ('A duration = ' + '{:.2f}'.format(floDurationA * 1000.0) + ' ms')
    print ('A frames per second = ' + '{:.1f}'.format(1.0 / floDurationA))
    print()

## display the masked images to screen
    cv2.imshow('hsvImageInput', hsvImageInput)
    cv2.imshow('binary_mask', binary_mask)
    cv2.imshow('yellow_masked', yellow_mask)

## loop for user input to close - loop indent 2
    booReqToExit = False # true when user wants to exit
    while (True):

### wait for user to press key
        k = cv2.waitKey(0)
        if k == 27:
            booReqToExit = True # user wants to exit
            break
        elif k == 82: # user wants to move down list
            if i - 1 < 0:
                i = intLastFile
            else:
                i = i - 1
            break
        elif k == 84: # user wants to move up list
            if i + 1 > intLastFile:
                i = 0
            else:
                i = i + 1
            break
        elif k == 115:
            intMaskMethod = 0
            print()
            print('Mask Method s = Simple In-Range')
            break
        elif k == 107:
            intMaskMethod = 1
            print()
            print('Mask Method k = Knoxville Method')
            break
        elif k == 109:
            intMaskMethod = 2
            print()
            print('Mask Method m = Merge Mystery Method')
            break
        elif k == 32:
            print()
            print('...repeat...')
            break
        else:
            print (k)

### end of loop indent 2

## test for exit main loop request from user
    if booReqToExit:
        break

## not exiting, close window before loading next
    cv2.destroyWindow(strImageInput)
    cv2.destroyWindow('hsvImageInput')
    cv2.destroyWindow('binary_mask')
    cv2.destroyWindow('yellow_masked')

## end of main loop indent 1

# cleanup and exit
cv2.destroyAllWindows()

