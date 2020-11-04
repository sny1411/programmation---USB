#coding:utf-8
import tkinter
"""
StringVar -> chaine de carac[str]
IntVar -> entier[int]
DoubleVar -> flottant[float]
BooleanVar -> bouléen[bool]
"""
#observer:
def observer_Radio(*args):
	if var_gender.get():
		print("changement -> choix Homme")
		var_label_gender.set("c'est un homme")
	else:
		print("changement -> choix Femme")
		var_label_gender.set("c'est une femme")

def update_label(*args):
	var_label.set(var_entry.get())


#creation fenetre et parametre
app = tkinter.Tk()
app.geometry("400x300")
app.title("variable tkinter")

#widget..
var_entry = tkinter.StringVar()
var_entry.trace("w", update_label)
entry = tkinter.Entry(app,textvariable=var_entry)
var_label = tkinter.StringVar()
label = tkinter.Label(app,text="ddd ",textvariable=var_label)

print("label : ",var_label.get())


label.pack()
entry.pack()


var_gender = tkinter.IntVar()
var_gender.trace("w", observer_Radio)
radio1 = tkinter.Radiobutton(app, text="homme", value=1, variable = var_gender)
radio2 = tkinter.Radiobutton(app,text="Femme",value=0, variable=var_gender)

var_label_gender = tkinter.StringVar()
label_gender = tkinter.Label(app,textvariable=var_label_gender)
label_gender.pack()


radio1.pack()
radio2.pack()

#boucle principal
app.mainloop()