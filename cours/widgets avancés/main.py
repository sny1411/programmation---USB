#coding:utf-8

import tkinter
from tkinter import messagebox

"""
pour les fenetre modal:
- showinfo 
- showerror
- showwarning
- askquestion
- askokcancel
- askyesno
- askretrycancel
"""
def show_modal_window():
	messagebox.showerror("ERREUR","Un probleme est survenu !")

app = tkinter.Tk()

check_widget = tkinter.Checkbutton(app, text="publier ?",offvalue=2,onvalue=5)


radio_widget = tkinter.Radiobutton(app, text="Homme",value=1)
radio_widget2 = tkinter.Radiobutton(app, text="Femme",value=0)

check_widget.pack()
radio_widget.pack()
radio_widget2.pack()

scale_w = tkinter.Scale(app, from_=10,to=100,tickinterval=10)
scale_w.pack()

spin_w = tkinter.Spinbox(app, from_=10,to=100)
spin_w.pack()

btn = tkinter.Button(app,text="déclencher une erreur",command=show_modal_window)
btn.pack()

lb = tkinter.Listbox(app)
lb.insert(1,"Windows")
lb.insert(2,"Linux")
lb.insert(3,"MacOS")
lb.pack()

app.mainloop()