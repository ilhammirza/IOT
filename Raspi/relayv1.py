import RPi.GPIO as GPIO
import time

in1 = 16
in2 = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

GPIO.output(in1, False)
GPIO.output(in2, False)
x=0.05
try:
    while True:
          GPIO.output(in1, True)
          time.sleep(x)
          GPIO.output(in1, False)
          GPIO.output(in2, True)
          time.sleep(x)
          GPIO.output(in2, False)
          x=x+0.25
          
except KeyboardInterrupt:
    GPIO.cleanup()