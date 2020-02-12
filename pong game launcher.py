import tkinter

win = tkinter.Tk()
win.geometry("400x200")
win.configure(background='black')


def butt2():
    import pong_game.py


def butt1():
    import pong_pre.py


win.title('pong games')
lab = tkinter.Label(win, text='hello ,welcome to this game', background='black', foreground='white',
                    font='blowbrush 22').pack()
lab2 = tkinter.Label(win, text='this is a pong game', background='black', foreground='white', font='Algerian 22').pack()
lab3 = tkinter.Label(win, text='select number of player', background='black', foreground='white',
                     font='times 22').pack()
bu1 = tkinter.Button(win, text='1 player', command=butt1, background='grey').pack()
bu2 = tkinter.Button(win, text='2 player', command=butt2, background='grey').pack()
win.mainloop()
