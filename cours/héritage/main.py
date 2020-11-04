#coding:utf-8

class Vehicule: #classe maman

	def __init__(self, nom , quantite_essence):
		self.nom = nom
		self.essence = quantite_essence

	def seDeplacer():
		print("Le Vehicule {} se deplace".format(self.nom))

class Voiture(Vehicule): #classe fille
	def __init__(self,nom_voiture, essence,puissance):
		Vehicule.__init__(self, nom_voiture,essence)
		self.puissance = puissance

	def seDeplacer():
		print("Je roule !")

class Avion(Vehicule): #classe fille 2
	def __init__(self, nom , essence , marchandise):
		Vehicule.__init__(self, nom , essence)
		self.marchandise = marchandise

	def seDeplacer():
		print("Je vole dans les airs !")

#prog principal

voiture1 = Voiture("fiat multiplat", 2 , 4000)
print(f"puissance de {voiture1.puissance} Cheveaux !")
print(f"c'est une {voiture1.nom}")
Avion1 = Avion("F22 raptor", 500 , "Missiles")

print(f"{Avion1.nom} transporte des {Avion1.marchandise}")

print(isinstance(voiture1, Vehicule))

#isinstance -> verifie qu'un objet est de la classe renseignée

#issubclass(<classe_fille> , <classe_reseignée>): verifie si une classe est fille
#d'une autre