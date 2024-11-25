import turtle
from turtle import *
from tank_control import MainTank

# Set up the screen:
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height= 800)
screen.title("Tank Brick Game")


game_on = True

main_tank = MainTank()

main_tank.spawn()

screen.listen()
screen.onkey(main_tank.turn_right, "Right")
screen.onkey(main_tank.turn_left, "Left")
screen.onkey(main_tank.turn_up, "Up")
screen.onkey(main_tank.turn_down, "Down")
screen.onkeypress(main_tank.move, "Right")
screen.onkeypress(main_tank.move, "Up")
screen.onkeypress(main_tank.move, "Down")
screen.onkeypress(main_tank.move, "Left")
screen.delay(0.6)
screen.update()
screen.mainloop()

while game_on:
    pass


