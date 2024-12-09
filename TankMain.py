from Screen import screen
from PlayerTank import MainTank
from OppTank import OppTank
from turtle import Turtle

score = 0

# Create a Turtle object for displaying the score
score_display = Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(0, 300)  # Adjust the position as needed
score_display.color("white")
score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

def update_score_display():
    score_display.clear()
    score_display.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))

main_tank = MainTank()
main_tank.spawn(main_tank.body)
opponents_list = []

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


def shoot_with_cooldown():
    global can_shoot
    if can_shoot:
        main_tank.shoot(opponents_list)
        can_shoot = False
        screen.ontimer(reset_can_shoot, 1000)


screen.onkey(shoot_with_cooldown, "space")

def move_opponent(opp_tank):
    global score
    if opp_tank.alive and not opp_tank.out_of_bound():
        opp_tank.opp_tank_move()
        opp_tank.opp_shoot([main_tank])# Move the tank once
        # Schedule the next move in 500ms
        screen.ontimer(lambda: move_opponent(opp_tank), 500)
    else:
        opp_tank.die()
        score += 1
        update_score_display()

        if opp_tank in opponents_list:
            score -= 1
            update_score_display()
            opponents_list.remove(opp_tank)


def spawn_opponent():
    if len(opponents_list) < 6:
        opp_tank = OppTank()
        opp_tank.opp_spawn()
        opponents_list.append(opp_tank)
        move_opponent(opp_tank)
        screen.ontimer(spawn_opponent, 3500)

def check_main_tank_alive():
    if not main_tank.alive:
        screen.bye()
        # Exit the game if the main tank is dead
    else:
        screen.ontimer(check_main_tank_alive, 100)
        # Check every 100ms

# Start the alive-checking loop
check_main_tank_alive()
screen.ontimer(spawn_opponent, 2000)

screen.delay(0.4)
screen.update()
screen.mainloop()
