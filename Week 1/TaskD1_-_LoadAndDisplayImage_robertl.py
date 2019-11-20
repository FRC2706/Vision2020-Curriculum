# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task D1 - > Load and Display Images
# Using Java or Python and OpenCV, write a small bit of code to load an image and display it on your screen.
# Recommeded starting points -> https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html
# Or -> https://www.tutorialspoint.com/opencv/opencv_reading_images.htm
# Pseudo code to do this is below

# Imports!
# Python - import modules of code as required (OpenCV here)
import cv2

# define a string variable for the path to the file
filename = 'C:\Bob\FRC\FRC-2020\Vision2020-Work\images_green_tape_rl\IMG_6593_green_tape.jpg'

# load a color image using string
img = cv2.imread(filename, cv2.IMREAD_COLOR)

# display the color image to screen
cv2.imshow('bonehead', img)

# wait for user input to close
cv2.waitKey(0)

# cleanup and exit
cv2.destroyAllWindows()
