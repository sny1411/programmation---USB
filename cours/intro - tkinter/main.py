#coding:utf-8

import tkinter
#from tkinter import * -> pour tout importer et pas devoir reecrire tkinter.<ft> 

"""
geometry("XxY+0+0")
mainapp.quit() -> quitte la fenetre manuellement
#mainapp.minsize(640,480) #taille minimal fenetre
#mainapp.maxsize(1280,720) #taille max fenetre
#mainapp.positionfrom("user")
"""

mainapp = tkinter.Tk()

screen_x = mainapp.winfo_screenwidth()
screen_y = mainapp.winfo_screenheight()
window_x = 800
window_y = 600

pos_X = (screen_x // 2) - (window_x // 2)
pos_Y = (screen_y // 2) - (window_y // 2)

mainapp.title("Mon premier prog en fenetre")
geo = "{}x{}+{}+{}".format(window_x,window_y,pos_X,pos_Y)
mainapp.geometry(geo) #taille de base 

mainapp.resizable(width=False,height=False) # si on peut redimentionner


mainapp.mainloop()




