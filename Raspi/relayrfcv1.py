import RPi.GPIO as GPIO
import time
from mfrc522 import SimpleMFRC522

in1 = 16
in2 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
reader=SimpleMFRC522()
GPIO.output(in1, True)
GPIO.output(in2, True)
def read():
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(in1, GPIO.OUT)
        GPIO.setup(in2, GPIO.OUT)
        id, text = reader.read()
        print(id)
        print(text)
        if id!="":
            in1_is_on = GPIO.input(in1)
            in2_is_on = GPIO.input(in2)
            if in1_is_on:
                GPIO.output(in1, False)
                in1_is_on = GPIO.input(in1)
                print(in1_is_on)
            else :
                GPIO.output(in1, True)
                in1_is_on = GPIO.input(in1)
                print(in1_is_on)
            if in2_is_on:
                GPIO.output(in2, False)
                in2_is_on = GPIO.input(in2)
                print(in1_is_on)
            else :
                GPIO.output(in2, True)
                in2_is_on = GPIO.input(in2)
                print(in1_is_on)
        time.sleep(2)
    finally:
        GPIO.cleanup()
    
while True:
    read()
    #time.sleep(2)
    