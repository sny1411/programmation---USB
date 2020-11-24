from PIL import Image
a="balloon.jpeg"
im=Image.open(a)

def negatifIM(image):
    c,l = image.size
    print(c, " ", l)
    imagearrive = Image.new('RGB',(c,l))
    for i in range(c): #on parcours les colonnes
        for j in range(l): #on parcours chaque ligne pour chacune des colonnes
            couleurPixel = image.getpixel((i,j))
            imagearrive.putpixel((i,j),(255 - couleurPixel[0],255 - couleurPixel[1],255 - couleurPixel[2])) #in place la couleur choisie aux pixel (i,j)
    imagearrive.show()