#coding:utf-8
import tkinter


# add_checkbutton()
# add_radiobutton()
# add_separator()

def show_about():
	about_window = tkinter.Toplevel(app)
	about_window.title("A propos")
	lb =tkinter.Label(about_window,text="Bonjour !")
	lb.pack()


app = tkinter.Tk()
app.geometry("640x480")
app.title("Création de Menu")

mainmenue = tkinter.Menu(app)

first_menu = tkinter.Menu(mainmenue, tearoff=0)
first_menu.add_command(label="option1")
first_menu.add_command(label="option2")
first_menu.add_command(label="quitter", command=app.quit)

second_menu = tkinter.Menu(mainmenue,tearoff=0)
second_menu.add_command(label="commande 1")
second_menu.add_command(label="a propos", command=show_about)

mainmenue.add_cascade(label="premier",menu=first_menu)
mainmenue.add_cascade(label="second",menu=second_menu)

app.config(menu=mainmenue)
app.mainloop()