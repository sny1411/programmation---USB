#coding:utf-8

import random
import time
import os

class Joueur:


	def __init__(self, prenom):
		barreCharche()
		print("\njoueur créé avec succés")
		time.sleep(3)
		self.prenom = prenom
		self.vie = 250
		os.system("cls")

	def stats(self):
		print("le joueur {} a actuellement {} points de vie".format(self.prenom,self.vie))

	def attaquer(self,Joueur):
		degats = degatsRandom()
		print("{} a donc subi {} points de dégats\n".format(Joueur.prenom,degats))
		Joueur.vie -= degats




def degatsRandom():
		randomAttack = random.randint(0,1)
		randomAttack = bool(randomAttack)
		if randomAttack == True:
			print("attaque réussite !")
			randomDamage = random.randint(0,100)
			return randomDamage
		else:
			print("attaque ratée !")
			return 0

def barreCharche():
	os.system("cls")