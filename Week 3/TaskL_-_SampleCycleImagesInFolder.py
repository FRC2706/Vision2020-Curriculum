# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task L - > Sample and Cycle Images in Folder. 
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

posCodePath = Path('Cube01.jpg').absolute()
#strVisionRoot = posCodePath.parent.parent.parent.parent.parent.parent.parent.parent.parent
#strImageFolder = str(strVisionRoot / 'CalibrationImages')
strImageFolder = r'C:\Users\spice\Downloads\Robotics\Vision2020-Curriculum\CalibrationImages'
print (strImageFolder)


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

    imgHVSInput = cv2.cvtColor(imgImageInput, cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([28,128,128])
    upper_yellow = np.array([32,255,255])

    imgImageInput = cv2.inRange(imgHVSInput, lower_yellow, upper_yellow)

    imgColorMask = cv2.bitwise_and(imgHVSInput,imgHVSInput, mask = imgImageInput)

    contours, hierarchy = cv2.findContours(imgImageInput, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    print ('found contours = ', len(contours))
    print(contours)

    cv2.drawContours(imgColorMask, contours, -1, (0,255,0), 5)
    cv2.imshow('imgColorMask', imgColorMask)
    cnt = contours[0]
    M = cv2.moments(cnt)
    #print (M)
    
    #cx = int(M['m10']/M['m00'])
    #cy = int(M['m01']/M['m00'])

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print('centroid = ',cx,cy)
    cv2.line(contours,(cx-10,cy-10),(cx+10,cy+10),red,2)
    cv2.line(contours,(cx-10,cy+10),(cx+10,cy-10),red,2)

    img = cv2.imread('Cube01.jpg',0)
    ret,thresh = cv2.threshold(img,127,255,0)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)

    area = cv2.contourArea(cnt)
    print('Area: ' + str(area))

    perimeter = cv2.arcLength(cnt,True)
    print('Perimeter: ' + str(perimeter))

    epsilon = 0.1*cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    print('Epsilon: ' + str(epsilon))
    cv2.drawContours(imgColorMask, approx, -1, (125,125,255), 15)

    hull = cv2.convexHull(cnt)
    cv2.drawContours(imgColorMask, approx, -1, (255,125,125), 10)

    Convextivity = cv2.isContourConvex(cnt)
    if (True):
        print('Convextivity: True')

    else:
        print('Convextivity: False')
    
    #cx = int(M['m10']/M['m00'])
    #cy = int(M['m01']/M['m00'])
    
    #cv2.line(imgColorMask,(cx-10,cy-10),(cx+10,cy+10), (0,255,0),2)
    #cv2.line(imgColorMask,(cx-10,cy+10),(cx+10,cy-10), (0,255,0),2)
    

    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(imgColorMask, [box],0,(0,0,255),2)

    (x,y),radius = cv2.minEnclosingCircle(cnt)
    center = (int(x),int(y))
    radius = int(radius)
    cv2.circle(imgColorMask,center,radius,(255,0,0),2)

    img = cv2.imread('Cube01.jpg',0)
    ret,thresh = cv2.threshold(img,127,255,0)
    contours,hierarchy = cv2.findContours(thresh, 1, 2)
    
    #ellipse = cv2.fitEllipse(cnt)
    #cv2.ellipse(imgColorMask,ellipse,(255,255,0),2)
    
    rows,cols = imgColorMask.shape[:2]
    [vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    cv2.line(imgColorMask,(cols-1,righty),(0,lefty),(255,255,255),2)

    extLeft = tuple(cnt[cnt[:, :, 0].argmin()][0])
    extRight = tuple(cnt[cnt[:, :, 0].argmax()][0])
    extTop = tuple(cnt[cnt[:, :, 1].argmin()][0])
    extBot = tuple(cnt[cnt[:, :, 1].argmax()][0])

    cv2.drawContours(imgColorMask, [cnt], -1, (125, 0, 125), 2)
    cv2.circle(imgColorMask, extLeft, 8, (0, 0, 255), -2)
    cv2.circle(imgColorMask, extRight, 8, (0, 255, 0), -2)
    cv2.circle(imgColorMask, extTop, 8, (255, 0, 0), -2)
    cv2.circle(imgColorMask, extBot, 8, (255, 255, 255), -2)


## display files
    cv2.imshow('imgColorMask', imgColorMask)
## loop for user input to close - loop indent 2
    booReqToExit = False # true when user wants to exit
    while (True):

### wait for user to press key
        k = cv2.waitKey(0)
        if k == 27:
            booReqToExit = True # user wants to exit
            break
        if k == 91: # user wants to move down list
            if i - 1 < 0:
                i = intLastFile
            else:
                i = i - 1
            break
        if k == 93: # user wants to move up list
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
