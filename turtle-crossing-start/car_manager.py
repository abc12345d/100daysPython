from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self) -> None:
        self.frequency_adding_car = 6
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE
        for _ in range(15):
            self.add_car(-300,300)

    def add_car(self, x_start, x_end):
        '''get the range [x_start,x_end] of x_coordinate to place the new car'''
        
        if random.randint(1,self.frequency_adding_car) == 1:
            color = random.choice(COLORS)
            random_y = random.randint(-250, 250)
            random_x = random.randint(x_start, x_end)

            car = Turtle(shape= "square")
            car.penup()
            car.setheading(180)
            car.goto(x = random_x , y = random_y)
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(color, color)

            self.cars.append(car)
        
    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def increase_move_distance(self):
        self.move_distance += MOVE_INCREMENT

    def increase_frequency_adding_car(self):
        self.frequency_adding_car -= 1

    def is_collision(self, player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False
