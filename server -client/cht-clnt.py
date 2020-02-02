# chat prgrm client

import socket


s=socket.socket()
host=socket.gethostname()   #server ip
port=1234                   #server port
s.connect((host,port))
while True:
    print("Server:",end="")
    b=s.recv(1024)
    print((b.decode()))
    a=input("Client: ")
    s.send(a.encode())
    if a=='bye':
        s.close()
        print("chat closed")
        break
