
from turtle import Turtle
import random



COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []





    def creat_cars(self):
        random_car = random.randint(1, 6)
        if random_car == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            car_ypos = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(300, car_ypos)
            self.cars.append(new_car)




    def car_move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)



