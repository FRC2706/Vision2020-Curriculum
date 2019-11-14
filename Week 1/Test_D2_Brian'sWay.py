#// This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
#// This is task D2 - > Load Display Mask Display Image
#// Using Java or Python and OpenCV, write a small bit of code to load an image and display it on your screen.  Then mask it to green or yellow and display that.
#// Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
#// Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
#// Pseudo code to do this is below


# Imports!
# Python - import modules of code as required (OpenCV here)
import cv2
import numpy as np

# Define string variable for path to file
strImage = "/Users/rachellucyshyn/Documents/GitHub/Vision2020-Curriculum/CalibrationImages/Cube08.jpg"

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
cv2.imshow('Rebecca',imgHVSInput)
cv2.imshow('Binary Mask',imgBinaryMask)
cv2.imshow('ColorMask',imgColorMask)
    
cv2.imshow('hue-title',hue)
cv2.imshow('sat-title',sat)
cv2.imshow('val-title',val)


# wait for user input to close
k = cv2.waitKey(0) #will close when key is pressed

# clean and exit
cv2.destroyAllWindows()