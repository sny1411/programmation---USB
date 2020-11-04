#coding:utf-8
import tkinter

app = tkinter.Tk()
app.geometry("640x480")
app.title("positionnement widgets V2")


btn = tkinter.Button(app,text="BIENVENUE")

btn.place(x=300,y=200)

app.mainloop()