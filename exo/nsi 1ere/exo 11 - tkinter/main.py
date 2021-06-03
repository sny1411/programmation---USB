#coding:utf-8

import tkinter

largeur = 800
hauteur = 600

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb
def soleil(x,y):
    x0 = x - 50
    y0 = y - 50
    x1 = x + 50
    y1 = y + 50
    zone_graphique.create_oval(x0, y0, x1, y1,fill='yellow',outline='yellow')
def sol(y):
    zone_graphique.create_rectangle(-5,y,largeur + 5,hauteur + 5,fill=_from_rgb((79,224,31)),outline=_from_rgb((79,224,31)))
def oiseau(x,y):
    zone_graphique.create_line(x+35,y,x,y-20, width=2)
    zone_graphique.create_line(x + 65, y - 20,x + 35,y, width=2)
def arbre(x,y):
    zone_graphique.create_rectangle(x,y,x+40,y-100,fill=_from_rgb((193,119,40)),outline =_from_rgb((193,119,40)))
    zone_graphique.create_oval(x-20,y-90,x+60,y-240,fill='green',outline='green')
def voiture(x,y):
    zone_graphique.create_rectangle(x,y-35,x+200,y-90)
    zone_graphique.create_oval(x+10,y,x+55,y-45)
    zone_graphique.create_oval(x+145,y,x+190,y-45)
    zone_graphique.create_polygon((x-175,y+120),(x-175,y+90),(x-125,y+120))



fenetre = tkinter.Tk()
fenetre.title("animation")

zone_graphique = tkinter.Canvas(fenetre,width=largeur,height=hauteur,bg='white')
zone_graphique.pack()

soleil(100,100)
sol(500)
oiseau(250,250)
arbre(600,500)
voiture(100,500)
"""
zone_graphique.create_rectangle(100,400,200,500)

zone_graphique.create_line(200,200,300,300)
zone_graphique.create_line(200,300,300,200)

zone_graphique.create_line(400,300,400,400)
zone_graphique.create_line(350,350,450,350)"""

fenetre.mainloop()



