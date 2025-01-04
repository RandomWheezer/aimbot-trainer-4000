# main file

import tkinter as tk



class Canvas:
    def __init__(self, width, height, bg, score, timer):
        self.game = tk.Tk()
        self.game.title("Aim Trainer 4000")
        self.game.geometry(f"{width}x{height}")
        self.score = self.score
        self.timer = self.timer


        self.canvas = tk.Canvas(self.game, width=width, height=height, bg=bg)
        self.canvas.pack()

        self.canvas.create_text(700, 500, text=f"score: {self.score}", fill="white", font=("Arial", 20))
        self.canvas.create_text(700, 470, text=f"time: {self.timer}", fill="white", font=("Arial", 20))

# mainloop lets the window run
if __name__ == "__main__":
    aim_trainer_canvas = Canvas(800, 600, "black")
    aim_trainer_canvas.game.mainloop()
