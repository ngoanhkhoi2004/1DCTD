from turtle import Turtle


class Bullet(Turtle):
    def __init__(self, x, y, dx, dy):
        """
        Initialise the bullet object.

        args:
            x (float): Initial x-coordinate of the bullet.
            y (float): Initial y-coordinate of the bullet.
            dx (float): Movement speed in the x-direction.
            dy (float): Movement speed in the y-direction.
        """
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.speed(0)
        self.goto(x, y)
        self.dx = dx # speed in x-direction
        self.dy = dy # speed in y-direction
        self.active = True

    def move(self):
       if self.active:
            new_x = self.xcor() + self.dx
            new_y = self.ycor() + self.dy
            self.goto(new_x, new_y)

        # check if bullet is out of bound
            if abs(new_x) > 400 or abs(new_y) > 400:
                self.hideturtle()
                self.active = False


