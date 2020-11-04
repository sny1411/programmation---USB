#coding:utf-8

"""
-  <nom_variable> = <donne_variable>   -> déclarer une variable

-  méthode pour recuperer saisie utilisateur -> input("<str question>")

-  cast de variable -> int()
   				    -> float()
				    -> str()
				    -> long()

-  on peut formater du texte avec .format et {}
"""

age_personne = 18

nom_personne = str(input("comment t'appel-tu ? "))

print("vous vous appelez {} et vous avez  {} ans".format(nom_personne,age_personne))