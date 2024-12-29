import time

from library.canvas import Canvas
from library.gamemanager import Manager
from library.target import Target

for i in range(30):
    time.sleep(1)
    gamemanager.timer -= 1

    if timer =< 0:
        canvas.delete("all")
        canvas.create_text(400, 300, text="Game Over", font=("Arial", 50))
        time.sleep(3)
        break
