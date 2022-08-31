from turtle import Turtle, Screen
import random

turtle_object = Turtle()
screen_object = Screen()
turtle_object.speed(0)
screen_object.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def spirograph(angle_move):
    for i in range (int(360/angle_move)):
        current_position = turtle_object.heading()
        turtle_object.color(random_color())
        turtle_object.circle(100)
        turtle_object.setheading(angle_move + current_position)

spirograph(2)


screen_object.exitonclick()
