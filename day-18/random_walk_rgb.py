from turtle import Turtle, Screen
import turtle
import random

turtle_object = Turtle()
screen_object = Screen()
screen_object.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


angle = [0, 90, 180, 270]
turtle_object.pensize(10)
turtle_object.speed(0)

for i in range(0, 200):
    turtle_object.color(random_color())
    turtle_object.setheading(random.choice(angle))
    turtle_object.forward(30)

screen_object.exitonclick()
