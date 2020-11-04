#coding:utf-8
import tkinter
"""
Button-3 -> souris
KP_Enter -> clavier numerique entré
Escape -> échape
Control -> control
"""



def func(event):
	print("La touche [A] a été pressée")

app = tkinter.Tk()
app.geometry("320x240")

entry_w = tkinter.Entry(app)
entry_w.bind('<Return>', func)

entry_w.pack()

app.mainloop()