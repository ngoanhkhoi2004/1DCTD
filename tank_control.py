from turtle import Turtle
from bullet import Bullet
import subprocess
import sys
import random

class MainTank(Turtle):
    def __init__(self):
        super().__init__()
        self.setx(0)
        self.sety(0)
        self.body = []
        self.alive = True
        self.bullet_speed = 17


    def spawn(self, body_list):
        for i in range(3):
            square = Turtle()
            square.penup()
            square.shape("square")
            square.color("white")
            square.goto(self.xcor()+22*i, self.ycor())
            body_list.append(square)
        square = Turtle()
        square.shape("square")
        square.penup()
        square.color("white")
        square.goto(self.xcor() + 22 * 1, self.ycor()+22)
        body_list.append(square)


    def shoot(self, tanks):
        bullet = Bullet("main_tank", tanks)
        bullet.goto(self.body[3].xcor(), self.body[3].ycor())
        orientation = self.get_orientation()
        data = {"up": [0, self.bullet_speed], "down": [0, -self.bullet_speed], "left": [-self.bullet_speed, 0], "right": [self.bullet_speed, 0]}
        bullet.x = data[orientation][0]
        bullet.y = data[orientation][1]
        bullet.move()

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

    def shoot(self, tanks):
        bullet = Bullet(
            x=self.body[3].xcor(),
            y=self.body[3].ycor(),
            dx=0,
            dy=0,
            source=self,
            tanks=tanks
        )
        orientation = self.get_orientation()
        data = {"up": [0, self.bullet_speed], "down": [0, -self.bullet_speed],
                "left": [-self.bullet_speed, 0], "right": [self.bullet_speed, 0]}
        bullet.dx = data[orientation][0]
        bullet.dy = data[orientation][1]
        bullet.move()


    def check_collision(self, bullet):
        if bullet.source == self:
            return False
        for square in self.body:
            if bullet.distance(square) < 15:
                return True
        return False

    def die(self):
        self.alive = False
        for square in self.body:
            square.hideturtle()
            square.clear()
        self.body.clear()

if __name__ == "__main__":
    subprocess.run([sys.executable, 'tank_main.py'])