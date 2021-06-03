from PIL import Image

with Image.open("balloon.jpeg") as ballon: #ouvre une image située dans le meme dossier
    #ballon.show()
    largeur,hauteur = ballon.size #donne directement la largeur et la hauteur de l'image
    print("lageur = ", largeur)
    print("hauteur = ", hauteur)

    donnee=ballon.getdata() #extrait les données de l'image
    #print(ballon.mode) # precise comment sont codés les couleurs
    #pixel102103=donnee.getpixel((102,103)) #permet de connaitre le code rgb du pixel 102,103
    #print(pixel102103)


    #on veut retourner l'image(gauche,droite)

    donneeRetournee = donnee.copy() # on crée un nouveau fichier de donnée à l'aide d'une copie
    #pas besoin de donner les dimension ni le mode
