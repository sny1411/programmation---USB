#coding:utf-8
import random
import pickle
import sys

def get_entier():
	entier = 0
	boucle = True
	while boucle:
		try:
			entier = int(input("entre ton choix (chiffres) -> "))
		except ValueError:
			print("il faut entrer un  nombre !")
			continue
		except KeyboardInterrupt:
			print("raccourcie clavier !")
			print("fin du programme..")
			sys.exit(0)
		else:
			return entier
			boucle = False

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
	with open("includes/dico.txt","r") as dico: #autre façon d'ouvrir des fichier
		listeDico = dico.readlines() # C'EST MIEUX :)
		nbre_ligne = len(listeDico)
		return listeDico[random.randint(0,nbre_ligne)].strip()



if __name__ == '__main__':
	get_motInDico()
