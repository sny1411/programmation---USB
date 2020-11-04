#coding:utf-8

"""
pour calculer on utilise les signe : + -> addition
									 - -> soustraction
									 * -> multiplication
									 / -> division
									 % -> modulo (correstion au reste d'une division euclidienne)

On peut utiliser toute ces operateur avec des nombre, et les nombre stocker dans des variables
"""		

nbre = float(input("entre un nbre stp : "))
diviseur = float(input("entre un diviseur stp : "))

resultat = nbre / diviseur

reste = nbre % diviseur

print("le resultat de la division est {} , et le reste est {}".format(int(resultat),reste))
