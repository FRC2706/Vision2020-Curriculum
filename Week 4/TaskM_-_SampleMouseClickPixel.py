# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task M - > Sample Mouse Clicks by Pixel. 
# We are going to continue towards our objective of a tool for season kickoff
# This pseudo file will allow us to determine a pixel color by clicking
# on it.  The purpose is to help calibration of the color filter.
# Using web searches for python and pixel color with a mouse, create your own
# code to deliver this capacity.

# coords of pixel and numbers for colour (depedning on bgr or hsv
# numpy is like spreadsheet -switch x and y to y (row) and x (column)
# have to calibrate to what range of yellow camera sees-change hsv range
#USE THIS TOOL TO CALIBRATE


# online info we already know!
# https://docs.opencv.org/3.4.7/d3/df2/tutorial_py_basic_ops.html
# https://docs.opencv.org/3.4.7/db/d5b/tutorial_py_mouse_handling.html

# online definition of numpy addressing
# https://numpy.org/devdocs/user/quickstart.html

# copy in task D2, based on ideas in link above change it to use BGR and HSV images

# Imports!
# Python - import modules of code as required (OpenCV here)
import cv2
import numpy as np

# Define string variable for path to file
strImage = "/Users/rachellucyshyn/Documents/GitHub/Vision2020-Curriculum/CalibrationImages/Cube11.jpg"

# load color image with string
imgBGRInput = cv2.imread(strImage)

# display color image to screen
cv2.imshow('Original Image', imgBGRInput) #window-title= what the window says at top


# mask image to only show yellow

# Convert BGR to HSV
imgHVSInput = cv2.cvtColor(imgBGRInput, cv2.COLOR_BGR2HSV)

hue = imgHVSInput[:,:,0]
sat = imgHVSInput[:,:,1]
val = imgHVSInput[:,:,2]


# Define range of colour in HSV (colour wheel- hue divide by 2 cause python is weird)
lower_yellow = np.array([28,128,128]) #hue/saturation/value (how much black or white)
upper_yellow = np.array([32,255,255]) # 255= zero black zero white

# Threshold the HSV image to get only yellow colors
imgBinaryMask = cv2.inRange(imgHVSInput, lower_yellow, upper_yellow)

# Bitwise-AND mask and original image
imgColorMask = cv2.bitwise_and(imgHVSInput,imgHVSInput, mask = imgBinaryMask) # frame = OG image


# display masked images
cv2.imshow('HVS',imgHVSInput)
cv2.imshow('Binary Mask',imgBinaryMask)
cv2.imshow('ColorMask',imgColorMask)
    
cv2.imshow('hue-title',hue)
cv2.imshow('sat-title',sat)
cv2.imshow('val-title',val)

def mouseRGB():
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = image[y,x,0]
        colorsG = image[y,x,1]
        colorsR = image[y,x,2]
        colors = image[y,x]
        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        print("Coordinates of pixel: X: ",x,"Y: ",y)


# wait for user input to close
k = cv2.waitKey(0) #will close when key is pressed

# clean and exit
cv2.destroyAllWindows()