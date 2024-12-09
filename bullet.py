from Screen import screen
from turtle import Turtle
import subprocess
import sys


class Bullet(Turtle):
    def __init__(self, source, tanks, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.35, stretch_len=0.35)
        self.x = 0
        self.y = 0
        self.source = source
        self.tanks = tanks
        self.active = True
        self.goto(position)

    def out_of_bound(self, screen_size=800):
        return abs(self.xcor()) > screen_size or abs(self.ycor()) > screen_size

    def disappear(self):
        self.active = False  # Mark as inactive when out of bounds
        self.hideturtle()

    def move(self):
        if not self.out_of_bound() and self.active:  # Check if still within bounds
            self.goto(self.xcor() + self.x, self.ycor() + self.y)
            # Schedule the next move
            for index, tank in enumerate(self.tanks):
                if tank.alive and tank.check_collision(self) and tank != self.source:
                    tank.die()
                    self.disappear()
                    self.tanks.pop(index)
            screen.ontimer(self.move, 50)
        else:
            self.disappear()


