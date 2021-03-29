#coding:utf-8

# --- PARTIE 1 ---

import csv


fichier = open("pokemon_stats_1.csv",'r',newline='',encoding='utf-8')
table_pokemon_1 = csv.reader(fichier,delimiter=';')
table_pokemon_1 = [ligne for ligne in table_pokemon_1]
fichier.close()

#print(table_pokemon_1)

### QUESTION 3

#cette collection correspond aux statistique d'une liste de pokemon, les descripteurs sont :
# - name
# - classification
# - attack
# - defense

### QUESTION 4

descripteurs_pokemon_1 = table_pokemon_1[0]
objets_pokemon_1 = table_pokemon_1[1:]

#print(descripteurs_pokemon_1)
#print(objets_pokemon_1)

### QUESTION 5

#il y a 507 objets dans la collection, j'ai obtenu cette valeur grace à :

#print(len(objets_pokemon_1))


# --- PARTIE 2 ---

### QUESTION 1

#print("nom :",objets_pokemon_1[340][0], " | attaque : " ,objets_pokemon_1[340][2])

### QUESTION 2

indice_objets = [i for i in range(len(objets_pokemon_1)) if objets_pokemon_1[i][0] == 'Toxicroak']
#print(indice_objets)
# -> 426

### QUESTION 3

# la boucle va de 0 jusqu'au nombre d'element qu'il y a dans les objets pokemon et à chaque tour il verifie si le nom du pokemon correspond à "Toxicroak" si c'est le cas, il ajoute
# l'index i à la liste

### QUESTION 4

#print(objets_pokemon_1[426])
# 426 est bien l'index du pokemon "Toxicroak"

### QUESTION 5

indice_objets2 = [i for i in range(len(objets_pokemon_1)) if objets_pokemon_1[i][0] == 'Lairon']
#print(indice_objets2)
# -> 218

#print(objets_pokemon_1[218])
# 218 est bien l'index du pokemon "Lairon"

#j'ai reutiliser la boucle de la question d'avant en modifiant le string dans la comparaison du if

### QUESTION 6

indice_objets2 = [i for i in range(len(objets_pokemon_1)) if objets_pokemon_1[i][1] == 'Dragon Pokémon']
#print(indice_objets2)


#au lien de regarder l'index [i][0] des objets pokemon qui correspond à regarder les noms des pokemons
# j'ai mis [i][1] qui correspond à la classification des pokemon

#print(objets_pokemon_1[183])
#print(objets_pokemon_1[243])
#print(objets_pokemon_1[300])
#print(objets_pokemon_1[484])
# -> ces pokemon sont bien classés Dragon Pokemon

### QUESTION 7

indices_objets = [12,74,123,253,388]
liste_objets = [objets_pokemon_1[i] for i in range(len(objets_pokemon_1)) if i in indices_objets]

#print(liste_objets)

### QUESTION 8

liste_objets2 = [objets_pokemon_1[i] for i in range(len(objets_pokemon_1)) if int(objets_pokemon_1[i][2]) >= 70]

#print(liste_objets2)
#print(len(liste_objets2))
# # -> il y en a 284

### QUESTION 9

liste_objets3 = [objets_pokemon_1[i][2] for i in range(len(objets_pokemon_1)) if int(objets_pokemon_1[i][2]) > 100 and int(objets_pokemon_1[i][3]) > 100 ]

#print(liste_objets3)
#print(len(liste_objets3))

# --- PARTIE 3 ---

### QUESTION 1

attaque_pokemon = [objets_pokemon_1[i][2] for i in range(len(objets_pokemon_1))]
moyenne_attaque = 0
for attaque in attaque_pokemon:
    moyenne_attaque += int(attaque)


moyenne_attaque =  moyenne_attaque/ len(objets_pokemon_1)

#print(moyenne_attaque)
# -> 77.17948717948718 , donc à peu près 77.18


### QUESTION 2
defense_pokemon = [objets_pokemon_1[i][3] for i in range(len(objets_pokemon_1))]
moyenne_defense = 0
for defense in defense_pokemon:
    moyenne_defense += int(defense)


moyenne_defense =  moyenne_defense/ len(objets_pokemon_1)

#print(moyenne_defense)

### QUESTION 3

index_max = 0
valeur_max = int(objets_pokemon_1[0][2])
#print(valeur_max)

for i in range(1,len(objets_pokemon_1)):
    if int(objets_pokemon_1[i][2]) > valeur_max:
        index_max = i
        valeur_max = int(objets_pokemon_1[i][2])
#print(index_max, " ", valeur_max)
# -> index_max = 41 , valeur_max = 185

#print(objets_pokemon_1[41][0])
#son nom est : Heracross

### QUESTION 4

index_min = 0
valeur_min = int(objets_pokemon_1[0][2])

for i in range(1,len(objets_pokemon_1)):
    if int(objets_pokemon_1[i][2]) < valeur_min:
        index_min = i
        valeur_min = int(objets_pokemon_1[i][2])

#print(index_min," ", valeur_min)
# -> index_min = 103 , valeur_min = 5

#print(objets_pokemon_1[103][0])
#son nom est : Happiny

### QUESTION 5

index_max = 0
valeur_max = int(objets_pokemon_1[0][3])

for i in range(1,len(objets_pokemon_1)):
    if int(objets_pokemon_1[i][3]) > valeur_max:
        index_max = i
        valeur_max = int(objets_pokemon_1[i][3])
#print(index_max, " ", valeur_max)
 # -> defense -> index_max :17 , valeur_max: 230

# --------

index_min = 0
valeur_min = int(objets_pokemon_1[0][3])

for i in range(1,len(objets_pokemon_1)):
    if int(objets_pokemon_1[i][3]) < valeur_min:
        index_min = i
        valeur_min = int(objets_pokemon_1[i][3])

#print(index_min," ", valeur_min)
# -> defense -> index_min : 103 , valeur_min : 5

### QUESTION 6
index_max = 0
moyenne_max =  (int(objets_pokemon_1[0][2]) + int(objets_pokemon_1[0][3])) / 2
for i in range(1,len(objets_pokemon_1)):
    moyenne_attaque_i = (int(objets_pokemon_1[i][2]) + int(objets_pokemon_1[i][3])) / 2
    if moyenne_attaque_i > moyenne_max:
        index_max = i
        moyenne_max = moyenne_attaque_i
#print(moyenne_max, " ", index_max)
#-> moyenne max : 185 , index : 17

#print(objets_pokemon_1[17][0])
# c'est Aggron qui a la plus grande moyenne attaque/defense
#pour obtenir ce resultat j'ai fait la moyenne de l'attaque et de la defense de chaque pokemon et si
#cette moyenne est meilleur que l'ancienne meilleur, la valeur est remplacé par la nouvelle

# --- PARTIE 4 ---

### QUESTION 1

liste_triee = sorted(objets_pokemon_1) # trie la liste dans l'ordre croissant par rapport au premier terme de chaque liste
#print(liste_triee)

### QUESTION 2

def fonction_cle_de_tri(liste):
    return int(liste[2])
liste_triee_attaque = sorted(objets_pokemon_1, key=fonction_cle_de_tri,reverse=True)
print(liste_triee_attaque[:3])

### QUESTION 3
def fonction_cle_de_tri2(liste):
    return int(liste[3])
liste_triee_defenseur = sorted(objets_pokemon_1,key=fonction_cle_de_tri2,reverse=True)
print(liste_triee_defenseur[:3])

### QUESTION 4

#Les elements qui revèlent d'une donnée sont les 3 meilleur defenseur.
#Et l'information les pokemons bons en attaque sont une information.

### QUESTION 5


liste_moyenne_attaque_defense = []
for i in range(1,len(objets_pokemon_1)):
    moyenne_attaque_i = (int(objets_pokemon_1[i][2]) + int(objets_pokemon_1[i][3])) / 2
    liste_moyenne_attaque_defense.append(list((moyenne_attaque_i,objets_pokemon_1[i][0])))

def fonction_cle_de_tri4(liste):
    return int(liste[0])
liste_moyenne_attaque_defense = sorted(liste_moyenne_attaque_defense,key=fonction_cle_de_tri4,reverse=True)
print(liste_moyenne_attaque_defense[:10]) # Aggron est le meilleur defenseur , steelix 2eme meilleur defenseur , groudon 3eme meilleur attaquant , Heracross 1ere attaquant et Kartana 2eme attaquant
#donc oui les pokemons qui ont la meilleur moyenne attaque defense, font parti des meilleurs attaquants ou des meilleurs defenseurs







