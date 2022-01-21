import cv2
from cv2 import FlannBasedMatcher
import numpy as np

def thresholding(img):
    """This function helps in extracting only the colour specified by lower and upper range rest all portions are black"""
    
    # Here we have converted BGR to HSv fromat because it is required to do thresholding 
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([99,0,113])
    upper = np.array([160,255,255])
    masked = cv2.inRange(img_hsv, lower, upper)
    
    return masked


def warp_img(img,points,w,h):
    '''This function takes in the image and points and provides the warped image'''
    #p1 are the points of the 4 red dots in the window they are basically the points on which the perspective change is required 
    pt1 = np.float32(points)
    pt2 = np.float32([[0,0], [w,0], [0,h], [w,h]])
    
    matrix = cv2.getPerspectiveTransform(pt1, pt2)
    
    img_warp = cv2.warpPerspective(img, matrix,(w,h))
    
    return img_warp

def nothing(a):
    '''This is just used for passing so that the code can run seamlessly when the tracker values change'''
    pass

def initialize_trackbar(vals, wT = 480, hT = 240):
    '''This function creates the trackbar '''
    cv2.namedWindow("Trackbars")
    cv2.resizeWindow("Trackbars", 360, 240)
    cv2.createTrackbar("Width Top", "Trackbars", vals[0],wT//2, nothing)
    cv2.createTrackbar("Height Top", "Trackbars", vals[1], hT, nothing)
    cv2.createTrackbar("Width Bottom", "Trackbars", vals[2],wT//2, nothing)
    cv2.createTrackbar("Height Bottom", "Trackbars", vals[3], hT, nothing)
    
    
def val_trackbar(wT= 480, hT = 240):
    '''This function helps to get the values of points that are used for wraping '''
    widthTop = cv2.getTrackbarPos("Width Top", "Trackbars")
    heightTop = cv2.getTrackbarPos("Height Top", "Trackbars")
    widthBottom = cv2.getTrackbarPos("Width Bottom", "Trackbars")
    heightBottom = cv2.getTrackbarPos("Height Bottom", "Trackbars")
    #print(widthTop, heightTop, widthBottom, heightBottom)
    points = np.float32([(widthTop, heightTop), (wT - widthTop, heightTop), 
                        (widthBottom, heightBottom), (wT - widthBottom, heightBottom)])

    return points


def draw_points(img, points):
    '''This function helps to draw the points on the image so that it is easy to warp the image'''
    for x in range(4):
        cv2.circle(img, (int(points[x][0]), int(points[x][1])), 15, (0,0,255), cv2.FILLED)
        
    return img

def get_histogram(img, percent=0.1, display = False):
    '''This function performs the pixel summation so that curve can be extracted '''

    hist_values = np.sum(img, axis=0)
    #print(hist_values)
    max_val = np.max(hist_values)
    min_val = max_val*percent
    index_array = np.where(hist_values >= min_val)
    base_point = int(np.average(index_array))
    # the base point value suggests weather to turn right or left
    print(base_point)
    if display:
        img_hist = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
        for x, intensity in enumerate(hist_values):
            cv2.line(img_hist, (x, img.shape[0]), (x, int(img.shape[0] - intensity // 255)), (255, 0, 255), 1)
            cv2.circle(img_hist, (base_point, img.shape[0]), 20, (0, 255, 255), cv2.FILLED)
        return base_point, img_hist

    return base_point

        
