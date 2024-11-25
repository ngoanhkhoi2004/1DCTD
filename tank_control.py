import time
from turtle import Turtle
from bullet import Bullet
import sys
import subprocess

class MainTank(Turtle):
    def __init__(self):
        super().__init__()
        self.setx(0)
        self.sety(0)
        self.body = []

    def spawn(self):
        for i in range(3):
            square = Turtle()
            square.penup()
            square.shape("square")
            square.color("white")
            square.goto(self.xcor()+22*i, self.ycor())
            self.body.append(square)
        square = Turtle()
        square.shape("square")
        square.penup()
        square.color("white")
        square.goto(self.xcor() + 22 * 1, self.ycor()+22)
        self.body.append(square)

    def shoot(self):
        pass

    def rotate(self, direction):
        """
        Rotate the tank either clockwise or anticlockwise.
        """
        body0 = self.body[0]
        body1 = self.body[1]
        body2 = self.body[2]
        body3 = self.body[3]

        if direction == "clockwise":
            body0.goto(body3.xcor(), body3.ycor())
            body3.goto(body2.xcor(), body2.ycor())
            if body2.xcor() > body1.xcor() and body2.ycor() == body1.ycor():
                body2.goto(body1.xcor(), body1.ycor() - 22)
            elif body2.xcor() < body1.xcor() and body2.ycor() == body1.ycor():
                body2.goto(body1.xcor(), body1.ycor() + 22)
            elif body2.xcor() == body1.xcor() and body2.ycor() > body1.ycor():
                body2.goto(body1.xcor() + 22, body1.ycor())
            elif body2.xcor() == body1.xcor() and body2.ycor() < body1.ycor():
                body2.goto(body1.xcor() - 22, body1.ycor())

        elif direction == "anticlockwise":
            body2.goto(body3.xcor(), body3.ycor())
            body3.goto(body0.xcor(), body0.ycor())
            if body0.xcor() > body1.xcor() and body0.ycor() == body1.ycor():
                body0.goto(body1.xcor(), body1.ycor() + 22)
            elif body0.xcor() < body1.xcor() and body0.ycor() == body1.ycor():
                body0.goto(body1.xcor(), body1.ycor() - 22)
            elif body0.xcor() == body1.xcor() and body0.ycor() > body1.ycor():
                body0.goto(body1.xcor() - 22, body1.ycor())
            elif body0.xcor() == body1.xcor() and body0.ycor() < body1.ycor():
                body0.goto(body1.xcor() + 22, body1.ycor())

    def get_orientation(self):
        """
        Determines the orientation of the tank.

        Returns:
            str: "up", "down", "left", or "right"
        """
        if self.body[3].ycor() > self.body[1].ycor() and self.body[1].xcor() == self.body[3].xcor():
            return "up"
        elif self.body[3].ycor() < self.body[1].ycor() and self.body[1].xcor() == self.body[3].xcor():
            return "down"
        elif self.body[3].ycor() == self.body[1].ycor() and self.body[1].xcor() < self.body[3].xcor():
            return "right"
        elif self.body[3].ycor() == self.body[1].ycor() and self.body[1].xcor() > self.body[3].xcor():
            return "left"

    def turn_right(self):
        """
        Rotate the tank to point right.
        """
        orientation = self.get_orientation()

        if orientation == "up":  # Up state
            self.rotate("clockwise")
        elif orientation == "left":  # Left state
            self.rotate("clockwise")
            self.rotate("clockwise")
        elif orientation == "down":  # Down state
            self.rotate("anticlockwise")

    def turn_left(self):
        """
        Rotate the tank to point left.
        """
        orientation = self.get_orientation()

        if orientation == "up":
            self.rotate("anticlockwise")
        elif orientation == "right":
            self.rotate("anticlockwise")
            self.rotate("anticlockwise")
        elif orientation == "down":
            self.rotate("clockwise")

    def turn_up(self):
        """
        Rotate the tank to point up.
        """
        orientation = self.get_orientation()

        if orientation == "right":  # Right state
            self.rotate("anticlockwise")
        elif orientation == "left":  # Left state
            self.rotate("clockwise")
        elif orientation == "down":  # Down state
            self.rotate("anticlockwise")
            self.rotate("anticlockwise")
        # Up state already aligned; no action needed

    def turn_down(self):
        """
        Rotate the tank to point down.
        """
        orientation = self.get_orientation()

        if orientation == "up":  # Up state
            self.rotate("clockwise")
            self.rotate("clockwise")
        elif orientation == "right":  # Right state
            self.rotate("clockwise")
        elif orientation == "left":  # Left state
            self.rotate("anticlockwise")

    def move(self):

        orientation = self.get_orientation()
        if orientation == "up":
            for square in self.body:
                square.goto(square.xcor(), square.ycor()+11)
        elif orientation == "down":
            for square in self.body:
                square.goto(square.xcor(), square.ycor()-11)
        elif orientation == "right":
            for square in self.body:
                square.goto(square.xcor()+11, square.ycor())
        elif orientation == "left":
            for square in self.body:
                square.goto(square.xcor()-11, square.ycor())

if __name__ == "__main__":
    subprocess.run([sys.executable, 'tank_main.py'])