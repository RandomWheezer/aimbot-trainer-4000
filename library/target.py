# target system

import tkinter
import random

# game manager
from main import Canvas



# target system
class Target:
    def __init__(self, canvas):
        self.canvas = canvas
        self.target = canvas.create_oval(20, 20, 35, 35, fill="red")
        # define game manager variables
        self.score = self.score

    def spawn(self):
        x = random.randint(0, 800)
        y = random.randint(0, 600)
        self.canvas.coords(self.target, x, y, x+20, y+20)
        self.target.pack()

    def hit(self, event):
        x, y = event.x, event.y
        if self.target in self.canvas.find_overlapping(x, y, x, y):
            self.canvas.itemconfig(self.target, fill="green")
            self.canvas.after(500, self.spawn)
            self.score += 1