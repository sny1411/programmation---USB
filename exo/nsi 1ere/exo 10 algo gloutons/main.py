#coding:utf-8
import operator

def renduMonnais(somme):
    listePiece = [1,2,5,10,20,50,100,200]
    n = len(listePiece)
    somme *= 100
    rendu = [0] * n
    for i in range(n - 1,0,-1):
        while listePiece[i] <= somme:
            rendu[i] += 1
            somme -= listePiece[i]
    return rendu

#print(renduMonnais(4.5))

objets = [["A",12,700],["B",13,400],["C",8,300],["D",10,300]]
for i in range(len(objets)):
    objets[i].append(objets[i][2] // objets[i][1])


def poidsSac(obj,max):
    sac = []
    benefice = 0
    obj = sorted(obj,key=operator.itemgetter(3), reverse=True)
    print(obj)
    poids = 0
    for i in range(len(obj)):
        if (poids + obj[i][1])<= max:
            sac.append(obj[i][0])
            poids += obj[i][1]
            benefice += obj[i][2]
    return sac,benefice,poids
#print(poidsSac(objets,30))

stationsDistance = [0,50,100,20,30,40,60,70]

def stations(lDistances,distanceMax):
    stationsUtilise = []
    km = 0
    for i in range(len(lDistances) - 1):
        if km + lDistances[i + 1] >= distanceMax:
            print("fuel stock - ", km+lDistances[i])
            stationsUtilise.append(i - 1)
            print(km," ", i)
            km = 0
        else:
            print(lDistances[i], " - ajout ", i)
            km += lDistances[i]
            print(km," ", i)
    return stationsUtilise
print(stations(stationsDistance,100))
