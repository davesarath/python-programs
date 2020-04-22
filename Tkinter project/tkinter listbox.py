from tkinter import *
root=Tk()
mainmenu=Menu(root)
root.configure(menu=mainmenu)
file=Menu(mainmenu,tearoff=False)
recent=Menu(mainmenu,tearoff=False)
mainmenu.add_cascade(label="File",menu=file)
file.add_cascade(label="File",menu=recent)
file.add_command(label="Exit",command=root.quit)

ls=Listbox(root)
ls.grid(row=1,column=0)
ls.insert(END,"English")
ls.insert(END,"Malayalam")
ls.insert(END,"Hindi")
ls.insert(END,"Tamil")
txt=StringVar()

lbl=Label(root,textvar=txt,font=70)
lbl.grid(row=4,column=0)
def show(e):
    y=ls.curselection()
    # print(y)
    x=ls.get(y)
    txt.set(x)
    # lbl.configure(text="asdf")

ls.bind("<<ListboxSelect>>",show)


root.mainloop()
