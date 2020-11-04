#coding:utf-8



class Humain:
	"""cette classe represente un HUMAIN """

	def __init__(self, nom, age):
		self.nom = nom
		self._age = age
	#property(<getter>, <setter> , <deleter>, <helper>)
	

	def _getage(self):
		try:
			return self._age
		except AttributeError:
			print("L'âge n'existe pas")

	def _setage(self,nouvel_age):
		if nouvel_age <= 0:
			self._age = 0
		else:
			self._age = nouvel_age

	def _delage(self):
		del self._age
	age = property(_getage, _setage, _delage, "Je suis l'age d'une Humain")


#programme principal
h1 = Humain("NONO", 8)
print(h1.age)

h1.age = 20

print(h1.age)
help(Humain)

print(f"coucou c'est {h1.nom}") # -> méthode f string
