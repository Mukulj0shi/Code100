from turtle import Turtle, Screen
import random

turtle_object = Turtle()
screen_object = Screen()

angle = [0, 90, 180, 270]
pen_color = ["royal blue", "yellow", "red", "purple", "green", "brown", "pink"]
turtle_object.pensize(10)
turtle_object.speed(0)

for i in range(0, 200):
    turtle_object.color(random.choice(pen_color))
    turtle_object.setheading(random.choice(angle))
    turtle_object.forward(30)

screen_object.exitonclick()


