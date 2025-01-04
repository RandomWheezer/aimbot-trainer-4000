import time
import tkinter as tk
from library import gamemanager
from main import Canvas

# Create an instance of Canvas
canvas_instance = Canvas()

root = tk.Tk()
canvas = Canvas(root)
canvas.pack()


class Timer:

    def __init__(self):
        self.canvas = canvas

    for i in range(30):
        time.sleep(1)
        canvas_instance.create_text(400, 300, text="Game Over", font=("Arial", 50))

        if gamemanager.timer <= 0:
            canvas.delete("all")
            Canvas.create_text(400, 300, text="Game Over", font=("Arial", 50))
            time.sleep(3)
            break
