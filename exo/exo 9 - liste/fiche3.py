#coding:utf-8

#exemple 3 (2)
villes = ["Bordeaux","Paris"]
towns = villes.copy()
towns.append("Lille")
print(villes)
print(towns)

#exercice 2:

def pairs_impairs(liste):
    """renvoie deux liste : les nombre impair et nbre pair de la liste donné
    entrée : list de type list (avec des int)
    sortie : tuple de list"""
    pairs = []
    impairs = []
    for nbre in liste:
        if nbre % 2 == 0:
            pairs.append(nbre)
        else:
            impairs.append(nbre)
    return pairs, impairs

listeInt = [10,2,3,7,16]

print(pairs_impairs(listeInt))

#exercice 3:

# 1)

def multiples1(n):
    for i in range(10):
        