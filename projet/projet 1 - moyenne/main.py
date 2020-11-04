#coding:utf-8
from os import system # -> permet d'importer la fonction system de la classe os -> (j'ai besoin que de cette fonction , ce qui explique cette façon d'importer)
import includes.fonction as fonction # -> importe le fichier nommée "fonction"



prog_lancer = True
listeValeur = [] #initialisation d'une liste 



#---------------------------------------------------
msg_debut = "programme calcul moyenne"
print(msg_debut.center(50 , "-"))
#---------------------------------------------------


while prog_lancer:
	# ---------- affiche les choix possible ----------
	print("1 - ajouter une valeur")
	print("2 - supprimer une valeur")
	print("3 - calculer moyenne")
	print("4 - quitter le programme")

	choix_menue = fonction.get_entier() # demande de faire un choix et le stock dans la vrb choix_menue
	system("cls") #fait la commande systeme cls (clear la console) -> attention ! fonctionne que sur windows ! 
	#(amelioration possible : trouver un moyen de rendre la chose multi-plateforme)
	print("liste valeur : ",fonction.get_liste_valeur(listeValeur)) #affiche la liste des valeur grace à la fonction get_liste_valeur() qui retourne la liste des valeur dans un format que je prefere x)


	if choix_menue == 1: # si choix_menue est égal à 1 -> correspond au nbre pour ajouter une valeur
		fonction.ajoute_valeur(listeValeur)

	elif choix_menue == 2: #si choix_menue est égal à 2 -> correspond au nbre pour supprimer une valeur
		try:
			listeValeur.remove(listeValeur[-1])
		except IndexError:
			print("Erreur ! on ne peut pas supprimer une valuer si il n'y en a pas !")
			system("pause") # sa aussi sa fonctionne que sur windows :(


	elif choix_menue == 3: #si choix_menue est égal à 3 -> lance fonction calcule moyenne
		
		
		fonction.get_moyenne(listeValeur)
		print("1 - nouvelle moyenne")
		print("2 - modifier les valeurs actuelle")
		print("3 - quitter le programme")
		boucle_erreur = True
		while boucle_erreur:
			choix_menue = fonction.get_entier()
			if choix_menue == 1:
				boucle_erreur = False
				listeValeur.clear()
			elif choix_menue == 2:
				boucle_erreur = False
			elif choix_menue == 3:
				prog_lancer = False
				boucle_erreur = False
			else:
				print("entre une valeur valide !")
				boucle_erreur = True
				


	elif choix_menue == 4: # si choix_menue est égal à 4 -> quitte le prog
		prog_lancer = False



	system("cls")
	print("liste valeur : ",fonction.get_liste_valeur(listeValeur))




print("Fin du programme..\n\
Au revoir..") # -> optimisation -> un seul appel de print :)