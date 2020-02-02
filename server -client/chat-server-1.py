import socket
def reci(c):
    data = c.recv(1024).decode()
    print("Client :",data)
    if data=="bye":
        print("Client Left")
        global check
        check=False
        c.close()
def snd(c):
    data = input("Server : ")
    c.send(data.encode())
    if data=="bye":
        global check
        check=False
        c.close()
    else:
        reci(c)
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))
while True:
    s.listen(1)
    c,addr = s.accept()
    print(addr)
    check=True
    while check:
        snd(c)
    print("He is gone")