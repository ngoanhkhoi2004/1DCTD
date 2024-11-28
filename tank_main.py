import turtle
from turtle import *
from tank_control import MainTank

# Set up the screen:
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height= 800)
screen.title("Tank Brick Game")
screen.tracer(0)

# set up tank
main_tank = MainTank()
main_tank.spawn()

#listen for tank controls
screen.listen()
screen.onkeypress(main_tank.move_right, "Right")
screen.onkeypress(main_tank.move_up, "Up")
screen.onkeypress(main_tank.move_down, "Down")
screen.onkeypress(main_tank.move_left, "Left")
screen.onkey(main_tank.shoot, "space") # shoot with space bar

def game_loop():
    screen.delay(0.6)
    screen.update()
    screen.ontimer(game_loop, 20)

game_loop()
screen.mainloop()



