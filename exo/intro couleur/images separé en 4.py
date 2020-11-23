# Créé par stuba, le 23/11/2020 en Python 3.7

from PIL import Image
a="balloon.jpeg"
im=Image.open(a)

def couperenquatre(image):
    c,l = image.size
    imagearrive = Image.new('RGB',(c,l))
    for i in range(l//2):#On va prendre le quart en haut à gauche
        for j in range(c//2):
            p=image.getpixel((j,i))
            imagearrive.putpixel((c//2+j,l//2+i),p) # On le place en bas à droite



    for i in range(l//2): #On va prendre le quart en haut à droite
        for j in range(c//2,c):
            p=image.getpixel((j,i))
            imagearrive.putpixel((j-c//2,l//2+i),p) # On le place en bas à gauche



    for i in range(l//2,l): # on va prendre le quart en bas à gauche"""
        for j in range(c//2):
            p=image.getpixel((j,i))
            imagearrive.putpixel((c//2+j,i-l//2),p) #On le place en haut à droite


    for i in range(l//2,l):#On va prendre le quart à droite en bas
        for j in range(c//2,c):
            p=image.getpixel((j,i))
            imagearrive.putpixel((j-c//2,i-l//2),p) #On le place en haut à gauche
    imagearrive.show()


