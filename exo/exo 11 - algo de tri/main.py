#coding:utf-8

l = ["ruby","python","logo","elan","rust"]

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
    saveUn = liste[indexUn]
    liste[indexUn] = liste[indexDeux]
    liste[indexDeux] = saveUn
    return liste

#print(swap(l, 3,1))

def ssort(liste):
    """trie une liste
    param liste(list): liste que l'on veut trier
    sortie: list : la liste triée"""
    for i in range(len(liste)):
        min = index_min(liste,i)
        swap(liste,i,min)
    return liste

print(ssort(l))



