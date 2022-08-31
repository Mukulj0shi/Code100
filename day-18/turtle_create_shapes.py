#!! triangle to nonagone !!
from turtle import Turtle, Screen
import random

Angle = 360
turtle_object = Turtle()
screen_object = Screen()
pen_color = ["royal blue", "yellow", "red", "purple", "green", "brown", "pink"]

for sides in range(3, 11):
    angle = 360/sides
    turtle_object.color(random.choice(pen_color))
    for i in range(1, sides+1):
        turtle_object.forward(100)
        turtle_object.right(angle)


screen_object.exitonclick()


