from tkinter import *
import random

win = Tk()
win.geometry("350x200")


score = 0
time = 30
colors = ["Red", "Green", "Blue", "Yellow", "Black", "White"]


def countdown():
    global time
    if time > 0:
        time -=1
        time_left.config(text="Time: "+str(time))
        time_left.after(1000, countdown)
    else:
        entry.config(state='disabled')


def StartGame(event):
    if time == 30:
        countdown()
    ChangeColor()


def ChangeColor():
    global score
    a = entry.get().lower()
    if a == colors[1].lower():
        score = score + 1
        Score.config(text="Score: " + str(score))
    random.shuffle(colors)
    label.config(text=colors[0], fg=colors[1])
    entry.delete(0, END)


instructions = Label(win, text="Type in the color of the words!", font=("Tahoma", 10))
instructions.pack()

Score = Label(win, text="Score: ", font=("Tahoma", 10))
Score.pack()

time_left = Label(win, text="Time Left: ", font=("Tahoma", 10))
time_left.pack()

label = Label(win,font=("Tahoma", 30))
label.pack()

entry = Entry(win)
entry.pack()


win.bind('<Return>', StartGame)

win.mainloop()
