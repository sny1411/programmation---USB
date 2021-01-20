#coding:utf-8

from class_Andfonction import Joueur
import class_Andfonction

JoueurOne = Joueur(str(input("Joueur 1: entre ton pseudo stp -> ")))
JoueurTwo = Joueur(str(input("Joueur 2: entre ton pseudo stp -> ")))

nbAttaque = 1



while JoueurOne.vie > 0 or JoueurTwo.vie > 0:
	print("---------- attaque n°{} ! ----------\n".format(nbAttaque))
	print("{} (Joueur 1)s'apprête à attaquer !".format(JoueurOne.prenom))
	JoueurOne.attaquer(JoueurTwo)
	print("{} (Joueur 2)s'apprête à attaquer !".format(JoueurTwo.prenom))
	JoueurTwo.attaquer(JoueurOne)
	print("---------- actualisation des stats ----------")
	print("{} à {} points de vie".format(JoueurOne.prenom,JoueurOne.vie))
	print("{} à {} points de vie\n".format(JoueurTwo.prenom,JoueurTwo.vie))
	nbAttaque += 1

print("---------- Résultat ----------")
if JoueurOne.vie > JoueurTwo.vie:
	print("c'est {} qui à gagné !".format(JoueurOne.prenom))
elif JoueurTwo.vie > JoueurOne.vie:
	print("c'est {} qui à gagné !".format(JoueurTwo.prenom))
else:
	print("égalité !")
