# chat prgrm client

import pickle
import socket
s=socket.socket()
host=socket.gethostname()
port=1234
s.connect((host,port))


stu_details=s.recv(2048)
f = open("stud.txt", 'wb')
pickle.dump(stu_details,f)
# f.write(stu_details)
f.close()
# print "Server:",
# print s.recv(1024)
# a=raw_input("Client: ")
# s.send(a)
# if a=='bye':
#     s.close()
#     print "chat closed"
#     break
