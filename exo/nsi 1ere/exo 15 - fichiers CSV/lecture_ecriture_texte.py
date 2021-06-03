#coding:utf-8

fichier = open("ma_table.csv","r",encoding="utf-8")
ma_table = fichier.readlines()
fichier.close()

print(ma_table)

ma_table = [ligne[:-1] for ligne in ma_table]
print(ma_table)

ma_table = [ligne.split(",") for ligne in ma_table]
print(ma_table)

print(ma_table[2])
print(ma_table[2][1])

descripteurs = ma_table[0]
print(descripteurs)

objets = ma_table[1:]
print(objets)

#fichier2 = open("ma_table.csv","a",encoding="utf-8")
#fichier2.write("M,JACKIE,1900\n")
#fichier2.write("M,Michelle,1950\n")
#fichier2.close()

import csv

fichier3 = open("ma_table.csv","r", encoding="utf-8")
ma_table = csv.reader(fichier3,delimiter=",")

for objets in ma_table:
    print(objets[2])

fichier3.close()

fichier4 = open("ma_table.csv","a",newline='',encoding="utf-8")
ma_table = csv.writer(fichier4,delimiter=",")

#ma_table.writerow(["F","Meissa","2004"])
#ma_table.writerow(["M","SNY","2004"])
ma_table.writerow(["M","SNYSNY","2004"])
fichier4.close()