from screen_manager import screen
from tank_control import MainTank
from OppTank import OppTank

main_tank = MainTank()
main_tank.spawn()

opponents_list = []

# Set up controls
screen.listen()
screen.onkey(main_tank.turn_up, "Up")
screen.onkey(main_tank.turn_down, "Down")
screen.onkey(main_tank.turn_left, "Left")
screen.onkey(main_tank.turn_right, "Right")
screen.onkey(lambda: main_tank.shoot(opponents_list), "space")

def spawn_opponent():
    if len(opponents_list) < 5:
        opp_tank = OppTank()
        opp_tank.spawn()
        opponents_list.append(opp_tank)
        screen.ontimer(lambda: move_opponent(opp_tank), 500)
    screen.ontimer(spawn_opponent, 3500)

def move_opponent(opp_tank):
    if opp_tank.alive:
        opp_tank.move()
        opp_tank.shoot([main_tank])
        screen.ontimer(lambda: move_opponent(opp_tank), 500)

def check_game_over():
    if not main_tank.alive:
        screen.bye()
    else:
        screen.ontimer(check_game_over, 100)

# Start game
check_game_over()
spawn_opponent()
screen.mainloop()