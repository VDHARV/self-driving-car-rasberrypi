import cv2
import numpy as np 
import utils

def get_curve(img):
    img_thres = utils.thresholding(img)
    cv2.imshow("thres", img_thres)
    return 
    


if __name__ == "__main__":
    video = cv2.VideoCapture('Image_Processing/Test1.avi')
    while True:
        success, img = video.read()
        img = cv2.resize(img, (480, 240))
        get_curve(img)
        cv2.imshow("Vid", img)
        cv2.waitKey(1)