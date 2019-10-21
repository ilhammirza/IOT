import socket
import RPi.GPIO as GPIO
import time
import threading
from mfrc522 import SimpleMFRC522


def makeconn(s,host,port):
    try:
        s.connect((host,port))
        return s
    except socket.timeout:
        makeconn(s,host,port)
def receive(conn):
    while True:
        data=conn.recv(1024)
        datastring=data.decode("utf-8")
        print("data yang diterima"+datastring)
        in1_is_on=int(datastring.split(",")[0])
        in2_is_on=int(datastring.split(",")[1])
        if in1_is_on:
            GPIO.output(in1, True)
            in1_is_on = GPIO.input(in1)
            print(in1_is_on)
        else :
            GPIO.output(in1, False)
            in1_is_on = GPIO.input(in1)
            print(in1_is_on)
        if in2_is_on:
            GPIO.output(in2, True)
            in2_is_on = GPIO.input(in2)
            print(in1_is_on)
        else :
            GPIO.output(in2, False)
            in2_is_on = GPIO.input(in2)
            print(in1_is_on)
        p=str(in1_is_on)+","+str(in2_is_on)
        send(conn,p)
def send(conn,data):
    #pl=data.encode("utf-8")
    conn.sendall(data.encode('utf8'))

def read():
    while True:
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
                    print(in2_is_on)
                else :
                    GPIO.output(in2, True)
                    in2_is_on = GPIO.input(in2)
                    print(in2_is_on)
            p=str(in1_is_on)+","+str(in2_is_on)
            print ("Telah Diubah Menjadi "+p)
            send(conn,p)
            time.sleep(2)
            
        finally:
            GPIO.cleanup()

#Initiate Lamp Control
in1 = 16 #kuning
in2 = 18 #merah

GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.output(in1, True)
GPIO.output(in2, True)

#Initiate RFC522 Control
reader=SimpleMFRC522()

#Initiate Socket Connection 
HOST = '10.242.252.155'  # The server's hostname or IP address
#HOST = '10.201.247.65' 
PORT = 65432        # The port used by the server
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn=makeconn(s,HOST,PORT)

#Get Lamp Data
in1_is_on = GPIO.input(in1)
in2_is_on = GPIO.input(in2)

#Construct Payload
p=str(in1_is_on)+","+str(in2_is_on)
#print (p)

#Send Data for the first time
send(conn,p)

x=threading.Thread(target=read)
x.start()
receive(conn)
