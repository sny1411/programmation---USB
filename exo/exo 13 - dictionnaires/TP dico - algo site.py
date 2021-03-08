#coding:utf-8
import random

websites = ["A","B","C","D","E","F"] #liste des sites web
hypertext = {} #dictionnaire des liens hypertext de chaque sites web
hypertext["A"] = ["B","C","E"]
hypertext["B"] = ["F"]
hypertext["C"] = ["A","E"]
hypertext["D"] = ["B","C"]
hypertext["E"] = ["A","B","C","D","F"]
hypertext["F"] = ["E"]

nb_visites = {nomSite : 0 for nomSite in websites} #dictionaire du nombre de visite de chaque site

def visites():
    """fonction qui détermine le nombre de visites sur chaque site de façon aléatoire
    return: dictionnaire """
    i=0
    while i < 1000:
        siteAlea = random.choice(websites)
        while random.random() < 0.85:
            nb_visites[siteAlea] += 1
            siteAlea = random.choice(hypertext[siteAlea])
        i += 1
    return nb_visites

    
def classement(dico):
    """classe les sites en fonction du nombre de visites
    param dico (dictionnaire): dictionnaire des sites avec le nombre de visites
    return: liste des sites par ordre décroissant de popularité"""
    dico = dict(sorted(dico.items(), key=lambda item: item[1],reverse=True))
    return list(dico.keys())

print(visites())
print(classement(nb_visites))
