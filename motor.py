# Basic Motor module just ot see if its working or not 


import RPi.GPIO as GPIO
from time import sleep 
GPIO.setmode(GRIO.BCM)
GPIO.setwarnings(False)

Ena = 11
In1 = 13
In2 = 15
GPIO.setup(Ena, GPIO.OUT)
GPIO.setup(In1, GPIO.OUT)
GPIO.setup(In2, GPIO.OUT)
pwm = GPIO.PWM(Ena, 100)
pwm.start(0)



pwm.ChangeDutyCycle(60)
GPIO.output(In1, GPIO.LOW)
GPIO.output(In2, GPIO.HIGH)
sleep(5)

pwm.ChangeDutyCycle(0)

