from turtle import Turtle


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
        while self.xcor() < 800 and self.ycor() < 800:
            self.goto(self.xcor() + self.x, self.ycor() + self.y)


