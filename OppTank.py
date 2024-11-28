from turtle import Turtle
import random

directions = ["up", "down", "right", "left"]
from tank_main import MainTank
class OppTank(MainTank):
    def __init__(self):
        super().__init__()
        self.direction = directions[random.randint(0,len(directions)-1)]
        self.alive = True

    def opp_spawn(self):
        if not self.alive:
            return
        self.spawn()
        if self.direction == "right":
            self.turn_right()
        elif self.direction == "left":
            self.turn_left()
            self.turn_down()

    def die(self):
        self.alive = False  # Set alive status to False
        self.hideturtle()   # Hide the turtle
        self.clear()

    def out_of_bound(self, screen_size=800):
        # check if bullet is out of bound
        return abs(self.xcor()) > screen_size or abs(self.ycor()) > screen_size








