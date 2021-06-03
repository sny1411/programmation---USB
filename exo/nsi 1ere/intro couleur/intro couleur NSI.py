from PIL import Image #importe la partie image de PIL

rectangle = Image.new("RGB",(100,200)) #créé une nouvelle image en code RGB et de dimensions 100(largeur) * 200(hauteur)

for i in range(100): #on parcours les colonnes
    for j in range(200): #on parcours chaque ligne pour chacune des colonnes
        if j < 100:
            rectangle.putpixel((i,j),(121, 248, 248)) #in place la couleur choisie aux pixel (i,j)
        else:
            rectangle.putpixel((i,j),(58, 242, 75))

rectangle.show() #on affiche la figure

