#// This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
#// This is task D2 - > Load Display Mask Display Image
#// Using Java or Python and OpenCV, write a small bit of code to load an image and display it on your screen.  Then mask it to green or yellow and display that.
#// Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
#// Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
#// Pseudo code to do this is below

#// Imports!
#// Python - import modules of code as required (OpenCV here)
import numpy as np
import cv2  
print("aahh")

#// define a string variable for the path to the file
file = 'Cube01.jpg'

#// load a color image using string
img = cv2.imread(file, flags=cv2.IMREAD_COLOR)

#// display the color image to screen
cv2.imshow('image',img)

#// mask the image to only show yellow or green images
imageMasked = cv2.inRange(img, np.array([0, 254, 0]), np.array([255, 255, 255]));

#// display the masked images to screen
cv2.imshow('image',imageMasked)


k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save png copy and exit
    cv2.imwrite(file2,img) #use file2 because want to save as png if press 's'
    cv2.destroyAllWindows()

#// wait for user input to close


#// cleanup and exit


