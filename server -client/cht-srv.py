# chat prgrm server

import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))

while True:
    s.listen(1)
    c,addr = s.accept()
    print(addr)
    while True:
        a = input("Server: ")
        c.send(a.encode(""))
        print("Client:",end="")
        b = c.recv(1024).decode()
        print(b)
        if (b=='bye'):
            c.close()
            print("chat cloed")
            break

