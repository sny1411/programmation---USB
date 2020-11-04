#coding:utf-8

"""
pour faire des boucles : - while / for 
Mots-clés : break (casse la boucle) / continue (reviens au debut de la boucle)
"""
i = 0

while i <= 300:
	print("{} - JE SUIS UNE PHRASE !".format(i))
	i += 1

sentence = "SALUT TOUT LE MONDE"

for letter in sentence:
	print(letter)

print("à bientot")