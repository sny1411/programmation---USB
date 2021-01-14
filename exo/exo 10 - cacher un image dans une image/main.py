import fonction
from PIL import Image

def cacherImage():
    img = Image.open("exo\exo 10 - cacher un image dans une image\paysage.jpg")
    carteCacher =Image.open("exo\exo 10 - cacher un image dans une image\carte 3.jpg")

    c,l = img.size
    print(c, " ", l)
    imageFinal = Image.new('RGB',(c,l))
    for i in range(c): #on parcours les colonnes
            for j in range(l): #on parcours chaque ligne pour chacune des colonnes
                imgPixel = img.getpixel((i,j))
                cartePixel = carteCacher.getpixel((i,j))
                pixelMelanger = (fonction.echangeBitFortFaible(imgPixel[0],cartePixel[0]),fonction.echangeBitFortFaible(imgPixel[1],cartePixel[1]),fonction.echangeBitFortFaible(imgPixel[2],cartePixel[2]))
                imageFinal.putpixel((i,j), pixelMelanger)
    imageFinal.show()

def retrouverImage():
    img = Image.open("yes.png")
    c , l = img.size
    imageRetrouver = Image.new('RGB', (c,l))
    for i in range(c):
        for j in range(l):
            imgPixel = img.getpixel((i,j))
            pixelCacher = (fonction.reconstitutionImage(imgPixel[0]),fonction.reconstitutionImage(imgPixel[1]),fonction.reconstitutionImage(imgPixel[2]))
            imageRetrouver.putpixel((i,j), pixelCacher)
    imageRetrouver.show()