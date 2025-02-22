from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance = random.randint(1, 5)
        if chance == 3:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            x_cor = 300
            y_cor = random.randint(-250, 250)
            new_car.goto(x_cor, y_cor)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
