#coding:utf-8
import tkinter
import geoshape

def update_labelVrb(*args):
	var_labelV.set("longueur/rayon = {} cm".format(var_entryV.get()))
	var_entryV_valid.set(var_entryV.get())
def fAireCarre():
	Var_result.set("Aire = {} cm²".format(geoshape.Aire_carre(var_entryV_valid.get())))

def fPeriCarre():
	Var_result.set("périmetre = {} cm".format(geoshape.perimetre_carre(var_entryV_valid.get())))

def fVolCube():
	Var_result.set("volume = {} cm³".format(geoshape.volume_cube(var_entryV_valid.get())))

app = tkinter.Tk()
app.geometry("640x480")
app.title("exo geometrie")


#------------------------------- creation frame + btn carré -------------------------------
frame_carre = tkinter.LabelFrame(app,text="operation carré/cube",width=150,height=200,borderwidth=2)
frame_carre.place(x=500,y=10)

btn1_carre = tkinter.Button(frame_carre,text="aire", command=fAireCarre)
btn2_carre = tkinter.Button(frame_carre,text="périmetre",command=fPeriCarre)
btn3_carre = tkinter.Button(frame_carre,text="volume",command=fVolCube)

btn1_carre.grid(padx=20,pady=5)
btn2_carre.grid(padx=20,pady=5)
btn3_carre.grid(padx=20,pady=5)
#------------------------------------------------------------------------------------------



#--------------------------- creation frame + widgets variable ----------------------------
frame_variable = tkinter.LabelFrame(app,text="longueur/rayon",width=150,height=130,borderwidth=2)
frame_variable.place(x=10,y=20)

var_entryV_valid = tkinter.IntVar()
var_entryV = tkinter.IntVar()
slider_variable = tkinter.Scale(frame_variable, from_=1,to=100,variable=var_entryV,orient="horizontal",sliderlength=20)
btn_variable = tkinter.Button(frame_variable,text="modifier",command=update_labelVrb)
var_labelV = tkinter.StringVar()
var_labelV.set("longueur/rayon = none")
label_variable = tkinter.Label(frame_variable,textvariable=var_labelV)

slider_variable.place(x=20,y=5)
btn_variable.place(x=40,y=50)
label_variable.place(x=5,y=80)


#------------------------------------------------------------------------------------------
Var_result = tkinter.StringVar()
Var_result.set("RESULTAT = NONE")
Label_result = tkinter.Label(app,textvariable=Var_result)
Label_result.place(x=275,y=200)


app.mainloop()