import cv2
import numpy as np 


if __name__ == "__main__":
    video = cv2.VideoCapture('Image_Processing/test.mp4')
    while True:
        success, img = video.read()
        img = cv2.resize(img, (480, 240))
        cv2.imshow("Vid", img)
        cv2.waitKey(1)