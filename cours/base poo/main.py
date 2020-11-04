#coding:utf-8

class Humain:
	"""
	classe etre humain
	"""
	lieu_habitation = "TERRE"
	humain_crees = 0

	def __init__(self, Cprenom, Cage):
		print("crétion d'un humain")
		self.prenom = Cprenom
		self.age = Cage
		Humain.humain_crees += 1

	def parler(self,message): #self = méthode standard
		print("{} : {}".format(self.prenom, message))

	def changerPlanete(cls, nouvellePlanete): #cls = méthode de classe
		Humain.lieu_habitation = nouvellePlanete

	changerPlanete = classmethod(changerPlanete)

	def definition():
		print("c'est un HUMAIN")

	definition = staticmethod(definition)

print("lancement du prog")

h1 = Humain("JOJO", 34)
print("prénom de h1 -> {}".format(h1.prenom))
print(Humain.humain_crees)
Humain.changerPlanete("Mars")
print(Humain.lieu_habitation)
Humain.definition()