#coding:utf-8

l = ["ruby","python","logo","elan","rust"]
nbre = ["a","q","c","b","d","i"]

def index_min(liste,index=0):
    """renvoie l'index du plus petit elt de la liste à l'indice index
    param liste (list) : liste que l'on veut trier
    param index (int) : indice à partir duquel on veut trouver le plus petit elt
    sortie: int : correspond à l'index de l'elt le plus petit"""
    min = index
    for i in range(index,len(liste)):
        if liste[min] > liste[i]:
            min = i
    return min

print(index_min(l,0))

def swap(liste, indexUn,indexDeux):
    """echange une valeur avec une autre dans une liste
    param liste(list): liste dans laquel on va echanger des valeurs
    param indexUn(int): index du premier element à echanger
    param indexDeux(int): index du deuxieme element à echanger
    sortie: list : la liste apres echange"""
    saveUn = liste[indexUn]
    liste[indexUn] = liste[indexDeux]
    liste[indexDeux] = saveUn
    return liste

#print(swap(l, 3,1))

def ssort(liste):
    """trie une liste
    param liste(list): liste que l'on veut trier
    sortie: list : la liste triée"""
    for i in range(len(liste) - 1):
        min = index_min(liste,i)
        swap(liste,i,min)
    return liste

print(ssort(l))

def inserer(liste,item): 
    place = len(liste)-1  #indice de parcours placé à la fin
    liste.append(item)    #on colle item à la fin
    while item==0:
        liste[place], liste[place + 1] = liste[place + 1], liste[place]
        place = place-1

def trierParInsertion(liste):
    listeTriee = []
    for item in liste:
        inserer(listeTriee,item)
    return listeTriee
#JARRIVE PAAAAAS


