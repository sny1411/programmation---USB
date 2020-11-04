#coding:utf-8

import random
import time
import os

class Joueur:


	def __init__(self, prenom):
		barreCharche()
		print("\njoueur créés avec succés")
		time.sleep(3)
		self.prenom = prenom
		self.vie = 250
		os.system("cls")

	def stats(self):
		print("le joueur {} à actuellement {} points de vie".format(self.prenom,self.vie))

	def attaquer(self,Joueur):
		degats = degatsRandom()
		print("{} à donc subit {} points de dégats\n".format(Joueur.prenom,degats))
		Joueur.vie -= degats




def degatsRandom():
		randomAttack = random.randint(0,1)
		randomAttack = bool(randomAttack)
		if randomAttack == True:
			print("attaque réussite !")
			randomDamage = random.randint(0,100)
			return randomDamage
		else:
			print("attaque raté !")
			return 0

def barreCharche():
	i = 0
	
	while i <= 100:
		os.system("cls")
		print("chargement : {} %".format(i))
		time.sleep(0.001)
		i += 1
	