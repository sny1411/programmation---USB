#coding:utf-8

import tkinter
from PIL import Image

largeur = 800
hauteur = 600
pos_voiture = [100,500]
pos_oiseau = [150,250]


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
def oiseau_1(x,y):
    zone_graphique.create_line(x+35,y,x,y-20, width=2)
    zone_graphique.create_line(x + 65, y - 20,x + 37,y, width=2)
def oiseau_2(x,y):
    zone_graphique.create_line(x+35,y,x,y+20,width=2)
    zone_graphique.create_line(x + 65, y + 20,x + 37, y,width=2)
def arbre(x,y):
    zone_graphique.create_rectangle(x,y,x+40,y-100,fill=_from_rgb((193,119,40)),outline =_from_rgb((193,119,40)))
    zone_graphique.create_oval(x-20,y-90,x+60,y-240,fill='green',outline='green')
def arbre_tombe(x,y):
    zone_graphique.create_rectangle(x,y,x+100,y-40,fill=_from_rgb((193,119,40)),outline =_from_rgb((193,119,40)))
    zone_graphique.create_oval(x+90,y+20,x+240,y-60,fill='green',outline='green')
def voiture(x,y):
    zone_graphique.create_rectangle(x,y-35,x+200,y-90,fill=_from_rgb((237,51,14)))
    zone_graphique.create_oval(x+10,y,x+55,y-45,fill=_from_rgb((0,0,0)))
    zone_graphique.create_oval(x+145,y,x+190,y-45,fill=_from_rgb((0,0,0)))
    zone_graphique.create_rectangle(x+25,y-90,x+175,y-135,fill=_from_rgb((255,255,102)))

frame_oiseau = 0
def animation():
    global frame_oiseau
    running = True
    zone_graphique.delete('all')
    soleil(100,100)
    sol(500)
    if frame_oiseau <= 25:
        oiseau_1(pos_oiseau[0],pos_oiseau[1])
        pos_oiseau[1] += 2
    elif frame_oiseau > 25 and frame_oiseau <= 50:
        oiseau_2(pos_oiseau[0],pos_oiseau[1])
        pos_oiseau[1] -= 2
    else:
        frame_oiseau = 0
    frame_oiseau += 1
    if pos_oiseau[0] > 800:
        pos_oiseau[0] = -50
    pos_oiseau[0] += 1
    if pos_voiture[0] + 200 < 600:
        arbre(600,500)
        voiture(pos_voiture[0],pos_voiture[1])
        pos_voiture[0] += 3
    else:
        arbre_tombe(600,500)
        voiture(400,500)
    zone_graphique.update()
    if running == True:
        fenetre.after(25,animation)

fenetre = tkinter.Tk()
fenetre.title("animation")

zone_graphique = tkinter.Canvas(fenetre,width=largeur,height=hauteur,bg='white')
zone_graphique.pack()

animation()
"""
zone_graphique.create_rectangle(100,400,200,500)

zone_graphique.create_line(200,200,300,300)
zone_graphique.create_line(200,300,300,200)

zone_graphique.create_line(400,300,400,400)
zone_graphique.create_line(350,350,450,350)"""

fenetre.mainloop()


