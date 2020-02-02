from tkinter import *
from tkinter import scrolledtext
def show(a):
    txt=sendtext.get()
    if txt =="":
        return
    print("hitted enter : ",txt)
    sendtext.delete(0,len(txt))
    logArea.configure(state='normal')
    logArea.insert(END, txt+"<<-Me\n",("centered",))
    logArea.tag_configure("centered", justify="right")

    # logArea.insert(END, txt+"<<-Me\n",("cent",))
    # logArea.tag_configure("cent", justify="left")

    logArea.configure(state='disabled')
    logArea.see(END)


root = Tk()
root.title(' Chat template')
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
