#coding:utf-8

#creation d'une liste
inventaire = ["arc" , "épée" , "bouclier"]
#arc = incdice 0 (premier elément)
for valeur in inventaire:
	print(valeur)


print(inventaire[1]) # affiche element 2
print(inventaire[:]) # affiche tout
print(inventaire[:2]) #affiche 2 premier
print(inventaire[2:]) #affiche 2 dernier -> avec des listes plus grande c'est mieux :(
print(inventaire[-1]) # affiche dernier element
print(inventaire[1:2]) # affiche element d'indice 1 à 2


inventaire[2] = "bouclier d'acier"
print(inventaire[:])

inventaire.append("test")
print(inventaire[:])

inventaire.insert(1, "popo de mana")
print(inventaire[:])

inventaire.remove("test")

del inventaire[1]
inventaire.sort() # range les valeurs
print(inventaire[:])

inventaire.reverse()
print(inventaire[:])

print("nbre arc : {} !".format(inventaire.count("arc")))

inventaire.clear()
print(inventaire[:])

phrase = ["bonjour", "à" , "tous"]

phrase = " ".join(phrase)
print(phrase)

import copy
listePlus = ["coucou"] * 5
liste1 = ["test"] * 5

liste2 = copy.deepcopy(liste1) #permet de bien copier des liste :)
liste2.extend(listePlus)

print(liste2[:])
print(liste1[:])
