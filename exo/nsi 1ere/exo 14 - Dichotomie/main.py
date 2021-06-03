#coding:utf-8
import time
tableaux = [3,4,7,15,15,20,30,44]


def cherche1(tab,elt):
    mIntervalle = 0
    interMin = 0
    interMax = len(tab)
    mIntervalle = (mIntervalle + interMax) // 2
    print(mIntervalle)
    while True:
        if tab[mIntervalle] == elt:
            print("recherche terminee, indice : ", mIntervalle)
            break
        elif tab[mIntervalle] < elt:
            interMin = mIntervalle
            mIntervalle = (mIntervalle + interMax) // 2
            print(mIntervalle , " ", interMin, " ", interMax)
            print("decale à droite")
        elif mIntervalle == 0 or mIntervalle > len(tab):
            print("l'element chercher ne se trouve pas dans la liste")
            break
        else:
            interMax = mIntervalle
            mIntervalle = (interMin + mIntervalle) // 2
            print(mIntervalle , " ", interMin, " ", interMax)
            print("decale à gauche")
        time.sleep(2)
cherche1(tableaux,44)

def cherche(tab,elt):
    mIntervalle = 0
    interMin = 0
    interMax = len(tab)
    mIntervalle = (mIntervalle + interMax) // 2
    while True:
        if tab[mIntervalle] == elt:
            print("recherche terminee, indice : ", mIntervalle)
            break
        elif tab[mIntervalle] < elt:
            interMin = mIntervalle
            mIntervalle = (mIntervalle + interMax) // 2
        elif mIntervalle == 0 or mIntervalle > len(tab):
            print("l'element chercher ne se trouve pas dans la liste")
            break
        else:
            interMax = mIntervalle
            mIntervalle = (interMin + mIntervalle) // 2

cherche(tableaux,20)


