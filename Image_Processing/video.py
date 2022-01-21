import cv2
import numpy as np
from pygame import image 
import utils

def get_curve(img):
    '''This function returns the curve values'''
    
    img_thres = utils.thresholding(img)
    h, w, c = img.shape
    points = utils.val_trackbar()
    img_warp = utils.warp_img(img_thres, points, w, h)
    img_warped_points = utils.draw_points(img, points)
    
    base_point, img_hist = utils.get_histogram(img_warp, display=True)
    cv2.imshow("thres", img_thres)
    cv2.imshow("wrap", img_warp)
    cv2.imshow("warp points", img_warped_points)
    cv2.imshow("warp points", img_hist)
    
    return 
    


if __name__ == "__main__":
    
    video = cv2.VideoCapture('Image_Processing/Test1.avi')
    initial_trackbar_val = [122, 107, 56, 219]
    utils.initialize_trackbar(initial_trackbar_val)
    frameCounter = 0
    while True:
        frameCounter +=1
        if video.get(cv2.CAP_PROP_FRAME_COUNT) ==frameCounter:
            video.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter=0
        
        success, img = video.read()    
        img = cv2.resize(img, (480, 240))
        get_curve(img)
        cv2.imshow("Vid", img)
        cv2.waitKey(1)