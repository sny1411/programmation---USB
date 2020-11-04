#coding:utf-8
import math


def Aire_carre(longueur):
	longueur = longueur*longueur
	return longueur

def perimetre_carre(longueur):
	longueur = longueur*4
	return longueur

def volume_cube(longueur):
	longueur = longueur*longueur*longueur
	return longueur

def perimetre_cercle(rayon):
	rayon = 2*3.14*rayon
	return rayon

def aire_cercle(rayon):
	rayon = 3.14*math.pow(rayon,2)
	return rayon

def volume_sphere(rayon):
	rayon = (4*3.14*math.pow(rayon,3))/3
	return rayon


if __name__ == "__main__": #if de test =>
	print(f"aire carré = {Aire_carre(5)} (coté : 5)")
	print(f"perimetre_carre = {perimetre_carre(5)} (coté : 5)")
	print(f"volume_cube = {volume_cube(5)} (coté : 5)")
	print(f"perimetre_cercle = {perimetre_cercle(5)} (rayon : 5)")
	print(f"aire_cercle = {aire_cercle(5)} (rayon : 5)")
	print(f"volume_sphere = {volume_sphere(5)} (rayon : 5)")