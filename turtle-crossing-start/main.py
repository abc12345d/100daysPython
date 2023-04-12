import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def increase_difficulty(scoreboard, car_manager, player):
        scoreboard.increase_level()
        car_manager.increase_move_distance()
        car_manager.increase_frequency_adding_car()
        player.restart()

# setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# setup player
player = Player()

# setup scoreboard
scoreboard = Scoreboard()

# setup car
car_manager = CarManager()

screen.listen()
screen.onkey(fun = player.go_up, key = "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.move()
    car_manager.add_car(x_start=300,x_end=300)

    if player.is_reach():
          increase_difficulty(scoreboard, car_manager, player)

    if car_manager.is_collision(player):
          scoreboard.game_over()
          game_is_on = False
    
    if scoreboard.level == 6:
          scoreboard.congratulation()
          game_is_on = False

screen.exitonclick()