# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task J - > Camera Orientation and Elevation.  Before the first 3 weeks of build season has
# passed the location of cameras on the robot will likely be decided and/or our choices will be limited.
# During the first 2 of build season is when we can take time to consider camera orientation and 
# elevation and influence it as much as possible on the physical robot.  Generally a vertical difference
# between the camera and rrt vision targets is helpful for certain math.  Conversely, sometimes, we want
# to stay below the top of the vision target to simplify math like the cube in Power Up.  The choice can
# also permit or eliminate additional calculations in some cases.  We will plan to show this in a live
# demo and discuss more.  Use your laptop cam or your own webcam at home, and please experiment with your
# code by looking at targets from difference angles.

# a folder has been added called ProblematicImages, modify your code to look there