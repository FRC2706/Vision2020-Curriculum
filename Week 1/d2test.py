#DOESNT WORK

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
# Convert BGR to HSV
hsv = cv2.cvtColor('file', cv2.COLOR_BGR2HSV)

# define range of yellow color in HSV
lower_yellow = np.array([55,75,95])
upper_yellow = np.array([65,85,105])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Bitwise-AND mask and original image
res = cv2.bitwise_and('img',img, mask= mask)

#// display the masked images to screen
cv2.imshow('mask',mask)
cv2.imshow('res',res)


k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save png copy and exit
    cv2.destroyAllWindows()

#// wait for user input to close


#// cleanup and exit
