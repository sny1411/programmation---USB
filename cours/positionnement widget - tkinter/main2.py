#coding:utf-8
import tkinter

app = tkinter.Tk()
app.geometry("640x480")
app.title("positionnement widgets V2")


label = tkinter.Label(app,text="Un label")
ent = tkinter.Entry(app)
btn = tkinter.Button(app,text="BIENVENUE")

label.grid(row=0,column=0, columnspan=2, rowspan=3) #-> columnspan=2 : dit qu'il occupe deux caser en largeur
ent.grid(row=0,column=2,padx=10,pady=50)
btn.grid(row=0,column=3,sticky="se")

app.mainloop()