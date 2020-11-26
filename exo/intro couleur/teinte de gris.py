#coding:utf-8

from PIL import Image
a="01.jpg"
im=Image.open(a)

def negatifIM(image):
    c,l = image.size
    print(c, " ", l)
    imagearrive = Image.new('RGB',(c,l))
    for i in range(c): #on parcours les colonnes
        for j in range(l): #on parcours chaque ligne pour chacune des colonnes
            couleurPixel = image.getpixel((i,j))
            niveauGris = (couleurPixel[0] + couleurPixel[1] + couleurPixel[2]) // 3
            imagearrive.putpixel((i,j),(niveauGris,niveauGris,niveauGris))
    imagearrive.show()