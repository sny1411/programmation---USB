#coding:utf-8

"""
création dictionnaire: dico = {} #vide
					   dico = {<cle>:<valeur>,<cle2>:<valeur>}

accès a une valeur 	 : dico[<cle>]

ajout au dictionnaire: dico[<cle>] = <valeur>
suppression 		 : dico.pop(<cle>)
					 : del dico[<cle>]



"""

dico = {1:145,"prenom":"sny"}

print(dico["prenom"])

dico["test"] = "c'est une test"

print(dico)

del dico["prenom"]
print(dico)

if "chien" in dico:
	print("oui")
else:
	print("non")

for key in dico.values():
	print(key)

for k,v in dico.items():
	print("clé {} - valeur {}".format(k,v))

dico2 = dico.copy()

# nouveauté 3.9 :  merge dictionnaires (opérateur | )
dictA = {'a':'1','b':'2','c':'3'}
dictB = {'b':'1','c':'2','d':'3'}

print(dictA | dictB) # les deux dico on été mergé



