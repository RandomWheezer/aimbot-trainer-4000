# creates the canvas (window)

import tkinter
import random # might be pointless but just in case

# import window (canvas) and game manager
from library.gamemanager import Manager
from library.target import Target

class Canvas:
    def __init__(self, width, height, bg):
        self.game = tkinter.Tk()
        self.game.title("Aim Trainer 4000")
        self.game.geometry(f"{width}x{height}")

        self.canvas = tkinter.Canvas(self.game, width=width, height=height, bg=bg)
        self.canvas.pack()

    game = tkinter.Tk()
    game.title("Aim Trainer 4000")
    game.geometry("800x600")

    canvas = tkinter.Canvas(game, width=800, height=600, bg="black")
    canvas.pack()

    # mainloop lets the window run
    game.mainloop()

    canvas.create_text(700,500, text= f"score: {self.score}",fill="white", font=("Arial", 20))
    canvas.create_text(700,470, text= f"time: {self.timer}",fill="white", font=("Arial", 20))
