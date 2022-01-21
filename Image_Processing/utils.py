import cv2
import numpy as np

def thresholding(img):
    """This function helps in extracting only the colour specified by lower and upper range rest all portions are black"""
    
    # Here we have converted BGR to HSv fromat because it is required to do thresholding 
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([99,0,113])
    upper = np.array([160,255,255])
    masked = cv2.inRange(img_hsv, lower, upper)
    
    return masked