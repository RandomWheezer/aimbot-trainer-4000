# target system

import tkinter
import random

# import window (canvas) and game manager
from library.canvas import Canvas
from library.gamemanager import Manager

class Target:
    def __init__(self, canvas):
        self.canvas = canvas
        self.target = self.canvas.create_oval(0, 0, 0, 0, fill="red")

    def spawn(self):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        self.canvas.coords(self.target, x, y, x+50, y+50)

    def hit(self, event):
        x, y = event.x, event.y
        if self.canvas.find_overlapping(x, y, x, y):
            self.canvas.delete(self.target)
            self.spawn()
            self.manager.score += 1
    