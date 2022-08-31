from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class CarManager:
    def __init__(self):
        self.x = 265
        self.move_x = -5
        self.length_list = 0
        self.new_y = 0
        self.TURTLE_LIST = []

    def create_cars(self):
        self.car_start = random.randint(1, 6)
        self.y = random.randint(-260, 260)
        if self.car_start == 1:
            turtle = Turtle()
            turtle.penup()
            turtle.shape("square")
            turtle.shapesize(1, 2)
            turtle.color(random.choice(COLORS))
            turtle.goto(self.x, self.y)
            self.TURTLE_LIST.append(turtle)
            self.length_list = len(self.TURTLE_LIST)

    def move_car(self):
        for car in range(self.length_list):
            self.TURTLE_LIST[car].forward(self.move_x)

    def accelerate(self):
        self.move_x = self.move_x - 5



