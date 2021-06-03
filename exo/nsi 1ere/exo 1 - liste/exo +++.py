#coding:utf-8

def liste(n):
    liste = []
    for i in range(1,n+1):
        liste.append(i)
        liste.extend([1 for x in range(i)])
    return liste

print(liste(5))