#coding:utf-8
import tkinter

app = tkinter.Tk()
app.geometry("640x480")
app.title("positionnement widgets")

mainframe = tkinter.LabelFrame(app, text="Titre", width=300,height=200,borderwidth=2)
mainframe.pack()

btn = tkinter.Button(app,text="BIENVENUE")
btn.pack()

app.mainloop()