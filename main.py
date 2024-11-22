import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    #Detect collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            score.game_over()

    #If turtle clears a level, reset and speed the cars
    if player.ycor() > 270:
        score.update_level()
        player.reset()
        car.increase_speed()

screen.exitonclick()
