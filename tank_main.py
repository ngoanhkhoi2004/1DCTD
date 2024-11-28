import turtle
from turtle import *
from tank_control import MainTank
from OppTank import OppTank

# Set up the screen:
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height= 800)
screen.title("Tank Brick Game")


game_on = True



while game_on:
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

    can_shoot = True


    def reset_can_shoot():
        global can_shoot
        can_shoot = True
        return


    def shoot_with_cooldown():
        global can_shoot
        if can_shoot:
            main_tank.shoot()
            can_shoot = False
            screen.ontimer(reset_can_shoot, 1000)
        return


    screen.onkey(shoot_with_cooldown, "space")

    opp_tank = OppTank()
    screen.ontimer(opp_tank.opp_spawn, 3000)
    while not opp_tank.out_of_bound():
        opp_tank.move()
    screen.delay(0.5)
    screen.update()
    screen.mainloop()



