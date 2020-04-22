from Tkinter import *
import socket
import time
import threading

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
    # print "haha"
    # t1 = threading.Thread(target=recv(), args=())
    # t1.start()
    # print "hooo"



def submit():
    c.send(a.get())
    if a.get() == "bye":
        # time.sleep(2)
        clos()


# def recv():
#     while True:
#         print "before time skip"
#         # time.sleep(10)
#         re_msg()
#         time.sleep(10)
#         print "aftr time skip"


def recv():
    global msge
    print("inside loop")
    msge =c.recv(1024)
    k2 = Label(q, text=msge, width=10)
    k2.grid(row=4, column=1)
    if msge == "bye":
        # time.sleep(5)
        clos()



def clos():
    c.send("bye")
    time.sleep(5)
    c.close()
    q.destroy()


q.mainloop()
