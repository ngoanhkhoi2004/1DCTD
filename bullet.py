import sys
from turtle import Turtle
import screen_manager
import screen


class Bullet(Turtle):
    def __init__(self, x=0, y=0, dx=0, dy=0, source = None, tanks = None):
        """
        Initialise the bullet object.

        args:
            x (float): Initial x-coordinate of the bullet.
            y (float): Initial y-coordinate of the bullet.
            dx (float): Movement speed in the x-direction.
            dy (float): Movement speed in the y-direction.
            source (object): the source tank that fired the bullet.
            tanks (list): A list of all tanks in the game for collision detection.
        """
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.35, stretch_len=0.35)
        self.speed(0)
        self.goto(x, y)
        self.dx = dx # speed in x-direction
        self.dy = dy # speed in y-direction
        self.source = source
        self.tanks = tanks
        self.active = True

    def out_of_bound(self, screen_size=800): # check if screen out of bound
        return abs(self.xcor()) > screen_size or abs(self.ycor()) > screen_size

    def disappear(self):
        self.active = False # mark as inactive when out of bound
        self.hideturtle()

    def move(self):
        if not self.out_of_bound() and self.active:
            self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

            for tank in self.tanks:  # Detect collision
                if tank.alive and tank != self.source and tank.check_collision(self):
                    tank.die()
                    self.disappear()

            screen.ontimer(self.move, 50)  # Schedule next move
        else:
            self.disappear()

if __name__ == '__main__':
    import subprocess
    import sys
    subprocess.run([sys.executable, 'tank_main.py'])
