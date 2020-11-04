#coding:utf-8
import pickle
"""
mode d'ouverture : r (lecture seule)
				   w (ecriture avec remplacement)
				   a (ecriture avec ajout en fin de fichier)
				   x (lecture et ecriture)
				   r+ (lecture/ecriture dans un meme fichier)
"""

fic = open("donnees.txt", "r")


print(fic.read()) # lit tout
print(fic.readline()) #lit une ligne
print(fic.readlines())  #recupere les lignes restante -> sous forme tableau


fic.close()

if fic.closed:
	print("fichier fermé")
else:
	print("fichier ecore ouvert")


with open("donnees.txt","r") as fic2: #autre façon d'ouvrir des fichier
	content = fic2.read() # C'EST MIEUX :)
	print(content)

with open("test.txt","w") as test:
	nbre = 15
	test.write(str(nbre)) 
	test.write("\ncoucou, je suis une phrase !") # pour ecrire


class Player:
	def __init__(self, name , level):
		self.name = name
		self.level = level
	def whoami(self):
		print("{} ({})".format(self.name,self.level))

p1 = Player("sny",10)

p1.whoami()
with open("player.data", "wb") as file:
	record = pickle.Pickler(file)
	record.dump(p1)

with open("player.data", "rb") as testOuverture:
	getRecord = pickle.Unpickler(testOuverture)
	playerOne = getRecord.load()

playerOne.whoami()




