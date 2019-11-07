import numpy as np
import cv2
MyImage = r"C:\Users\spice\Downloads\Robotics\Vision2020-Curriculum\Week 1\Cube01.jpg"
img = cv2.imread(MyImage,1)
print(img)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF

#if k == 27:        
#    cv2.destroyAllWindows()
#elif k == ord('s'): 
#    cv2.imwrite(MyImage,img)
#    cv2.destroyAllWindows()
    



