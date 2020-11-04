#coding:utf-8
import tkinter
import game


def main_quit():
	mainApp.quit()
def runGame():
	game.game()


mainApp = tkinter.Tk()

mainApp.configure(bg='#EDD997')
mainApp.title("Devine Mot")
mainApp.resizable(width=False,height=False)
screen_x = mainApp.winfo_screenwidth()
screen_y = mainApp.winfo_screenheight()
window_x = 350
window_y = 82

pos_X = (screen_x // 2) - (window_x // 2)
pos_Y = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x,window_y,pos_X,pos_Y)
mainApp.geometry(geo)

mainFrame = tkinter.Frame(mainApp,width=300,height=150,)

mainFrame.pack()

btn_newGame = tkinter.Button(mainFrame,text="nouvelle partie",bg='green',width=50,height=2,command=game.game)
btn_newGame.pack()
btn_quit = tkinter.Button(mainFrame,text="quitter le programme", command=main_quit, bg='red',width=50,height=2)
btn_quit.pack()

mainApp.mainloop()