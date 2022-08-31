from turtle import Turtle, Screen
import spot_color
import random

turtle_object = Turtle()
screen_object = Screen()
screen_object.colormode(255)
colors = spot_color.color_list
print(colors)


def print_line():
    for i in range(10):
        turtle_object.showturtle()
        turtle_object.pendown()
        turtle_object.dot(20, colors[random.randint(0, len(colors)-1)])
        turtle_object.penup()
        turtle_object.forward(50)


def go_back():
    turtle_object.hideturtle()
    turtle_object.left(90)
    turtle_object.forward(50)
    turtle_object.right(90)
    turtle_object.backward(500)


for i in range(10):
    print_line()
    go_back()

screen_object.exitonclick()
