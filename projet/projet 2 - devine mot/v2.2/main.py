#coding:utf-8

import tkinter
import random
import time
import joueur


def melanger_str(motMystere):
	motMystere.strip()
	i = 0
	melange = ''
	while i < len(motMystere):
		nbre_alea = random.randint(0,len(motMystere) - 1)
		melange += motMystere[nbre_alea]
		motMystere = motMystere[:nbre_alea] + motMystere[nbre_alea+1:]
	return melange

def get_motInDico():
	with open("dico.txt","r") as dico: #autre façon d'ouvrir des fichier
		listeDico = dico.readlines() # C'EST MIEUX :)
		nbre_ligne = len(listeDico)
		return listeDico[random.randint(0,nbre_ligne)].strip()

def  frame_quit(): 
	app.quit()

def button_new_game():
	varTk_verif.set(f"Le mot mystere était : {var_motMystere.get()}")
	new_game()

def new_game():
	var_motMystere.set(get_motInDico())
	motMystereMelange = melanger_str(var_motMystere.get())
	varTk_indice.set("indice : {}".format(motMystereMelange))
	var_tk_text.set("")



def testValid():
	motMystere = var_motMystere.get()
	saisie = var_tk_text.get()
	if saisie == motMystere:
		varTk_verif.set("c'est cela ! le mot mystere était donc : {}".format(motMystere))
		print("vrai")
		joueur1.setScore(joueur1.getScore() + 1)
		varTk_label_Score.set(f"score : {joueur1.getScore()}")
		time.sleep(1.5)
		new_game()
	else:
		varTk_verif.set("faux !")
		print("faux")

joueur1 = joueur.Joueur() #creation joueur pour enregistré le score 
# creation fenetre -----------------------------------------------
app = tkinter.Tk()
app.resizable(width=False,height=False)
screen_x = app.winfo_screenwidth()
screen_y = app.winfo_screenheight()
window_x = 450
window_y = 250

pos_X = (screen_x // 2) - (window_x // 2)
pos_Y = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x,window_y,pos_X,pos_Y)
app.geometry(geo)

mainFrame = tkinter.Frame(app,width=450,height=250)
mainFrame.pack()

gameFrame = tkinter.LabelFrame(mainFrame,borderwidth=2,width=100,height=150)
gameFrame.place(x=10,y=10)
var_motMystere = tkinter.StringVar()
var_motMystere.set(get_motInDico())
motMystereMelange = melanger_str(var_motMystere.get())

varTk_indice = tkinter.StringVar()
varTk_indice.set("indice : {}".format(motMystereMelange))
tk_label_indice = tkinter.Label(gameFrame, textvariable=varTk_indice)
tk_label_indice.pack()


var_tk_text = tkinter.StringVar()
tk_text = tkinter.Entry(gameFrame,textvariable=var_tk_text)
tk_text.bind("<Return>",lambda event : testValid())
tk_text.pack()



varTk_verif = tkinter.StringVar()
tk_label_verif = tkinter.Label(gameFrame, textvariable=varTk_verif)
tk_label_verif.pack()


tk_btn_valid = tkinter.Button(gameFrame,width=4,height=1,text="check",command=testValid)
tk_btn_valid.pack()
buttonControl = tkinter.LabelFrame(mainFrame,borderwidth=2)
buttonControl.place(x=320,y=5)
btn_newGame = tkinter.Button(buttonControl,text="changer de mot",bg='red',width=16,height=2,command=button_new_game)
btn_newGame.pack()

btn_quit = tkinter.Button(buttonControl,text="quitter le programme", bg='red',width=16,height=2,command=frame_quit)
btn_quit.pack()

FrameScore = tkinter.LabelFrame(mainFrame,borderwidth=2)
FrameScore.place(x=10,y=150)

varTk_label_Score = tkinter.StringVar()
varTk_label_Score.set(f"score : {joueur1.getScore()}")
tk_label_Score = tkinter.Label(FrameScore,textvariable=varTk_label_Score)
tk_label_Score.pack()


app.mainloop()