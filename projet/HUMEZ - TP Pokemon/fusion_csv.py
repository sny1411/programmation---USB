#coding:utf-8

### --- PARTIE 5 ---

# QUESTION 1
import csv

fichier1 = open("pokemon_stats_2_a.csv","r",newline='',encoding='utf-8')
objets_pokemon_2_a = csv.reader(fichier1,delimiter=';')
objets_pokemon_2_a = [ligne for ligne in objets_pokemon_2_a]
fichier1.close()
fichier2 = open("pokemon_stats_2_b.csv","r",newline='',encoding='utf-8')
objets_pokemon_2_b = csv.reader(fichier2,delimiter=';')
objets_pokemon_2_b = [ligne for ligne in objets_pokemon_2_b]
fichier2.close()
# QUESTION 2

descripteurs_pokemon_2_a = objets_pokemon_2_a[0]
descripteurs_pokemon_2_b = objets_pokemon_2_b[0]

objets_pokemon_2_a = objets_pokemon_2_a[1:]
objets_pokemon_2_b = objets_pokemon_2_b[1:]

# QUESTION 3 - 4
if descripteurs_pokemon_2_a == descripteurs_pokemon_2_b: #ils sont egaux ^^
    print("les descripteurs des deux tables sont egaux et sont dans le meme ordre")
else:
    print("les descripteurs ne sont pas egaux")

# QUESTION 5

#pour concatener deux listes d'objets , ont peut utiliser la fonction append()

objets_pokemon_2 = objets_pokemon_2_a.copy()
objets_pokemon_2.extend(objets_pokemon_2_b)
print(objets_pokemon_2)
# QUESTION 6

print(len(objets_pokemon_2)) # il y a 537 objets dans objets_pokemon_2
print(len(objets_pokemon_2_a)+ len(objets_pokemon_2_b)) # si ont fait l'addition de la longeur de objets pokemon a et b, on trouve le meme nombre
#donc les longeurs des deux listes correspondent

# QUESTION 7 - 8

doublons = False
i = 0
while doublons != True and i < len(objets_pokemon_2):
    for j in range(i+1,len(objets_pokemon_2)):
        if objets_pokemon_2[j] == objets_pokemon_2[i]:
            print(objets_pokemon_2[i]) # le nom du premier pokemon en double est Spheal
            print(j," ",i)
            doublons = True
    i+=1
print(doublons)

# QUESTION 9

objets_pokemon_2_sans_doublons = []
for objets in objets_pokemon_2:
    if not objets in objets_pokemon_2_sans_doublons:
        objets_pokemon_2_sans_doublons.append(objets)

print(len(objets_pokemon_2_sans_doublons))

# QUESTION 10

fichier = open("pokemon_stats_2.csv","a",newline='',encoding='utf-8')
ma_table =csv.writer(fichier,delimiter=';')
ma_table.writerow(descripteurs_pokemon_2_a)
ma_table.writerows(objets_pokemon_2_sans_doublons)
fichier.close()

# --- PARTIE 6 ---

# QUESTION 1





