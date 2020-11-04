#coding:utf-8
import time
import includes.fonctions as fonctions
from os import system

motMystere = " "

def chercher(motMystere,melange):
	boucle_cherche = True
	while boucle_cherche:
		print("indice -> ",melange)
		reponse = str(input("trouve le mot mystere -> "))
		if reponse == motMystere:
			print("bravo ! le mot mystere etait donc -> ",motMystere)
			boucle_cherche = False
		elif reponse == "cheat()":
			print("CHEATER ! la reponse etait: ",motMystere)
			boucle_cherche = False
		else:
			print("faux ! desole, recommence !")
			continue



print("menue".center(50, "-"))

print("1 - jouer seul")
print("2 - jouer à deux")

choix_menue = fonctions.get_entier()

if choix_menue == 1: #choix 1 - jouer seul
	motMystere = str(fonctions.get_motInDico())
	melange = fonctions.melanger_str(motMystere)
	chercher(motMystere,melange)

elif choix_menue == 2: #choix 2 - jouer à deux
	motMystere = str(input("joueur 1 : entre le mot mystere -> "))
	print("le mot mystere est donc -> ",motMystere)
	time.sleep(3)
	system("cls")
	melange = fonctions.melanger_str(motMystere)
	chercher(motMystere,melange)

else:
	print("entre un chiffre qui correspond avec un choix du menue stp !")

