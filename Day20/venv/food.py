from turtle import Turtle, Screen
import random


class SnakeFood(Turtle):  # Turtle is superclass
    def __init__(self):  # Create initializer, class destructor.
        super().__init__()  # Class SnakeFood has inherited Turtle class.
        # No need to define objects separately as we have inherited Turtle class
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.move_food()

    def move_food(self):
        x_cord = random.randint(-280, 280)
        y_cord = random.randint(-280, 280)
        self.goto(x_cord, y_cord)

# snake = SnakeFood()
# snake.food_location()
# screen = Screen()
# screen.exitonclick()
