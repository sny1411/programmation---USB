from PIL import Image

def sup_4bit_drt(photo):
    """supprime les 4 bits de poids faible
    param photo (string): la photo de départ
    return: image modifié"""
    image = Image.open(photo)
    largeur, hauteur = image.size
    data = image.getdata()
    data_nouv=data.copy()
    for i in range(largeur):
        for j in range(hauteur):
            r, g, b =data.getpixel((i,j))
            r1,g1,b1 =r&240, g&240, b&240
            data_nouv.putpixel((i,j),(r1,g1,b1))
    image_nouv = Image.new(image.mode,(largeur,hauteur))
    image_nouv.putdata(data_nouv)
    return image_nouv
"""
image_tronque = sup_4bit_drt("carte 3.jpg")
image_tronque.save("image_tronque.png")
image_tronque.show()
image_pays =sup_4bit_drt("paysage.jpg")
image_pays.save("paysage2.png")"""

def depl_4bit_gch_drt(photo):
    """déplace les 4 bits de droite à gauche
    param photo (string): photo à modifier
    return: nouvelle image"""
    image = Image.open(photo)
    largeur, hauteur = image.size
    data = image.getdata()
    data_nouv=data.copy()
    for i in range(largeur):
        for j in range(hauteur):
            r, g, b =data.getpixel((i,j))
            r1,g1,b1 = r//16, g//16, b//16
            data_nouv.putpixel((i,j),(r1,g1,b1))
    image_nouv = Image.new(image.mode,(largeur,hauteur))
    image_nouv.putdata(data_nouv)
    return image_nouv

#image_tronque_depl=depl_4bit_gch_drt("image_tronque.png")
#image_tronque_depl.save("image_depl.png")
#image_tronque_depl.show()

def somme(ph1,ph2):
    """cache la photo 1 dans la photo2
    param: photo 1 et 2 (str) sont deux photos
    return: retourne l'image en additionnant les pixels"""
    image1 = Image.open(ph1)
    image2 = Image.open(ph2)
    largeur,hauteur=image1.size
    lc,hc=image2.size
    data_image1=image1.getdata()
    data_image2=image2.getdata()
    data_somme=data_image2.copy()
    for i in range(lc):
        for j in range(hc):
            r1,g1,b1=data_image1.getpixel((i,j))
            r2,g2,b2=data_image2.getpixel((i,j))
            r,g,b=r1+r2, g1+g2, b1+b2
            data_somme.putpixel((i,j),(r,g,b))
    image_somme = Image.new(image1.mode,(largeur,hauteur))
    image_somme.putdata(data_somme)
    return image_somme

#image_somme=somme("image_depl.png","paysage2.png")
#image_somme.show()
#image_somme.save("image_somme.png")

def recup_image_cachee(photo):
    """récupère les 4 pixels de droite et les déplace à gauche
    param photo (string): image avec la photo cachée
    return: la photo cachée"""
    img = Image.open(photo)
    l,h = img.size
    data_img = img.getdata()
    data_nouv = data_img.copy()
    for i in range(l):
        for j in range(h):
            print(i,' ',j)
            r,g,b=data_img.getpixel((i,j))
            r,g,b= r&15,g&15,b&15
            r,g,b = r*16,g*16,b*16
            data_nouv.putpixel((i,j),(r,g,b))
    img_recup = Image.new(img.mode,(l,h))
    img_recup.putdata(data_nouv)
    return img_recup

img = recup_image_cachee('exo\exo 10 - cacher un image dans une image\correction prof\sny.png')
img.show()

