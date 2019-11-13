# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task E - > Find ideas online for inspiration.  There is an large and perhaps confusing quantity 
# of code on the internet, primarily github.  You need to develop the ability to find it, understand it, 
# and use parts where appropriate, and give credit where it is due.  Please give the following google
# searches some time and see what you can find.  

# Google searches:
# - "chief Delphi vision 2019"
# - "github frc python vision"
# - "github frc java vision"

# Post a few favourie links into your copy of this file, then push to github.

https://github.com/team3997/ChickenVision/blob/master/ChickenVision.py

#Angles in radians

#image size ratioed to 16:9
image_width = 256
image_height = 144

#Lifecam 3000 from datasheet
#Datasheet: https://dl2jx7zfbtwvr.cloudfront.net/specsheets/WEBC1010.pdf
diagonalView = math.radians(68.5)

#16:9 aspect ratio
horizontalAspect = 16
verticalAspect = 9

#Reasons for using diagonal aspect is to calculate horizontal field of view.
diagonalAspect = math.hypot(horizontalAspect, verticalAspect)
#Calculations: http://vrguy.blogspot.com/2013/04/converting-diagonal-field-of-view-and.html
horizontalView = math.atan(math.tan(diagonalView/2) * (horizontalAspect / diagonalAspect)) * 2
verticalView = math.atan(math.tan(diagonalView/2) * (verticalAspect / diagonalAspect)) * 2

#Focal Length calculations: https://docs.google.com/presentation/d/1ediRsI-oR3-kwawFJZ34_ZTlQS2SDBLjZasjzZ-eXbQ/pub?start=false&loop=false&slide=id.g12c083cffa_0_165
H_FOCAL_LENGTH = image_width / (2*math.tan((horizontalView/2)))
V_FOCAL_LENGTH = image_height / (2*math.tan((verticalView/2)))
#blurs have to be odd
green_blur = 7
orange_blur = 27

# define range of green of retroreflective tape in HSV
lower_green = np.array([0,220,25])
upper_green = np.array([101, 255, 255])
#define range of orange from cargo ball in HSV
lower_orange = np.array([0,193,92])
upper_orange = np.array([23, 255, 255])

#Flip image if camera mounted upside down
def flipImage(frame):
    return cv2.flip( frame, -1 )

#Blurs frame
def blurImg(frame, blur_radius):
    img = frame.copy()
    blur = cv2.blur(img,(blur_radius,blur_radius))
    return blur

# Masks the video based on a range of hsv colors
# Takes in a frame, range of color, and a blurred frame, returns a masked frame
def threshold_video(lower_color, upper_color, blur):


    # Convert BGR to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # hold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Returns the masked imageBlurs video to smooth out image

    return mask



# Finds the tape targets from the masked image and displays them on original stream + network tales
def findTargets(frame, mask):
    # Finds contours
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
    # Take each frame
    # Gets the shape of video
    screenHeight, screenWidth, _ = frame.shape
    # Gets center of height and width
    centerX = (screenWidth / 2) - .5
    centerY = (screenHeight / 2) - .5
    # Copies frame and stores it in image
    image = frame.copy()
    # Processes the contours, takes in (contours, output_image, (centerOfImage)
    if len(contours) != 0:
        image = findTape(contours, image, centerX, centerY)
    else:
        # pushes that it deosn't see vision target to network tables
        networkTable.putBoolean("tapeDetected", False)

    # Shows the contours overlayed on the original video
    return image

# Finds the balls from the masked image and displays them on original stream + network tables
def findCargo(frame, mask):
    # Finds contours
    _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)
    # Take each frame
    # Gets the shape of video
    screenHeight, screenWidth, _ = frame.shape
    # Gets center of height and width
    centerX = (screenWidth / 2) - .5
    centerY = (screenHeight / 2) - .5
    # Copies frame and stores it in image
    image = frame.copy()
    # Processes the contours, takes in (contours, output_image, (centerOfImage)
    if len(contours) != 0:
        image = findBall(contours, image, centerX, centerY)
    else:
        # pushes that it doesn't see cargo to network tables
        networkTable.putBoolean("cargoDetected", False)
    # Shows the contours overlayed on the original video
    return image



https://github.com/chargingchampions/FRC-2019-Vision-Code-Python/blob/master/VisionRunner.py
import cv2
import numpy as np
from networktables import NetworkTables
from grip import GripRetroreflectivePipeline

exposure_ID = 15
#brightness_ID = 10
#brightness = 0
exposure = -10000
H_FOV = 59.70292
V_FOV = 33.58289
min_slant = -85
max_slant = -65
y_displacement = 2

#to be calculated once started
width = None
height = None
focalLength = None
centerX = None
centerY = None


def extra_processing(pipeline, frame):
    """
    Performs extra processing on the pipeline's outputs and publishes data to NetworkTables.
    :param pipeline: the pipeline that just processed an image
    :return: None
    """
    x_angle_table = []
    distance_table = []

    print(pipeline.filter_contours_output.__len__())
    for contour in pipeline.filter_contours_output:
        #returns a Box2D structure which contains following detals
        #( top-left corner(x,y), (width, height), angle of rotation )
        rect = cv2.minAreaRect(contour)
        point, dimensions, angle = rect
        boxPoints = cv2.boxPoints(rect)
        
        #keeping only the right-slanted rectangles
        if (angle > min_slant and angle < max_slant):
            boxPoints = np.int0(boxPoints)
            x, y = np.sum(boxPoints, axis = 0)/4
            #now, x and y are the coordinates of the center pixel of the target
            
            #calculating the angles
            x_angle = np.degrees(np.arctan((centerX-x)/focalLength))
            y_angle = np.degrees(np.arctan((centerY-y)/focalLength))
            print('x_angle=',x_angle,'y_angle=',y_angle)
            
            #calculating distance along horizontal plane
            distance = y_displacement/np.tan(np.radians(y_angle))
            print('distance=',distance)
            
            x_angle_table.append(x_angle)
            distance_table.append(distance)
            cv2.drawContours(frame,[boxPoints],0,(0,0,255),2)
            cv2.circle(frame, (int(x), int(y)), 4, (0, 0, 255))

    # Publish to the '/vision/lines' network table
    #table = NetworkTables.getTable('/vision/lines')
    #table.putNumberArray('x', center_x_positions)
    #table.putNumberArray('y', center_y_positions)
    #table.putNumberArray('width', widths)
    #table.putNumberArray('height', heights)
    return frame