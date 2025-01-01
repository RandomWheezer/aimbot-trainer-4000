# game manager

# import
import tkinter
import random

class Manager:
    def __init__(self):
        self.score = 0
        self.timer = 30

    def return_score(self):
        return self.score
    
    def return_time(self):
        return self.time