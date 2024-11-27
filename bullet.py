from turtle import Turtle

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.3, stretch_len=0.3)


    def move(self):
        print('h')

