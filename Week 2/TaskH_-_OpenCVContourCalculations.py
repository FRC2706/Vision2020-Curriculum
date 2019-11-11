# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task H - > OpenCV "Contour Calculations."  Not sure if it is clear by now, 
# but OpenCV can do a lot of things, we need to understand what it offers to complete 
# our vision code.  For a given single contour, (meaning it was imaged and masked and 
# converted to a coordinate array), you need to be able to use a number of OpenCV functions.
# Please experiment with the following, easiest is to simply draw them back to a blank image
# or on top of original.

# - moments, contour area, contour perimeter, contour approximation, bounding rectangles, 
# minimum enclosing circle, fitting elipse, fitting line, etc.

# useful links
# https://docs.opencv.org/3.4.7/dd/d49/tutorial_py_contour_features.html
# https://docs.opencv.org/3.4.7/d1/d32/tutorial_py_contour_properties.html


import numpy as np
import cv2
from pathlib import Path

print('OpenCV Version = ', cv2.__version__)
print()

# define colors for code readablility
purple = (165, 0, 120)
red = (0, 0, 255)

# ask pathlib for python code file path and determine root of repository
posCodePath = Path(__file__).absolute()
# print(posCodePath)
strVisionRoot = posCodePath.parent.parent
# print(strVisionRoot)

# define a string variable for the path to the image file
strImageInput = str(strVisionRoot / 'CalibrationImages' / 'Cube09.jpg')

# load a color image using string
imgImageInput = cv2.imread(strImageInput)

# display the color image to screen
# cv2.imshow('input-image-title-bar', imgImageInput)

# Convert BGR to HSV
hsvImageInput = cv2.cvtColor(imgImageInput, cv2.COLOR_BGR2HSV)

# define range of yellow color in HSV
lower_yellow = np.array([28,150,150])
upper_yellow = np.array([32,255,255])

# Threshold the HSV image to get only yellow colors
binary_mask = cv2.inRange(hsvImageInput, lower_yellow, upper_yellow)

# mask the image to only show yellow or green images
# Bitwise-AND mask and original image
yellow_mask = cv2.bitwise_and(hsvImageInput, hsvImageInput, mask=binary_mask)

# display the masked images to screen
# cv2.imshow('hsvImageInput', hsvImageInput)
#cv2.imshow('binary_mask',binary_mask)
# cv2.imshow('yellow_masked',yellow_mask)

# generate the contours and display
#imgFindOutput, contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
ret, contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
imgContours = yellow_mask.copy()
cv2.drawContours(imgContours, contours, -1, purple, 10)
#cv2.imshow('contours over yellow mask', imgContours)
#print(contours)

# Moment and Centroid
cnt = contours[0]
#print('original',cnt)
M = cv2.moments(cnt)
#print( M )
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print('centroid = ',cx,cy)
cv2.line(imgContours,(cx-10,cy-10),(cx+10,cy+10),(0,255,0),2)
cv2.line(imgContours,(cx-10,cy+10),(cx+10,cy-10),(0,255,0),2)

# Area
area = cv2.contourArea(cnt)
print('area = ', area)

# Perimeter
perimeter = cv2.arcLength(cnt,True)
print('perimeter = ', perimeter)

# Contour Approximation
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
print('approx', approx)

# Hull
hull = cv2.convexHull(cnt)
print('hull', hull)

# Check Convexity
print('convexity is', cv2.isContourConvex(cnt))

# straight bounding rectangle
x,y,w,h = cv2.boundingRect(cnt)
print('straight bounding rectangle = ', (x,y) ,w,h)
cv2.rectangle(imgContours,(x,y),(x+w,y+h),(0,255,0),2)

# rotated rectangle
rect = cv2.minAreaRect(cnt)
print('rotated rectangle = ',rect)
(x,y),(width,height),angleofrotation = rect
#box = cv2.boxPoints(rect)
#box = np.int0(box)
#cv2.drawContours(imgContours,[box],0,(0,0,255),2)

# minimum enclosing circle
(x,y),radius = cv2.minEnclosingCircle(cnt)
print('minimum enclosing circle = ', (x,y),radius)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(imgContours,center,radius,(0,255,0),2)

# fitting an elipse
ellipse = cv2.fitEllipse(cnt)
#print(ellipse)
# search ellipse to find it return a rotated rectangle in which the ellipse fits
(x,y),(width,height),angleofrotation = ellipse
cv2.ellipse(imgContours,ellipse,(0,255,0),2)

# fitting a line
rows,cols = binary_mask.shape[:2]
#[vx,vy,x,y] = cv.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01) #errors in VS Code, search online and found fix
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(imgContours,(cols-1,righty),(0,lefty),(0,255,0),2)

# Display the contours and maths generated
cv2.imshow('contours and math over yellow mask', imgContours)

# wait for user input to close
k = cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()