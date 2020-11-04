#coding:utf-8

import time
nomTerminal = "Défaut"
while True:
	saisie = str(input("[{}]> ".format(nomTerminal)))

	if saisie == "help":
		print("\t-run (affiche 5 fois un point avec une pause entre chaque affichage de 1 s)")
		print("\t-name (renome le nom du terminal)")
		print("\t-help (affiche la liste des commandes)")
		print("\t-quit (termine l'execution du programme)")
		print("\t-Dieu (annonce qui est Dieu)")
	elif saisie == "run":
		i = 0
		for i in range(5):
			print("*")
			time.sleep(1)
	elif saisie == "name":
		nomTerminal = str(input("entre le nouveau nom que tu veut pour ton terminal -> "))
	elif saisie == "quit":
		break
	elif saisie == "Dieu":
		print("MAIS !")
		print("c'est sny bien sur haha :)")
		print("de quoi ? gogolatulipe ?")
		print("JAMAIS entendu parler x)")
	else:
		print("Commande inconnu -> entre une commande connue ou <help> pour connaitre la liste des commandes")
print("FIN DU PROGRAMME")
print("-----------------------")
print("AU REVOIR..")