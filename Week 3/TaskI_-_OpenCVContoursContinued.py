# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task I - > OpenCV "Contours Continued."  Not sure if it is clear by now, 
# but OpenCV can do a lot of things, we need to understand what it offers to complete 
# our vision code.  For a given single contour, (meaning it was imaged and masked and 
# converted to a coordinate array), you need to be able to use a number of OpenCV functions.
# Please experiment with the following, easiest is to simply draw them back to a blank image
# or on top of original.  Some very important OpenCV produced actions van only br
# printed to the console or used in code to filter contours.

# Continuing from last week - contour perimeter, contour approximation, bounding rectangles, 
# minimum enclosing circle, fitting elipse, fitting line, aspect ratio
# extent, solidity, equivalent diameter, orientation, points, min/max
# mean color, extreme points

# useful links
# https://docs.opencv.org/3.4.7/dd/d49/tutorial_py_contour_features.html
# https://docs.opencv.org/3.4.7/d1/d32/tutorial_py_contour_properties.html


import cv2
import numpy as np
import sys

print('Using python version {0}'.format(sys.version))
print('Using OpenCV Version = ', cv2.__version__)
print()

strImage = r'C:\Users\spice\Downloads\Robotics\Vision2020-Curriculum\Week 1\Cube03.jpg'

imgBGRInput = cv2.imread(strImage)

#cv2.imshow('Original Image', imgBGRInput)

imgHVSInput = cv2.cvtColor(imgBGRInput, cv2.COLOR_BGR2HSV)

lower_yellow = np.array([28,128,128])
upper_yellow = np.array([32,255,255])

imgBinaryMask = cv2.inRange(imgHVSInput, lower_yellow, upper_yellow)

imgColorMask = cv2.bitwise_and(imgHVSInput,imgHVSInput, mask = imgBinaryMask)

#cv2.imshow('Original',imgBGRInput)
#cv2.imshow('Masked Image',imgBinaryMask)
#cv2.imshow('Coloured Masked Image',imgColorMask)

contours, hierarchy = cv2.findContours(imgBinaryMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print ('found contours = ', len(contours))
print(contours)

#cv2.drawContours(imgBGRInput, contours, -1, (0,255,0), 3)

cv2.drawContours(imgColorMask, contours, -1, (0,255,0), 5)
cv2.imshow('imgColorMask', imgColorMask)
cnt = contours[0]
M = cv2.moments(cnt)
print (M)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

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

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])

cv2.line(imgColorMask,(cx-10,cy-10),(cx+10,cy+10), (0,255,0),2)
cv2.line(imgColorMask,(cx-10,cy+10),(cx+10,cy-10), (0,255,0),2)


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

ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(imgColorMask,ellipse,(255,255,0),2)

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

cv2.imshow('imgColorMask', imgColorMask)

k = cv2.waitKey(0)  
    
cv2.destroyAllWindows() 