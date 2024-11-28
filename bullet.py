import time
from turtle import Turtle
import subprocess
import sys


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.x = 0
        self.y = 0

    def move(self):
        while not self.out_of_bound():
            self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def out_of_bound(self, screen_size=800):
        # check if bullet is out of bound
        return abs(self.xcor()) > screen_size or abs(self.ycor()) > screen_size



if __name__ == "__main__":
    subprocess.run([sys.executable, 'tank_main.py'])
