import socket

def reci(s):
    data = s.recv(1024).decode()
    print("Server :",data)
    if data=="bye":
        print("Server Left")
        global check
        check=False
        s.close()
    else:
        snd(s)

def snd(s):
    data = input("Client : ")
    s.send(data.encode())
    if data=="bye":
        global check
        check=False
        s.close()

s=socket.socket()
host=socket.gethostname()
port=1234
s.connect((host,port))
check=True
while check:
    reci(s)