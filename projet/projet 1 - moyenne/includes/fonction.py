#coding:utf-8
from os import system

def get_moyenne(listeValeur):
	nbreValeur = len(listeValeur)
	valeurAdd = 0
	i = 0
	while i < nbreValeur:
		valeurAdd += float(listeValeur[i])
		i += 1
	try:
		result = valeurAdd / nbreValeur
		print(f"La moyenne est égal à -> {result}")
	except ZeroDivisionError:
		print("il faut entrer des valeurs pour pouvoir calculer la une moyenne :)")
		system("pause")


def ajoute_valeur(listeValeur):
	error = True
	while error:
		try:
			new_valeur = float(input("entre la valeur que tu veut rajouter: "))
		except ValueError:
			print("il faut entrer un nombre !")
			
		else:
			listeValeur.append(new_valeur)
			error = False

def supprime_valeur(listeValeur):
	pass


def get_liste_valeur(listeValeur):
	values = " "
	i = 0
	while i < len(listeValeur):
		values += str(listeValeur[i]) + ", "
		i += 1
	return values

def get_entier():
	entier = 0
	boucle = True
	while boucle:
		try:
			entier = int(input("entre ton choix (chiffres) -> "))
		except ValueError:
			print("il faut entrer une nombre !")
			continue
		else:
			return entier
			boucle = False


