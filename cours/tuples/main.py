#coding:utf-8

"""
creation tuple : mon_tuple = () #vide
				 mon_tuple = 10, # une seule valeur
				 mon_tuple = (10,) # idem au dessus
				 mon_tuple = (4,6) #plusieur valeur
"""


liste = [1,2,3,4,5,6]

for chose in enumerate(liste):
	print(chose)



mon_tuple = (45,)
print(type(mon_tuple))


def getPlayerPosition():
	posX = 148
	posY = 86
	return (posX,posY)
#prog principal

cordx = 0
cordy = 0

print("position joueur : ({}/{})".format(cordx,cordy))

(cordx,cordy) = getPlayerPosition()

print("position joueur : ({}/{})".format(cordx,cordy))
