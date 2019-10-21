import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
def write():
    try:
            text = input('New data:')
            print("Now place your tag to write")
            reader.write(text)
            print("Written")
    finally:
            GPIO.cleanup()
def read():
    try:
        id, text = reader.read()
        print(id)
        print(text)
    finally:
        GPIO.cleanup()
            
reader=SimpleMFRC522()
while True:
    read()

            



