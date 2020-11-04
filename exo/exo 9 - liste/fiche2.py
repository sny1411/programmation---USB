#coding:utf-8

#exemple 2
villes = ["Bordeaux","Paris","Lens", "Grenoble"]
villesES = ["Barcelone","Pampelune","Ibiza"]
villes.extend(villesES)
print(villes)


#exemple 3
villes2 = ["Bordeaux","Paris"]
towns = villes
towns.append("Lille")
print(villes2)