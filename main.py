from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
loop_count = 1
while game_is_on:
    car_manager.move_cars()
    time.sleep(0.1)

    # make a new car every second
    loop_count += 1
    if loop_count % 10 == 0:
        car_manager.new_car()

    screen.update()

    # detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False

    # detect finish line
    if player.ycor() == 280:
        car_manager.speed_up()
        scoreboard.update_round()
        player.start_round()

scoreboard.game_over()
screen.exitonclick()
