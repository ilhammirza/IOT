import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import socket

HOST = '192.168.88.60'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def read():
    try:
        id, text = reader.read()
        #print(id)
        #print(text)
    finally:
        GPIO.cleanup()
        return(str(id)+" "+text)
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
reader=SimpleMFRC522()
while True:
    x=read()
    if(x!=""):
       s.sendall(x.encode('utf8'))
       data = s.recv(1024)
       x=""
       print("Data Terkirim")