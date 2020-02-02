import threading
import time

def cube(i):
    for j in range(i):
        print(j*j*j,"   cube")
        print("cube")
        time.sleep(9)

def squa(i):
    for j in range(i):
        print(j*j,"square")
        print("square")
        time.sleep(9)


t1=threading.Thread(target=cube,args=(5,))
t2=threading.Thread(target=squa,args=(5,))
t1.start()
t2.start()
