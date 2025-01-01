# main file

import tkinter

# adding important modules


# import window (canvas) and game manager

class Canvas:
    def __init__(self, width, height, bg, score_x=700, score_y=500, time_x=700, time_y=470):
        self.game = tkinter.Tk()
        self.game.title("Aim Trainer 4000")
        self.game.geometry(f"{width}x{height}")
        self.score = 0
        self.timer = 60


        self.canvas = tkinter.Canvas(self.game, width=width, height=height, bg=bg)
        self.canvas.pack()

        self.canvas.create_text(score_x, score_y, text=f"score: {self.score}", fill="white", font=("Arial", 20))
        self.canvas.create_text(time_x, time_y, text=f"time: {self.timer}", fill="white", font=("Arial", 20))

# mainloop lets the window run
if __name__ == "__main__":
    aim_trainer_canvas = Canvas(800, 600, "black")
    aim_trainer_canvas.game.mainloop()
