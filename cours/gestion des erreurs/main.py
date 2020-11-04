#coding:utf-8

"""
GERER EXECPTION : try/except (+ else, finally)
"""

try:
	age = int(input("Quel âge as-tu ?"))
except:
	print("L'age est pas bonne !")
else:
	print("Tu as {} ans".format(age))
finally:
	print("FIN DU PROGRAMME...")

nbre1 = 150
nbre2 = intput("choisir un diviseur")

try:
	nbre2 = int(nbre2)
	print("Résultat = {}".format(nbre1 / nbre2))
except ZeroDivisionError:
	print("VOUS NE POUVEZ PAS DIVISER PAR 0 !")
except ValueError:
	print("il faut entrer un nbre !")
except:
	print("valeur incorrecte !")
try:
	age = input("quel age as-tu ?")
	age = int(age)
	assert age > 25 #je veux que age soit plus grand que 25
except AssertionError:
	print("j'ai choppé l'exception !")
