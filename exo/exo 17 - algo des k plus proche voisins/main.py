#coding:utf-8

def distance(x,y):
    """cette fonction calcule la distance entre deux nbre reels
    param: a et b sont deux float
    return: float
    >>> distance(2,5)
    3"""
    return(abs(x - y))


def prochesVoisins(liste,x,k):
    """ cette fonction détermine la liste des k éléments les plus proches de x
    param liste: liste des éléments à trier
    param x: float point dont on cherche les k plus proches voisisns
    param k: int nombre de voisins à déterminer
    return: liste
    CU: k doit être plus petit que la longueur de la liste
    >>> prochesVoisins(L,3.0,3)
    [3.7, 2.0, 1.0]
    >>> prochesVoisins(L,3.0,5)
    [3.7, 2.0, 1.0, 5.0, 0.5]"""
    distanceVoisins = []
    for distAxe in liste:
        distanceVoisins.append([distance(x,distAxe), distAxe])
    distanceVoisins = sorted(distanceVoisins, key=lambda tup: tup[0],reverse=False)
    listePlusProche = []
    for i in range(len(distanceVoisins)):
        listePlusProche.append(distanceVoisins[i][1])
    return listePlusProche[:k]

L= [0.5,1.0,2.0,3.7,5.0,6.0,7.0]

Classes=['T','C','C','T','T','C','C']

def prochesIndices(liste1,liste2):
    """cette fonction donne la liste des indices des éléments de la liste1 dans
    la liste2
    param : 2 listes
    return: liste d'entiers
    CU: les éléments de la liste1 sont aussi dans la liste2
    >>> prochesIndices(prochesVoisins(L,3.0,3),L)
    [3, 2, 1]
    >>> prochesIndices(prochesVoisins(L,3.0,5),L)
    [3, 2, 1, 4, 0]"""
    lProcheVoisins = []
    for i in range(len(liste1)):
        for k in range(len(liste2)):
            if liste2[k] == liste1[i]:
                lProcheVoisins.append(k)
    return lProcheVoisins
        

#print(prochesIndices(prochesVoisins(L,3.0,3),L))
#print(prochesIndices(prochesVoisins(L,3.0,5),L))

def predireClasse(liste,classe,x,k):
    """Cette fonction prédit la classe de l'élément d'abscisse x en fonction des
    k plus proches voisins
    param liste: liste des abscisses
    param classe: liste des classes
    param x: float: abscisse de l'élément dont on veut déterminer la classe
    param k: int: nb de voisins que l'on utilise
    return: str: classe prédite
    >>> predireClasse(L,Classes,3.0,3)
    'C'
    >>> predireClasse(L,Classes,3.0,5)
    'T'"""
    lProcheVoisins = prochesVoisins(liste,x,k)
    lProcheIndices = prochesIndices(lProcheVoisins,liste)
    classeUtilise = []
    for i in range(len(lProcheIndices)):
        classeUtilise.append(classe[lProcheIndices[i]])
    maxCount = 0
    maxClasse = None
    for classe in classeUtilise:
        if classe != maxClasse:
            count = 0
            for i in range(len(classeUtilise)): 
                if classeUtilise[i] == classe:
                    count += 1
            if count > maxCount:
                maxCount = count
                maxClasse = classe
    return maxClasse

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,verbose=True)
