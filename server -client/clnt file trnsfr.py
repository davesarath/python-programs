#!/usr/bin/env python3
import socket, os.path, datetime, sys
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re


host = '127.0.0.1'
port = 50001
s = socket.socket()
s.connect((host, port))

Tk().withdraw()
Filepath = askopenfilename()
print(Filepath)
Filename =re.split(r"/",Filepath)
Filename=Filename[len(Filename)-1]
# Filename=re.findall("[a-zA-Z]*|[0-9]*[.][a-z]+$",Filepath)
print(Filename)

s.send(Filename.encode())
# Filename = input("Type in ur file ")
myfile = open(Filepath, "rb")
data = myfile.read(1024)
while data:
    s.send(data)
    data = myfile.read(1024)

print("file successfully transfered")
myfile.close()
s.close()
