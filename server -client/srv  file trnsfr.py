#!/usr/bin/env python3
import socket
import os
import sys


host = '127.0.0.1'
port = 50001

s = socket.socket()
s.bind((host,port))
print("server Started")
s.listen(1)
while True:
    c, addr = s.accept()
    print("Connection from: " + str(addr))
    # filename = input("Enter new file name: ")
    filename = c.recv(1024).decode()
    cont = c.recv(1024)
    data = cont
    while data:
        data = c.recv(1024)
        cont = cont + data
    print("file recieved successfully")
    myfile = open(filename, "wb")
    myfile.write(cont)
    myfile.close()
    c.close()

