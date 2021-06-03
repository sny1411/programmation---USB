#coding:utf-8
import random

def creer_grille(horizontale,vertical):
    grille = []
    for i in range(vertical):
        grille.append(list(0 for i in range(horizontale)))
    return grille

def hauteur_grille(grille):
    return len(grille)

def largeur_grille(grille):
    return len(grille[0])

def creer_grille_aleatoire(horizontale,vertical,p):
    grille = []
    case = 0
    for i in range(vertical):
        grille_2 = []
        for y in range(horizontale):
            if random.random() > p:
                case = 0
            else:
                case = 1
            grille_2.append(case)
        grille.append(grille_2)
    return grille

def voisins_case(grille,x,y):
    case_voisine = []
    # ligne du dessus
    if y != 0:
        if x != 0:
            case_voisine.append(grille[y-1][x-1])
        case_voisine.append(grille[y-1][x])
        if x != largeur_grille(grille) - 1:
            case_voisine.append(grille[y-1][x+1])
    #à droite et à gauche
    if x != 0:
        case_voisine.append(grille[y][x-1])
    if x != largeur_grille(grille) - 1:
        case_voisine.append(grille[y][x+1])
    # ligne en dessous
    if y != hauteur_grille(grille) - 1:
        if x != 0:
            case_voisine.append(grille[y+1][x-1])
        case_voisine.append(grille[y+1][x])
        if x != largeur_grille(grille) - 1:
            case_voisine.append(grille[y+1][x+1])
    return case_voisine

def voisins_case_simplifier(grille,x,y):
    for hauteur in range(y-1,y+1):
        pass

def nb_cellules_voisins(grille,x,y):
    nb = 0
    for case in voisins_case(grille,x,y):
        if case == 1:
            nb += 1
    return nb

def afficher_grille(grille):
    
    for ligne in grille:
        ligne_transformer = ""
        for case in ligne:
            if case == 1:
                ligne_transformer += (" O ")
            else:
                ligne_transformer += (" _ ")
        print(ligne_transformer)

def generation_suivante(grille):
    grille_evol = []
    for y in range(hauteur_grille(grille)):
        ligne_evol = []
        for x in range(largeur_grille(grille)):
            nb_cell = nb_cellules_voisins(grille,x,y)
            if grille[y][x] == 1:
                if nb_cell == 2 or nb_cell == 3: # survie
                    ligne_evol.append(1)
                else: # meurt
                    ligne_evol.append(0)
            else:
                if nb_cell == 3: # naissance
                    ligne_evol.append(1)
                else:
                    ligne_evol.append(0)
        grille_evol.append(ligne_evol)
    return grille_evol

import time

def evolution_n_generations(grille,n):
    for i in range(n):
        print("------------------------------------------------")
        afficher_grille(grille)
        grille = generation_suivante(grille)
        time.sleep(1)


grilleTest = creer_grille_aleatoire(20,20,0.4)
evolution_n_generations(grilleTest,20)

oscillateur = [[0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]]

planeur = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


#evolution_n_generations(oscillateur,20)
#evolution_n_generations(planeur,20)