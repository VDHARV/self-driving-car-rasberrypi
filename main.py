from motor import Motor
from Image_Processing.video import get_curve
import Image_Processing.webcam as webcam
import cv2 

######################################
motor = Motor(32, 33, 11, 13, 15, 16)
######################################


def main():
    
    img = webcam.getImg(display=True)
    curve_val = get_curve(img, display=1)
    
    sen = 1.3
    max_val = 0.3
    
    if curve_val > max_val:
        curve_val = max_val
    
    if curve_val < -max_val:
        curve_val = -max_val
    
    if curve_val>0:
        sen = 1.7
        if curve_val< 0.05:
            curve_val = 0
    else:
        if curve_val<-0.08:
            curve_val = 0
    
    motor.move(0.05, curve_val*sen, 0.2)
    cv2.waitKey(1)
    


if __name__ == "__main__":
    while True:
        main()
        