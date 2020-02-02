import threading
import time
import socket
from tkinter import *
from tkinter import scrolledtext


# it should recieve msg and insert to scrolltext
def recieve_msg():
    while(True):
        txt=s.recv(1024).decode()
        if not txt=="":
            logArea.configure(state='normal')
            logArea.insert(END, "->>"+txt+"\n",("lefted",))
            logArea.tag_configure("lefted", justify="left")
            logArea.configure(state='disabled')
            logArea.see(END)


def show(a):
    txt=sendtext.get()
    if txt =="":
        return
    sendtext.delete(0,len(txt))
    logArea.configure(state='normal')
    logArea.insert(END, txt+"<<-Me\n",("righted",))
    logArea.tag_configure("righted", justify="right")
    s.send(txt.encode())
    logArea.configure(state='disabled')
    logArea.see(END)


s=socket.socket()
host=socket.gethostname()
port=1234
s.connect((host,port))
t1=threading.Thread(target=recieve_msg,)
t1.start()
root = Tk()
root.title(' client ')
logArea = scrolledtext.ScrolledText(root,
                    wrap   = WORD,
                    state="disabled",
                    name="logArea"
                )
logArea.grid(padx=10, pady=10,row=0,column=0,columnspan=2)
pro = Label(root, text="Me ->>");
pro.grid(row=2,column=0)
sendtext = Entry(root, width=80)
sendtext.focus_set()
sendtext.bind(sequence="<Return>", func=show)
sendtext.grid(row=2,column=1)
root.mainloop()
