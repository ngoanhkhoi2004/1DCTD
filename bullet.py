from turtle import Turtle


class Bullet(Turtle):
    def init(self):
        super().init()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)
        self.x = 0
        self.y = 0
        self.speed = 0.5

    def move(self):
        while self.xcor() < 800 and self.ycor() < 800:
         self.goto(self.xcor() + self.x, self.ycor() + self.y)

    def out_of_bound(self, screen_size=400):
        # check if bullet is out of bound
        return abs(self.xcor()) > screen_size or abs(self.ycor()) > screen_size


