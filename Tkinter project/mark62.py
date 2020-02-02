from tkinter import *
import socket
import time


q = Tk()
q.title("Chat Client")
bb1=Button(q,text="connect",command=lambda : crt(),width=5)
bb1.grid(row=0,column=0)


bb3 = Button(q, text="Recieve", command=lambda: recv(), width=5)
bb3.grid(row=1, column=0)


b2 = Label(q, text="Server", width=10)
b2.grid(row=2, column=0)
# k2 = Label(q, text= msge, width=10)
# k2.grid(row=2, column=1)


b1 = Label(q,text="Client",width=10)
b1.grid(row=3,column=0)
a = Entry(q,fg='black')
a.grid(row=3,column=1)

bb2=Button(q,text="send",command=lambda : submit(),width=5)
bb2.grid(row=4,column=2)



bb4=Button(q,text="Close",command=lambda : clos(),width=5)
bb4.grid(row=5,column=1)



def crt():
    global s
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    s.connect((host, port))

def submit():
    s.send(a.get().encode())
    if a.get() == "bye":
        # time.sleep(2)
        clos()


def recv():
    global msge
    msge =s.recv(1024).decode()
    k2 = Label(q, text=msge, width=10)
    k2.grid(row=2, column=1)
    if msge == "bye":
        # time.sleep(5)
        clos()


def clos():
    time.sleep(5)
    s.close()
    q.destroy()


q.mainloop()