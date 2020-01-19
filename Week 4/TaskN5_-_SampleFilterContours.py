# This is a pseudo code file for Merge Robotics, 2020, Infinite Recharge
# This is task N5 - > Sample Filter Contours. 
# Over the weeks, we have explored ways to understand Contours visualy and using
# OpenCV functions.  Now lets put these to work and really get down to the 
# challenge of finding FRC vision targets.  Basic idea is to loop through
# sorted contours keeping desired contous only

# let's use L4 as a starting point, copied it in here.

# imports
import numpy as np
import cv2
from pathlib import Path
import sys
import os
import time
import math

# define colors
purple = (165, 0, 120)
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
cyan = (252, 252, 3)
magenta = (252, 3, 252)
yellow = (3, 252, 252)
black = (0, 0, 0)
white = (255, 255, 255)
orange = (3, 64, 252) 

# define constraints
floMinExtent = 0.5
floMinArea = 400.0
floImageMultiplier = 3.0
booBlankUpper = True

# definitions of ...
# from Merge ChickenVision 2019
def threshold_range(im, lo, hi):
    unused, t1 = cv2.threshold(im, lo, 255, type=cv2.THRESH_BINARY)
    unused, t2 = cv2.threshold(im, hi, 255, type=cv2.THRESH_BINARY_INV)
    return cv2.bitwise_and(t1, t2)

# function to determine line and slope of ellipse
# ideas from https://stackoverflow.com/questions/33432652/how-draw-axis-of-ellipse
# using a function ideas https://www.geeksforgeeks.org/g-fact-41-multiple-return-values-in-python/
def get_ellipse_major(center, size, angle):
    cost = math.cos(90.0-angle)
    sint = math.sin(90.0-angle)
    xc, yc = center
    xa, xb = size

    LongAxis0X = int(xc - xa*cost)
    LongAxis0Y = int(yc - xa*sint)
    LongAxis1X = int(xc + xa*cost)
    LongAxis1Y = int(yc + xa*sint)

    return (LongAxis0X, LongAxis0Y, LongAxis1X, LongAxis1Y)

def get_ellipse_minor(center, size, angle):
    cost = math.cos(angle)
    sint = math.sin(angle)
    xc, yc = center
    xb, xa = size

    ShortAxis0X = int(xc - xb*sint)
    ShortAxis0Y = int(yc + xb*cost)
    ShortAxis1X = int(xc + xb*sint)
    ShortAxis1Y = int(yc - xb*cost)

    return (ShortAxis0X, ShortAxis0Y, ShortAxis1X, ShortAxis1Y)

# improved ellipse handling from http://raphael.candelier.fr/?blog=Image%20Moments
def get_ellipse(targetEllipse, targetMoments):

    te = targetEllipse
    tm = targetMoments

    # centroid
    cx = tm['m10']/tm['m00']
    cy = tm['m01']/tm['m00']

    # Central moments (intermediary step)
    a = tm['m20']/tm['m00'] - cx**2
    b = 2*(tm['m11']/tm['m00'] - cx*cy)
    c = tm['m02']/tm['m00'] - cy**2

    # Orientation (in radians)
    theta = 1/2*math.atan(b/(a-c)) + (a<c)*math.pi/2

    #Minor and major axis
    ew = math.sqrt(8*(a+c-math.sqrt(b**2+(a-c)**2)))/2
    el = math.sqrt(8*(a+c+math.sqrt(b**2+(a-c)**2)))/2

    # Ellipse focal points
    ed = math.sqrt(el**2-ew**2)
    efx1 = cx + ed*math.cos(theta)
    efy1 = cy + ed*math.sin(theta)
    efx2 = cx - ed*math.cos(theta)
    efy2 = cy - ed*math.sin(theta)

    return (int(efx1), int(efy1), int(efx2), int(efy2))

# from https://stackoverflow.com/questions/41462419/python-slope-given-two-points-find-the-slope-answer-works-doesnt-work/41462583
def get_slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1) 

# homemade! http://home.windstream.net/okrebs/Ch9-1.gif
def get_opposit(hyp, theta):
    return hyp*math.sin(math.radians(theta))

# homemade! http://home.windstream.net/okrebs/Ch9-1.gif
def get_adjacent(hyp, theta):
    return abs(hyp*math.cos(math.radians(theta)))

# select folder of interest
posCodePath = Path(__file__).absolute()
strVisionRoot = posCodePath.parent.parent
#strImageFolder = str(strVisionRoot / 'CalibrationImages')
#strImageFolder = str(strVisionRoot / 'ProblemImages')
#strImageFolder = str(strVisionRoot / 'DistanceImages') 
strImageFolder = str(strVisionRoot / '2706-Elimins-Images')
#strImageFolder = str(strVisionRoot / 'EllipseImages')
#strImageFolder = str(strVisionRoot / 'PowerCellSketchup')

print (strImageFolder)

# read file names, and filter file names
photos = []
if os.path.exists(strImageFolder):
    for file in sorted(os.listdir(strImageFolder)):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".JPG") or file.endswith(".PNG"):
            photos.append(file)
else:
    print
    print ('Directory', strImageFolder, 'does not exist, exiting ...')
    print
    sys.exit
print (photos)

# set index of files
i = 0
intLastFile = len(photos) -1

# define maskmethod as interger variable
intMaskMethod = 2
print()
print('Mask Method s = Simple In-Range')

# begin main loop indent 1
while (True):

    ## start timer for loop as indication of FPS...
    floStartTimeA = time.perf_counter()
    ##print ('start = ',floStartTimeA)

    ## set image input to indexed list
    strImageInput = strImageFolder + '/' + photos[i]
    ##print (i, ' ', strImageInput)

    ## read file
    imgImageInput = cv2.imread(strImageInput)

    if booBlankUpper:
        ## blank upper portion from Task K
        intBinaryHeight,intBinaryWidth = imgImageInput.shape[:2]
        cv2.rectangle(imgImageInput, (0,0), (intBinaryWidth, int(intBinaryHeight/2-10)), black, -1)

    ## Convert BGR to HSV
    hsvImageInput = cv2.cvtColor(imgImageInput, cv2.COLOR_BGR2HSV)

    ## define range of yellow color in HSV
    #lower_yellow = np.array([28,150,150])
    #upper_yellow = np.array([40,255,255])

    lower_yellow = np.array([22,105,145]) #28,150,150
    upper_yellow = np.array([36,255,255]) #32,255,255

    ## Depending upon mask method create binary and yellow mask
    if intMaskMethod == 0:
        ### from 
        ### Threshold the HSV image to get only yellow colors
        binary_mask = cv2.inRange(hsvImageInput, lower_yellow, upper_yellow)

    elif intMaskMethod == 1:
        ### from https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/visionPi.py
        ### set low and high by HSV from         
        hueMin, satMin, valMin = lower_yellow
        hueMax, satMax, valMax = upper_yellow
        #print(hueMin,hueMax,satMin,satMax,valMin,valMax)

        ### split HSV into separate images
        imghue = hsvImageInput[:,:,0]
        imgsat = hsvImageInput[:,:,1]
        imgval = hsvImageInput[:,:,2]

        ### create blank images in advance because it's faster
        hueBin = np.zeros(imghue.shape, dtype=np.uint8)
        satBin = np.zeros(imgsat.shape, dtype=np.uint8)
        valBin = np.zeros(imgval.shape, dtype=np.uint8)

        ### do ranges on HSV separately
        cv2.inRange(imghue, int(hueMin), int(hueMax), hueBin)
        cv2.inRange(imgsat, int(satMin), int(satMax), satBin)
        cv2.inRange(imgval, int(valMin), int(valMax), valBin)

        ### finish off with the 'mask' extrodinare
        bin = np.copy(hueBin)
        cv2.bitwise_and(satBin, bin, bin)
        cv2.bitwise_and(valBin, bin, bin)

        ### in our terms this is the binary_mask
        binary_mask = bin.copy()

    elif intMaskMethod == 2:
        ### from https://github.com/Knoxville-FRC-alliance/Vision-2018-Python/blob/master/visionPi.py
        ### set low and high by HSV from         
        hueMin, satMin, valMin = lower_yellow
        hueMax, satMax, valMax = upper_yellow

        h, s, v = cv2.split(hsvImageInput)

        h = threshold_range(h, int(hueMin), int(hueMax))
        s = threshold_range(s, int(satMin), int(satMax))
        v = threshold_range(v, int(valMin), int(valMax))
        binary_mask = cv2.bitwise_and(h, cv2.bitwise_and(s,v))

    else:
        pass # for future methods

    ## mask the image to only show yellow or green images
    ## Bitwise-AND mask and original image
    yellow_mask = cv2.bitwise_and(hsvImageInput, hsvImageInput, mask=binary_mask)

    ## display the masked images to screen
    #    cv2.imshow('hsvImageInput', hsvImageInput)
    #    cv2.imshow('binary_mask', binary_mask)
    cv2.imshow('yellow_masked', yellow_mask)

    ## generate the contours
    imgFindContours, contours, hierarchy = cv2.findContours(binary_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    ## print number of contours found
    intInitialContoursFound = len(contours)
    print (photos[i])
    print('Found', intInitialContoursFound, 'initial contours')
    print('--==--')

    ## add loop to display each contour
    imgContours = yellow_mask.copy()

    if intInitialContoursFound:
        
        ### sort contours by area, keep only largest
        initialSortedContours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]

        ### filter contours by area, keeping only those over floMinArea
        areaSortedContours = []

        for (j, indiv) in enumerate(initialSortedContours):
            if cv2.contourArea(indiv) > floMinArea:
                areaSortedContours.append(indiv)

        print('Filtered to ', len(areaSortedContours), 'contours by area')

        ### draw the valid contours in thin cyan
        cv2.drawContours(imgContours, areaSortedContours, -1, cyan, 2)

        ### create a holder or array for contours we want to keep in first filter
        tallestValidContour = []
        tallestRectangle = []
        floMaximumHeight = 0.0
        floWidthAtMaxHeight = 0.0
        floAngleAtMaxHeight = 0.0
        intIndexMaximumHeight = -1
        
        ### loop through area sorted contours, j is index, indiv is single contour
        for (j, indiv) in enumerate(areaSortedContours):

            #### determine minimum area rectangle
            rectangle = cv2.minAreaRect(indiv)
            (xm,ym),(wm,hm), am = rectangle

            #### search 'opencv minarearect widht height' and other
            #### program creek link https://www.programcreek.com/python/example/89463/cv2.minAreaRect
            #### noticed https://namkeenman.wordpress.com/2015/12/18/open-cv-determine-angle-of-rotatedrect-minarearect/
            #### this is not really working...
            #### if abs(am) > 45 or (abs(am) == 45 and wm < hm):
            ####     wm, hm = [hm, wm]
            ####     am = 90 + am

            #### more research https://stackoverflow.com/questions/15956124/minarearect-angles-unsure-about-the-angle-returned

            if hm > wm:
                am = am + 90
                wm, hm = [hm, wm]
            else:
                am = am + 180

            if am == 180:
                am = 0

            #### calculate extent as pre-filter suggesting not a cube, handle zero area
            floRectangleArea = wm * hm
            floContourArea = cv2.contourArea(indiv)
            if floRectangleArea != 0.0:
                floContourMinAreaExtent = floContourArea / floRectangleArea 
            else:
                floContourMinAreaExtent = 0.0

            #### print to console, but handle zero height / zero area
            if (hm != 0.0 and floContourArea != 0.0):
                print ('index=',j,'area=',(floContourArea),'extent=','{:.2f}'.format(floContourMinAreaExtent),'height=','{:.1f}'.format(hm),'width=','{:.1f}'.format(wm),'angle=','{:.1f}'.format(am),'minAreaAspect=','{:.1f}'.format(wm/hm))
            else:
                print ('index=',j,'extent= zero','height=','{:.1f}'.format(0.0),'width=','{:.1f}'.format(wm),'angle=','{:.1f}'.format(am),'minAreaAspect= div by zero')                

            #### track tallest contour that looks like a cube based on extent
            if (hm > floMaximumHeight and floContourMinAreaExtent > floMinExtent):
                floMaxHtMinaX = xm
                floMaxHtMinaY = ym
                floMaximumHeight = hm
                floWidthAtMaxHeight = wm
                floAngleAtMaxHeight = am
                intIndexMaximumHeight = j
                tallestRectangle = rectangle
                

        # taking the tallest contour, do some calculations for direction finding
        if intIndexMaximumHeight > -1: # 0 or higher means a valid tallest contour found

            #### add the contour # not really working...
            tallestValidContour.append(areaSortedContours[intIndexMaximumHeight])

            #### print tallest
            print ('extent over', floMinExtent, 'and highest=',intIndexMaximumHeight,'height=','{:.1f}'.format(floMaximumHeight),'width=','{:.1f}'.format(floWidthAtMaxHeight),'angle=','{:.1f}'.format(floAngleAtMaxHeight))

            #### print count of points in contour
            print('there are', len(tallestValidContour[0]),'points in this contour')
            # areaSortedContours[intIndexMaximumHeight]

            #### draw tallest min area rectange
            box = cv2.boxPoints(tallestRectangle)
            box = np.int0(box)
            cv2.drawContours(imgContours,[box],-1,blue,2)

            #### calculate the dimensions to the center of the short sides
            opp = get_opposit(floWidthAtMaxHeight/2.0, floAngleAtMaxHeight)
            adj = get_adjacent(floMaximumHeight/2.0, floAngleAtMaxHeight)

            #print('opp=',opp, 'adj=',adj)

            #### cv2.line to mark x at center of minAreaRect (begin coords, end coords, color, width)
            #cv2.line(imgContours,(int(floMaxHtMinaX)-50,int(floMaxHtMinaY)-50),(int(floMaxHtMinaX)+50,int(floMaxHtMinaY)+50),green,2)
            #cv2.line(imgContours,(int(floMaxHtMinaX)-50,int(floMaxHtMinaY)+50),(int(floMaxHtMinaX)+50,int(floMaxHtMinaY)-50),green,2)

            #print('xc=',floMaxHtMinaX, 'yc=',floMaxHtMinaY, 'hm=',floMaximumHeight, 'wm=',floWidthAtMaxHeight)
            #print('angle=',floAngleAtMaxHeight)
            #### calculate slope of major axis of minAreaRect, and display
            if floAngleAtMaxHeight < 90:
                #print('x1=',floMaxHtMinaX-adj,'y1=', floMaxHtMinaY-opp,'x2=',floMaxHtMinaX+adj,'y2=',floMaxHtMinaY+opp)
                slope = get_slope(floMaxHtMinaX-adj, floMaxHtMinaY-opp, floMaxHtMinaX+adj, floMaxHtMinaY+opp)
                cv2.line(imgContours,(int(floMaxHtMinaX-adj), int(floMaxHtMinaY-opp)), (int(floMaxHtMinaX+adj), int(floMaxHtMinaY+opp)), blue, 5)
            elif floAngleAtMaxHeight > 90:
                #print('x1=',floMaxHtMinaX-adj,'y1=', floMaxHtMinaY+opp,'x2=',floMaxHtMinaX+adj,'y22=',floMaxHtMinaY-opp)
                slope = get_slope(floMaxHtMinaX-adj, floMaxHtMinaY+opp, floMaxHtMinaX+adj, floMaxHtMinaY-opp)
                cv2.line(imgContours,(int(floMaxHtMinaX-adj), int(floMaxHtMinaY+opp)), (int(floMaxHtMinaX+adj), int(floMaxHtMinaY-opp)), blue, 5)
            else: # implies angle is 90
                #print('x1=',floMaxHtMinaX-adj,'y1=', floMaxHtMinaY+opp,'x2=',floMaxHtMinaX+adj,'y22=',floMaxHtMinaY-opp)
                slope = 100
                cv2.line(imgContours,(int(floMaxHtMinaX-adj), int(floMaxHtMinaY+opp)), (int(floMaxHtMinaX+adj), int(floMaxHtMinaY-opp)), blue, 5)

            print('minARect slope=',slope)

            #### draw tallest contour, approach 2
            cv2.drawContours(imgContours, tallestValidContour, -1, orange, 3)

            #### calculate the moments and use in various cases
            M = cv2.moments((areaSortedContours[intIndexMaximumHeight]))
            
            #### need to make sure contour will not break ellipse function
            if len(areaSortedContours[intIndexMaximumHeight]) > 4:
                ##### calculate the ellipse and draw
                ellipse = cv2.fitEllipse(areaSortedContours[intIndexMaximumHeight])
                #print(ellipse)
                cv2.ellipse(imgContours, ellipse ,blue ,3)

                ##### found fancier ellipse function here http://raphael.candelier.fr/?blog=Image%20Moments
                efx1, efy1, efx2, efy2 = get_ellipse(ellipse, M)
                #print (efx1, efy1, efx2, efy2)
                cv2.line(imgContours,(efx1, efy1),(efx2, efy2),blue,3)

                ##### calculate slope of major axis from ellipse
                slope = get_slope(efx1, efy1, efx2, efy2)
                print('ellipse slope=',slope)

                #ellcent, ellaxe, ellang = ellipse
                #maja0x, maja0Y, maja1x, maja1y = get_ellipse_major(ellcent, ellaxe, ellang)
                #cv2.line(imgContours,(maja0x, maja0Y),(maja1x, maja1y),red,3)

        else:
            print('no cubes found...')

        ### repeating if statment but target reconstruction
        #if intIndexMaximumHeight > -1: # 0 or higher means a valid tallest contour found
        if tallestValidContour:

            #### height carries through all possibilities
            targetHeight = floMaximumHeight

            #### a simple single cube defined by ascpect
            aspect = floWidthAtMaxHeight / floMaximumHeight
            if aspect < 1.7:
                print('single cube, aspect less than 1.7')
                targetWidth = floWidthAtMaxHeight
                targetX = int(M['m10']/M['m00'])
                targetY = int(M['m01']/M['m00'])

            #### use slope to adjust for multi-cube face on vs trailing away
            elif abs(slope) < 0.1: 
                print('multi cube, slope less than 0.1')
                targetWidth = floWidthAtMaxHeight
                #M = cv2.moments((areaSortedContours[intIndexMaximumHeight]))
                targetX = int(M['m10']/M['m00'])
                targetY = int(M['m01']/M['m00'])

            elif abs(slope) >= 0.1:
                print('multi cube, slope more than 0.1')
                targetWidth = targetHeight * 1.55

                #cnt = (areaSortedContours[intIndexMaximumHeight])
                cnt = tallestValidContour[0]
                if slope > 0: # start with lower right
                    print('fade to the left')
                    # extreme points
                    rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
                    topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
                    bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
                    btmX, btmY = bottommost
                    rgtX, rgtY = rightmost
                    cv2.circle(imgContours, rightmost, 6, red, -1)
                    cv2.circle(imgContours, bottommost, 6, blue, -1)
                    #cv2.circle(imgContours, (rgtX,btmY), 12, cyan, -1)
                    targetX = (rgtX - int(targetWidth/2.0))
                    targetY = (btmY - int(targetHeight/2.0))

                elif slope < 0: # start with lower left
                    print('fade to the right')
                    # extreme points
                    leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
                    topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
                    bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
                    btmX, btmY = bottommost
                    lftX, lftY = leftmost
                    cv2.circle(imgContours, leftmost, 6, green, -1)
                    cv2.circle(imgContours, bottommost, 6, blue, -1)
                    #cv2.circle(imgContours, (lftX,btmY), 12, cyan, -1)
                    targetX = (lftX + int(targetWidth/2.0))
                    targetY = (btmY - int(targetHeight/2.0))

            else:
                pass

            ### print target on screen            
            cv2.circle(imgContours, (targetX,targetY), int(targetHeight/4), purple, 4, -1)
            cv2.circle(imgImageInput, (targetX,targetY), int(targetHeight/4), purple, 4, -1)


    ## calculate duration of processing as FPS...
    print('--==--')
    floDurationA = time.perf_counter() - floStartTimeA
    print ('code duration estimate = ', '{:.2f}'.format(floDurationA * 1000.0) + ' ms')
    print ('frames per second = ', '{:.1f}'.format(1.0 / floDurationA))
    print()

    ## display modified size original image
    imgShowInput = cv2.resize(imgImageInput, None, fx=floImageMultiplier, fy=floImageMultiplier, interpolation = cv2.INTER_AREA)
    cv2.imshow(photos[i], imgShowInput)
    cv2.moveWindow(photos[i],100,50)

    ## show result over color mask at modified size
    imgShowHSV = cv2.resize(imgContours, None, fx=floImageMultiplier, fy=floImageMultiplier, interpolation = cv2.INTER_AREA)
    cv2.imshow('contours over yellow mask', imgShowHSV)
    cv2.moveWindow('contours over yellow mask',600,50)

    ## loop for user input to close - loop indent 2
    booReqToExit = False # true when user wants to exit

    while (True):

        ### wait for user to press key
        k = cv2.waitKey(0)
        if k == 27:
            booReqToExit = True # user wants to exit
            break
        elif k == 82: # user wants to move down list
            if i - 1 < 0:
                i = intLastFile
            else:
                i = i - 1
            break
        elif k == 84: # user wants to move up list
            if i + 1 > intLastFile:
                i = 0
            else:
                i = i + 1
            break
        elif k == 115:
            intMaskMethod = 0
            print()
            print('Mask Method s = Simple In-Range')
            break
        elif k == 107:
            intMaskMethod = 1
            print()
            print('Mask Method k = Knoxville Method')
            break
        elif k == 109:
            intMaskMethod = 2
            print()
            print('Mask Method m = Merge Mystery Method')
            break
        elif k == 32:
            print()
            print('...repeat...')
            break
        else:
            print (k)

        ### end of loop indent 2

    ## test for exit main loop request from user
    if booReqToExit:
        break

    ## not exiting, close windows before loading next
    cv2.destroyAllWindows()
    ## cv2.destroyWindow(photos[i])
    ## cv2.destroyWindow('contours over yellow mask')
    ##    cv2.destroyWindow('hsvImageInput')
    ##    cv2.destroyWindow('binary_mask')
    ##    cv2.destroyWindow('yellow_masked')

# end of main loop indent 1

# cleanup and exit
cv2.destroyAllWindows()

