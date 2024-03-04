import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manage = CarManager()

screen.listen()
screen.onkey(player.move, "Up")
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manage.create_cars()
    car_manage.move_car()

    for car in car_manage.cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.finish():
        player.go_to_start()
        car_manage.level_up()
        score.increase_level()

screen.exitonclick()
