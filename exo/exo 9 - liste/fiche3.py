#coding:utf-8

#exemple 3 (2)
villes = ["Bordeaux","Paris"]
towns = villes.copy()
towns.append("Lille")
#print(villes)
#print(towns)


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

#print(pairs_impairs(listeInt))

#exercice 3:

# 1)

def multiples1(n):
    """renvoie la liste des 10 premier multiple de n
    entrée: n de type int
    sortie: list"""
    listeM = []
    if n < 0:
        pass
    else:
        for i in range(1,11):
            listeM.append(n*i)
        return listeM

#print(multiples1(5))

def multiples2(n):
    """renvoie la liste des multiple de n strictement inférieur à 1000
    entrée: n de type int
    sortie: list"""
    listeM = []
    if n < 0:
        pass
    else:
        i = 1
        while i * n < 1000:
            listeM.append(i * n)
            i += 1
        print(len(listeM))
        return listeM


#print(multiples2(6))


def diviseur(n):
    """renvoie la liste des diviseur de n
    entrée: n de type int
    sortie: list"""
    listeD = []
    if n < 0:
        pass
    else:
        for i in range(1,100):
            if n % i == 0:
                listeD.append(i)
        return listeD
#print(diviseur(70))

#exo 4:

#1:


def listConstruc1(n):
    listCreated = []
    i = 1
    while i - 1< n:
        listCreated.extend([1,i])
        i += 1
    return listCreated

#print(listConstruc1(10))
        
#2:

def listConstruc2(n):
    listCreated = []
    x = 0
    while x != n:
        x += 1
        for i in range(x):
            listCreated.append(i + 1)
        
    return listCreated

#print(listConstruc2(10))

#exercice 5:

def mystere(liste1,liste2):
    """ liste 1 et liste2 sont deux listes de nbre entiers rangés dans l'ordre croissant"""
    liste = []
    i,j = 0,0
    while i < len(liste1) and j < len(liste2):
        if liste1[i] < liste2[j]:
            liste.append(liste1[i])
            i += 1
        else:
            liste.append(liste2[j])
            j += 1
    return liste

#print(mystere([2,5,6,8],[1,4,7,8,9]))

#exercice 6:

def nomPrenom():
    nom_prenom = input("entrez vos nom et prénom séparés par un espace: ")
    nom = nom_prenom.split(" ")[0]
    prenom = nom_prenom.split(" ")[1]
    a = nom[0].upper()
    b = prenom[0].upper()
    print(a, ".",b)

nomPrenom()
        