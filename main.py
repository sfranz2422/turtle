import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()

car_manager = CarManager()

# setup controls
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()


    if player.ycor() > 280:
        player.return_to_start()
        scoreboard.increase_score()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.distance(player) <20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
