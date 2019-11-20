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
img = cv2.imread('C:\Bob\FRC\FRC-2020\Vision2020-Curriculum\ExtraImages\star.jpg',0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
cv2.imshow('thresh', thresh)
# im2, contours, hierarchy = cv2.findContours(thresh, 1, 2)
contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
M = cv2.moments(cnt)
print(M)

cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
print("cx=", cx, " cy=", cy)

area = cv2.contourArea(cnt)
print("area=", area)

perimeter = cv2.arcLength(cnt,True)
print("perimeter=", perimeter)

epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)

# hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]

hull = cv2.convexHull(cnt)

k = cv2.isContourConvex(cnt)

x,y,w,h = cv2.boundingRect(cnt)
cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)

cv2.imshow('img after boundingRect', img)

rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(img,[box],0,(255,255,255),2)

cv2.imshow('img after drawCountours', img)

(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
cv2.circle(img,center,radius,(255,255,255),2)

cv2.imshow('img after minEnclosingCircle', img)

ellipse = cv2.fitEllipse(cnt)
cv2.ellipse(img,ellipse,(255,255,255),2)

cv2.imshow('img after ellipse', img)

rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
cv2.line(img,(cols-1,righty),(0,lefty),(255,255,255),2)

cv2.imshow('img after line', img)

# wait for user input to close
cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()

