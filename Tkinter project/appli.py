# from tkinter import *
from tkinter import *
q = Tk()
q.title("Application")
b1 = Label(q,text="Name",width=10)
b1.grid(row=0,column=0)
a = Entry(q,fg='black')
a.grid(row=0,column=1)


ev=IntVar()
# ev.set(1)
b2 = Label(q,text="Gender",width=10)
b2.grid(row=1,column=0)
r1=Radiobutton(q,text='male',variable=ev,value=1)
r1.grid(row=1,column=1)
r2=Radiobutton(q,text="female",variable=ev,value=2)
r2.grid(row=1,column=2)
r3=Radiobutton(q,text="trans",variable=ev,value=3)
r3.grid(row=1,column=3)

b3 = Label(q,text="Languages",width=10)
b3.grid(row=2,column=0)
a1=IntVar()
c1=Checkbutton(q,text='cpp',variable=a1,onvalue=1,offvalue=0)
c1.grid(row=2,column=1)
a2=IntVar()
c2=Checkbutton(q,text='java',variable=a2,onvalue=1,offvalue=0)
c2.grid(row=2,column=2)
a3=IntVar()
c3=Checkbutton(q,text='c#',variable=a3,onvalue=1,offvalue=0)
c3.grid(row=2,column=3)


b4 = Label(q,text="Place",width=10)
b4.grid(row=3,column=0)
Lb=Listbox(q)
Listbox()
Lb.insert(1,'malapuram')
Lb.insert(2,'Kozhikode')
Lb.insert(3,'kannur')
Lb.insert(4,'Palakkad')
Lb.insert(6,'kannur')
Lb.grid(row=3,column=1)


k10 = Label(q, text="state", width=25)
k10.grid(row=4, column=0)
variab = StringVar(q)
variab.set("kerala") # default value
# ww = OptionMenu(q, variab, "kerala", "Tamil nadu")
ww = OptionMenu(q,variab,"kerala","TN","goa",)
ww.grid(row=4,column=1)
bb=Button(q,text="submit",command=lambda : submit(),width=5)
bb.grid(row=5,column=2)


def submit():
    w = Tk()
    w.title("Result window")
    nam=a.get()
    k1 = Label(w, text="Name", width=10)
    k1.grid(row=1, column=0)
    k2 = Label(w, text=nam, width=10)
    k2.grid(row=1, column=1)

    if ev.get()==1:
        gendr="male"
    elif ev.get()==2:
        gendr="Female"
    elif ev.get()==3:
        gendr="Transgender"
    else:gendr="Not sepecified"
    k3 = Label(w, text="Gender", width=10)
    k3.grid(row=2, column=0)
    k4 = Label(w, text=gendr, width=10)
    k4.grid(row=2, column=1)

    k5 = Label(w, text="Languages", width=10)
    k5.grid(row=3, column=0)
    i=1
    if a1.get()==1:
        k6 = Label(w, text="Cpp", width=10)
        k6.grid(row=3, column=i)
        i = i + 1
    if a2.get()==1:
        k7 = Label(w, text="Java", width=10)
        k7.grid(row=3, column=i)
        i = i + 1
    if a3.get()==1:
        k8 = Label(w, text="C#", width=10)
        k8.grid(row=3, column=i)

    k9 = Label(w, text="Place", width=10)
    k9.grid(row=4, column=0)
    k9 = Label(w, text=Lb.get(Lb.curselection()), width=10)
    k9.grid(row=4, column=1)

    k11 = Label(w, text="state", width=10)
    k11.grid(row=5, column=0)
    k12=Label(w, text=variab.get(), width=10)
    k12.grid(row=5, column=1)
    bb1 = Button(w, text="Close", command=lambda: clos(), width=5)
    bb1.grid(row=6, column=1)

    def clos():
        w.destroy()


q.mainloop()