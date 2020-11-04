#coding:utf-8
import pickle
import tkinter
import random

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







def testValid():
	saisie = var_tk_text.get()
	if saisie == motMystere:
		varTk_verif.set("c'est cela ! le mot mystere était donc : {}".format(motMystere))
		print("1")
	elif saisie == "cheat()":
		varTk_verif.set("ENNNN CHEATER !!!!! le mot mystere était {}".format(motMystere))
		print("2")
	else:
		varTk_verif.set("faux !")
		print("3")

def getVar1():
	var_tk_text = tkinter.StringVar()
	return var_tk_text



def game():
	motMystere = get_motInDico()
	motMystereMelange = melanger_str(motMystere)
	print(motMystere," ",motMystereMelange)

	new_game = tkinter.Tk()
	new_game.resizable(width=False,height=False)
	screen_x = new_game.winfo_screenwidth()
	screen_y = new_game.winfo_screenheight()
	window_x = 350
	window_y = 150

	pos_X = (screen_x // 2) - (window_x // 2)
	pos_Y = (screen_y // 2) - (window_y // 2)

	geo = "{}x{}+{}+{}".format(window_x,window_y,pos_X,pos_Y)
	new_game.geometry(geo)

	mainFrame = tkinter.Frame(new_game,width=300,height=150)
	mainFrame.pack()

	varTk_indice = tkinter.StringVar()
	varTk_indice.set("indice : {}".format(motMystereMelange))
	tk_label_indice = tkinter.Label(mainFrame, textvariable=varTk_indice)
	tk_label_indice.pack()


	var_tk_text = tkinter.StringVar()
	tk_text = tkinter.Entry(mainFrame,textvariable=var_tk_text)
	tk_text.pack()



	varTk_verif = tkinter.StringVar()
	tk_label_verif = tkinter.Label(mainFrame, textvariable=varTk_verif)
	tk_label_verif.pack()


	tk_btn_valid = tkinter.Button(mainFrame,width=4,height=1,text="check",command=testValid)
	tk_btn_valid.pack()
	new_game.mainloop()

	




 #RETIENS 8 -> pour mymy 
macron nous as dit deux gros mois 









