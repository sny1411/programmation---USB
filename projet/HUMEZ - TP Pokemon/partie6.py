#coding:utf-8

### QUESTION 2

#ils ont le nom et la classification en descripteur commun mais tous les autres sont differents

### QUESTION 3

#c'est le descripteur "name" qui permet d'identifier de maniere unique chaque pokemon

### QUESTION 4

#pour fusionner les deux tables, il faudra rajouter tout les descripteurs differents des deux tables sans les doublons
#puis fusionner chaque objets 1 par 1 en enlevant les doubons pour les rajouter à la nouvelle table


### QUESTION 5

import csv

fichier = open("pokemon_stats_1.csv",'r',newline='',encoding='utf-8')
table_pokemon_1 = csv.reader(fichier,delimiter=';')
table_pokemon_1 = [ligne for ligne in table_pokemon_1]
fichier.close()

fichier = open("pokemon_stats_2.csv",'r',newline='',encoding='utf-8')
table_pokemon_2 = csv.reader(fichier,delimiter=';')
table_pokemon_2 = [ligne for ligne in table_pokemon_2]
fichier.close()

# on fusionne la liste des objets des deux tables
objets_pokemon_3 = table_pokemon_1[1:].copy()
objets_pokemon_3.extend(table_pokemon_2[1:])

def fonction_cle_de_tri(liste):
    return liste[0]

objets_pokemon_3 = sorted(objets_pokemon_3,key=fonction_cle_de_tri) #puis on la range dans l'ordre alphabetique par rapport au noms du pokemon

descripteur3 = table_pokemon_1[0].copy()
descripteur3.extend(table_pokemon_2[0]) #on fusionne les descripteurs des deux tables

descripteurs3_sans_doublons = [] # ce sont les descipteurs que nous garderons pour la fin
for descripteur in descripteur3:
    if not descripteur in descripteurs3_sans_doublons:
        descripteurs3_sans_doublons.append(descripteur)

objets_pokemon_3_final = [] # c'est dans cette liste que nous allons mettre tout les pokemons que nous allons fusionner
while len(objets_pokemon_3) > 0: #le temps que la longueur de "objets_pokemon_3" est plus grande que 0
    indice_pokemon = [i for i in range(1,len(objets_pokemon_3)) if objets_pokemon_3[i][0] == objets_pokemon_3[0][0]] # on commence par chercher pour le pokemon d'indice 0
    # si il n'y a pas un autre pokemon du meme nom dans la table "objets_pokemon_3"
    if len(indice_pokemon) == 0: # si il n'y a pas de pokemon du meme nom
        objets_pokemon_3_final.append(objets_pokemon_3[0])
        objets_pokemon_3.pop(objets_pokemon_3) # on rajoute directement le pokemon d'indice 0 dans "objets_pokemon_3_final" puis on le retire de "objets_pokemon_3"
    elif len(indice_pokemon) == 1: # si il y a 1 autre pokemon avec le meme nom (c'est toujours le cas ici)
        pokemon = objets_pokemon_3[0].copy()
        pokemon.extend(objets_pokemon_3[indice_pokemon[0]]) # on fusionne les deux pokemon dans une liste intermediare
        pokemon.pop(8)# puis on retire l'indice 8 et 4 qui correspondent au nom et à la classification en double
        pokemon.pop(4)
        objets_pokemon_3_final.append(pokemon) # on rajoute cette liste à "objets_pokemon_3_final"
        objets_pokemon_3.pop(indice_pokemon[0]) # et on supprime les deux pokemon que l'on a utilisé
        objets_pokemon_3.pop(0)
    else:
        print("je sais pas faire si il y en a plus de deux pareil moi :(")




fichier = open("pokemon_stats_3.csv","a",newline='',encoding='utf-8')
ma_table =csv.writer(fichier,delimiter=';')
ma_table.writerow(descripteurs3_sans_doublons)
ma_table.writerows(objets_pokemon_3_final)

fichier.close()







