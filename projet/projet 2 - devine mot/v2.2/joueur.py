class Joueur(object):
	"""docstring for Joueur"""
	def __init__(self):
		self.score = 0
		#d'autres choses prévu ici ... :)
		print(f"Joueur creé avec un score à {self.score}")

	def getScore(self):
		return self.score

	def setScore(self, newScore):
		self.score = newScore
		print(f"score set to {self.score}")