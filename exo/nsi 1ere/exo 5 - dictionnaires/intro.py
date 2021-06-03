#coding:utf-8

anissa=["Kacmarek","Anissa","1F",["nsi","maths","SVT"],[15,16.8,15.3]]
kevin=["Dupont","Kévin","1G",["SVT","maths","physique"],[8.9,10.3,9.8]]
les_eleve=[anissa,kevin]


def eleves_specialite(spec,les_elvs):
    """retourne la liste des noms et prénoms des élèves qui ont choisi la spétialité spec
    param spec : str -> la spécialité
    param les_elvs : list(eleve)
    return: list(str)"""
    eleves_spe = []
    for eleve in les_elvs:
        if spec in eleve[3]:
            eleves_spe.append(f"{eleve[0]} {eleve[1]}")
    return eleves_spe

print(eleves_specialite("maths",les_eleve))

    