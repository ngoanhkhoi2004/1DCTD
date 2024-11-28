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

    def move_left(self):
            # tank moves left
            for square in self.body:
                square.goto(square.xcor() - 22, square.ycor())

    def move_right(self):
        # move tank right
        for square in self.body:
            square.goto(square.xcor() + 22, square.ycor())

    def move_down(self):
        # move tank down
        for square in self.body:
            square.goto(square.xcor(), square.ycor() - 22)

    def move_up(self):
        # move tank up
        for square in self.body:
            square.goto(square.xcor(), square.ycor() + 22)


    def shoot(self):
        # shoot bullet in current orientation
        if self.body:
            #bullet origin at top of tank, third piece
            bullet_origin = self.body[3]
            bullet_x = bullet_origin.xcor()
            bullet_y = bullet_origin.ycor() + 22

            # bullet moving up
            bullet = Bullet(bullet_x, bullet_y, 0, 10)

            def bullet_move():
        # recursive moving bullet
                bullet.move()
                if bullet.active:
                    bullet.getscreen().ontimer(bullet_move, 50)

            bullet_move()


if __name__ == "__main__":
    subprocess.run([sys.executable, 'tank_main.py'])