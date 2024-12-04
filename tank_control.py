import time
from turtle import Turtle

import bullet
from bullet import Bullet
import sys
import subprocess

class MainTank(Turtle):
    def __init__(self):
        super().__init__()
        self.body = []
        self.orientation = "up" # default orientation

    def spawn(self):
        #spawn tank with body parts
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

    def get_orientation(self):
        """Returns the current orientation of the tank."""
        return self.orientation

    def set_orientation(self, direction):
        """Update the tank's orientation."""
        self.orientation = direction
        self.update_body()

    def update_body(self):
        """Update the tank's body to match the current orientation."""
        x, y = self.body[1].xcor(), self.body[1].ycor()

        if self.orientation == "up":
            self.body[0].goto(x - 22, y)
            self.body[2].goto(x + 22, y)
            self.body[3].goto(x, y + 22)
        elif self.orientation == "down":
            self.body[0].goto(x + 22, y)
            self.body[2].goto(x - 22, y)
            self.body[3].goto(x, y - 22)
        elif self.orientation == "left":
            self.body[0].goto(x, y + 22)
            self.body[2].goto(x, y - 22)
            self.body[3].goto(x - 22, y)
        elif self.orientation == "right":
            self.body[0].goto(x, y - 22)
            self.body[2].goto(x, y + 22)
            self.body[3].goto(x + 22, y)

    def move(self):
        """Move the tank in the current orientation."""
        if self.orientation == "up":
            for square in self.body:
                square.goto(square.xcor(), square.ycor() + 22)
        elif self.orientation == "down":
            for square in self.body:
                square.goto(square.xcor(), square.ycor() - 22)
        elif self.orientation == "left":
            for square in self.body:
                square.goto(square.xcor() - 22, square.ycor())
        elif self.orientation == "right":
            for square in self.body:
                square.goto(square.xcor() + 22, square.ycor())

    def turn_up(self):
        """Orient the tank upward."""
        if self.orientation != "up":
            self.set_orientation("up")

    def turn_down(self):
        """Orient the tank downward."""
        if self.orientation != "down":
            self.set_orientation("down")

    def turn_left(self):
        """Orient the tank to the left."""
        if self.orientation != "left":
            self.set_orientation("left")

    def turn_right(self):
        """Orient the tank to the right."""
        if self.orientation != "right":
            self.set_orientation("right")


    def shoot(self):
        # shoot bullet in current orientation
        if self.body:
            #bullet origin at top of tank, third piece
            bullet_origin = self.body[3]
            bullet_x = bullet_origin.xcor()
            bullet_y = bullet_origin.ycor()

            # Set bullet direction based on tank orientation
            if self.orientation == "up":
                bullet_dx, bullet_dy = 0, 10  # Move upward
            elif self.orientation == "down":
                bullet_dx, bullet_dy = 0, -10  # Move downward
            elif self.orientation == "left":
                bullet_dx, bullet_dy = -10, 0  # Move left
            elif self.orientation == "right":
                bullet_dx, bullet_dy = 10, 0  # Move right

            # bullet moving up
            bullet = Bullet(bullet_x, bullet_y, bullet_dx, bullet_dy)

            def bullet_move():
        # recursive moving bullet
                bullet.move()
                if bullet.active:
                    bullet.getscreen().ontimer(bullet_move, 50)

            bullet_move()


if __name__ == "__main__":
    subprocess.run([sys.executable, 'tank_main.py'])
