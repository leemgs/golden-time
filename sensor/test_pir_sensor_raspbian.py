#!/usr/bin/env python

# PIR Motion Sensor:                ,--------.
# . Power (+DC voltage):  2,2 ------|        |
# . Signal(Output)     : 11,7 ------| PIR    | GPIO17 = pin no. 11
# . GND (Ground)       :  6,6 ------| Sensor |
#                                   `--------'

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

INPUT_SIGNAL=11
COUNT=0

GPIO.setup(INPUT_SIGNAL, GPIO.IN)       # Read output from PIR motion sensor
# GPIO.setup(3, GPIO.OUT)    # LED output pin

while True:
    i=GPIO.input(INPUT_SIGNAL)
    COUNT += 1
    if i==0:                 # When output from motion sensor is LOW
        print COUNT," No people:",i
        # GPIO.output(3, 0)  # Turn OFF LED
        time.sleep(1.1)
    elif i==1:               # When output from motion sensor is HIGH
        print COUNT," People detected:",i
        # GPIO.output(3, 1)  # Turn ON LED
        time.sleep(1.1)


