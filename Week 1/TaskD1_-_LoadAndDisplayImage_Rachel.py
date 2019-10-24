#// This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
#// This is task D1 - > Load and Display Images
#// Using Java or Python and OpenCV, write a small bit of code to load an image and display it on your screen.
#// Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
#// Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
#// Pseudo code to do this is below

#// Imports!
# Python - import modules of code as required (OpenCV here)
import numpy as np
import cv2 
print("ai ya")

# define a string variable for the path to the file
file = 'Cube01.jpg'
file2 = 'Cube01.png'

# load a color image using string
img = cv2.imread(file, flags=cv2.IMREAD_COLOR) #use file inside the brackets instead of 'Cube01.jpg' 
#have to use flags to get the color

# display the color image to screen
cv2.imshow('image',img)

k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save png copy and exit
    cv2.imwrite(file2,img) #use file2 because want to save as png if press 's'
    cv2.destroyAllWindows()








