# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task G - > Find Contours.  This is a seemingly simple command. But is where the real math begins.  
# The command basically converts the masked image into arrays of coordinates that we do math on.  Make sure
# you can do this in your code.  You need to end up with a set of contours!  If you print them to the console
# you will see pages and pages of coordinates go by.  Do that at least once.

# useful links
# https://docs.opencv.org/3.4.7/d4/d73/tutorial_py_contours_begin.html

import numpy as np
import cv2

im = cv2.imread('C:\Bob\FRC\FRC-2020\Vision2020-Work\images_rl\die.jpg')
cv2.imshow('original image', im)

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imshow('greyscale image', imgray)

#ret, thresh = cv2.threshold(imgray, 127, 255, 0)
ret, thresh = cv2.threshold(imgray, 50, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh)
# im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('thresh after contours', thresh)

print("number contours:", len(contours))

cv2.drawContours(im, contours, -1, (0,255,0), 3)
cv2.imshow('original image with contours', im)

#print("contours:", contours)

# wait for user input to close
cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()
