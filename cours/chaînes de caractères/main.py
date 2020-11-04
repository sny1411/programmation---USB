#coding:utf-8

"""
classe str : string (chaine de carac)

méthodes : str.upper() , str.lower(), 
		   str.capitalize(), str.title()

str.center(<largeur> , caractere_remplissage)
str.index(<chaine> , <début> , <fin>)
str.strip -> enleve espaces
str.replace(<ancienne> , <nouvelle> , <occurences>)
"""

phrase = "bonjour ! "

phrase = phrase + "salut !"
phrase = phrase.title()
print(phrase)

ch1 = "bonjour"
ch2 = ch1

print(ch1)
print(ch2)

ch1 = ch1.upper()

print(ch1)
print(ch2)

st1 = "test"
st1 = st1.center(50 , "-")

print(st1)



