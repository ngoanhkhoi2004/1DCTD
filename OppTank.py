from turtle import Turtle
import random
from bullet import Bullet

directions = ["up", "down", "right", "left"]
class OppTank(Turtle):
    def __init__(self):
        super().__init__()
        self.direction = directions[random.randint(0,3)]
        self.alive = True
        self.body = []
        self.dx = random.randint(-350, 350)
        self.dy = random.randint(-350, 350)
        self.bullet_speed = 17

    def opp_spawn(self):
        for _ in range(4):
            square = Turtle()
            square.penup()
            square.setposition(self.dx, self.dy)
            square.shape("square")
            square.color("white")
            self.body.append(square)
        if self.direction == "up":
            self.body[1].goto(self.body[0].xcor(), self.body[0].ycor()+22)
            self.body[2].goto(self.body[0].xcor()-22, self.body[0].ycor())
            self.body[3].goto(self.body[0].xcor()+22, self.body[0].ycor())
        elif self.direction == "down":
            self.body[1].goto(self.body[0].xcor(), self.body[0].ycor()-22)
            self.body[2].goto(self.body[0].xcor()-22, self.body[0].ycor())
            self.body[3].goto(self.body[0].xcor()+22, self.body[0].ycor())
        else:
            self.body[1].goto(self.body[0].xcor() , self.body[0].ycor()-22)
            self.body[2].goto(self.body[0].xcor(), self.body[0].ycor()+22)
            if self.direction == "right":
                self.body[3].goto(self.body[0].xcor() + 22, self.body[0].ycor())
            elif self.direction == "left":
                self.body[3].goto(self.body[0].xcor() - 22, self.body[0].ycor())

    def die(self):
        self.alive = False
        for square in self.body:
            square.hideturtle()
            square.clear()
        self.body.clear()

    def opp_tank_move(self):
        if self.direction == "up":
            for square in self.body:
                square.goto(square.xcor(), square.ycor()+11)
        elif self.direction == "down":
            for square in self.body:
                square.goto(square.xcor(), square.ycor()-11)
        elif self.direction == "right":
            for square in self.body:
                square.goto(square.xcor()+11, square.ycor())
        elif self.direction == "left":
            for square in self.body:
                square.goto(square.xcor()-11, square.ycor())

    def opp_shoot(self, tanks):
        bullet = Bullet("opp_tank", tanks, [self.body[0].xcor(), self.body[0].ycor()])
        data = {"up": [0, self.bullet_speed], "down": [0, -self.bullet_speed], "left": [-self.bullet_speed, 0], "right": [self.bullet_speed, 0]}
        bullet.x = data[self.direction][0]
        bullet.y = data[self.direction][1]
        bullet.move()

    def out_of_bound(self, screen_size=350):
        return abs(self.body[0].xcor()) > screen_size or abs(self.body[0].ycor()) > screen_size

    def check_collision(self, bullet):

        if bullet.source == "opp_tank":
            return False
        for square in self.body:
            if bullet.distance(square) < 15:
                return True
        return False
