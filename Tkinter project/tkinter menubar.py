from tkinter import *

root=Tk()
mainmenu=Menu(root)
root.configure(menu=mainmenu)

file=Menu(mainmenu,tearoff=True)
recent=Menu(mainmenu,tearoff=True)

mainmenu.add_cascade(label="File",menu=file)
file.add_cascade(label="File",menu=recent)
file.add_command(label="show",command=lambda : print("show"))
file.add_command(label="Exit",command=root.quit)
# recent.add_cascade(label="Text",menu=text)
recent.add_command(label="info",command=lambda : print("info"))
recent.add_command(label="edit",command=lambda : print("edit"))
root.mainloop() 

