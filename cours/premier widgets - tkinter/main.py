#coding:utf-8

"""
<nomVariable> = <nom widget>(<widget parent>, <param>...)
"""
import tkinter

def hello():
	print("hello sur la console !")

app = tkinter.Tk()

label_welcome = tkinter.Label(app, text="Bienvenue à tous !")
print(label_welcome.cget("text"))
label_welcome.pack()

message = tkinter.Message(app, text = "coucou \n c'est moa")
message.pack()

button_quit = tkinter.Button(app,text="OK", command=hello)
button_quit.pack()

entry = tkinter.Entry(app, width=45)
entry.pack()

app.mainloop()

