# chat prgrm server
import pickle
import socket
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))
s.listen(1)


c,addr = s.accept()
f = open("student.txt", 'r')
stu_details = pickle.load(f)
# stu_details = f.read()
n = len(stu_details)
f.close()
print(stu_details)
c.send(stu_details)
# print(addr)
# a = raw_input("Server: ")
# c.send(a)
# print("Client:",)
# b = c.recv(1024)
# print(b)
# if b=='bye':
#     c.close()
#     print("chat cloed")
#     break

