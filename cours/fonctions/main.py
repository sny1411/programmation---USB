#coding:utf-8


def direBonjour():
    print("hello!")


#direBonjour()

def boucleNfois(n = 5):
    for i in range(n):
        print(i," - salut !")

#boucleNfois()
#boucleNfois(10)

from random import randint

def GetNbreAlea(nbreMin = 0,nbreMax = 100) -> int: # le "-> int" est une nouveauté de la 3.9
    return randint(nbreMin,nbreMax)


#print(GetNbreAlea(10,20))

