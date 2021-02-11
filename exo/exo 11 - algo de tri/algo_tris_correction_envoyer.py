#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 18:11:55 2021

@author: arnaud
"""
####Tris par sélection ####

def index_min(liste,ind):
    s=ind
    for i in range(ind,len(liste)):
        if liste[i]<liste[s]:
            s=i
    return s

def swap(liste,i1,i2):
    liste[i1], liste[i2]=liste[i2],liste[i1]
    return liste

def ssort(liste):
    """ trie la liste par sélection
    parm: liste non triée
    return liste triée"""
    for i in range(len(liste)-1):
        j=index_min(liste,i)
        swap(liste,i,j)
    return liste


#### Tris par insertion####


def insert(liste, ind):
    """place l'elt d'indice ind d'une liste triée jusque ind-1
    param liste (list): liste triée jusque ind-1
    param ind (int): indice de l'let à mettre à sa place dans le début
    return: liste triée jusque ind
    >>> insert([1,2,4,3,7,2],3)
    [1, 2, 3, 4, 7, 2]
    >>> insert([1, 2, 3, 4, 7, 2],5)
    [1, 2, 2, 3, 4, 7]
    """
    i=ind
    elt=liste[ind]
    while liste[i-1]>elt and i>0:
        liste[i]=liste[i-1]
        i=i-1
    liste[i]=elt
    return liste


def isort(liste):
    """ trie la liste par insertion
    parm: liste non triée
    return liste triée"""
    for i in range(1,len(liste)):
        liste=insert(liste,i)
    return liste

#### Tris par bulles####

def bsort(liste):
    """ trie la liste par bulles
    parm: liste non triée
    return liste triée
    >>> bsort([7,4,9,5,1,3])
    [1, 3, 4, 5, 7, 9]"""
    for i in range(len(liste),1,-1):
        for j in range(i-1):
            if liste[j]>liste[j+1]:
                swap(liste,j,j+1)
    return liste




import doctest
#doctest.testmod()
#doctest.testmod(verbose=True)
doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=False)
