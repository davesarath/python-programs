from tkinter import *
import socket
import time

q = Tk()
q.title("Chat server")
bb1=Button(q,text="create",command=lambda : crt(),width=5)
bb1.grid(row=0,column=0)
b1 = Label(q,text="Sever",width=10)
b1.grid(row=1,column=0)
a = Entry(q,fg='black')
a.grid(row=1,column=1)

bb2=Button(q,text="send",command=lambda : submit(),width=5)
bb2.grid(row=2,column=2)

bb3 = Button(q, text="Receive", command=lambda: recv(), width=5)
bb3.grid(row=3, column=0)


b2 = Label(q, text="Client", width=10)
b2.grid(row=4, column=0)
# k2 = Label(q, text= msge, width=10)
# k2.grid(row=4, column=1)


bb4=Button(q,text="Close",command=lambda : clos(),width=5)
bb4.grid(row=5,column=1)



def crt():
    global s
    s = socket.socket()
    host = socket.gethostname()
    port = 1234
    print(host)

    s.bind((host, port))
    # print s.bind((host, port))
    s.listen(1)
    global c
    global addr
    c, addr = s.accept()
    print(addr)




def submit():
    c.send(a.get().encode())
    if a.get() == "bye":
        # time.sleep(2)
        clos()


def recv():
    global msge
    msge =c.recv(1024).decode()
    k2 = Label(q, text=msge, width=10)
    k2.grid(row=4, column=1)
    if msge == "bye":
        # time.sleep(5)
        clos()


def clos():
    time.sleep(5)
    c.close()
    q.destroy()


q.mainloop()
