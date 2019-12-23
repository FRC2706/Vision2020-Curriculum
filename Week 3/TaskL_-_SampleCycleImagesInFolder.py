# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task L - > Sample and Cycle Images in Folder. 
# We are going to continue towards our objective of a tool for season kickoff
# This pseudo file is a reasonable attempt at cycling through a folder and 
# displaying all the images (png or jpg only, our decision) navigating with up/down
# arrow keys, and exiting with esc key or q.




#L2 in brian branch can do different masking techniques

# imports
import numpy as np
import cv2
from pathlib import Path
import os
import glob

# select folder of interest
#folder = str(Path(__file__).parent.parent / 'CalibrationImages')
folder = "/Users/rachellucyshyn/Documents/GitHub/Vision2020-Curriculum/CalibrationImages"

# read and filter file names
filenames = glob.glob(folder + '/' + '*.[jJ][pP][gG]')

# set index of files

i = 0

# begin loop
while(True):
    print('beginning of loop, i =', i)

    ## read file
    img = cv2.imread(filenames[i])

    ## display files
    cv2.imshow('img', img)

    ## wait for user input
    k = cv2.waitKey(0)
    if (k == 27):
        break;
    if k == 97: # user wants to move down list (a)
        i = (i - 1) % len(filenames) # mod (%) gives the remainder-if you go back down it'll give you the last thing
    if k == 122: # user wants to move up list (z)
        i = (i + 1) % len(filenames)

    print('end of loop, i =', i)

    ## end of loop

# cleanup and end of file
cv2.destroyAllWindows()
