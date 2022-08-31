#!/usr/bin/env python
"""
# This module include Creating snake using turtle module.
# Moving snake forward and changing snake direction based on the inputs from keyword.
# Function snake_body defines the snake body.
# Function move_snake_fwd responsible for moving the snake and changing its direction.
"""

from turtle import Turtle, Screen

turtle_obj = Turtle()
screen_obj = Screen()
screen_obj.screensize(canvwidth=600, canvheight=600)
screen_obj.bgcolor("black")
screen_obj.title("Snake Game")
screen_obj.listen()
is_game_on = True

# Define snake body
def snake_body():
    x_cordinate = 0
    y_cordinate = 10
    turtle_obj.shape("square")
    turtle_obj.color("white")
    turtle_obj.shapesize(1, 1, 1)
    # Creating turtle of 3times more than original length. Here we will create 3 turtle objects.
    for i in range(0, 4):
        turtle_obj.setx(x_cordinate)
        turtle_obj.sety(y_cordinate)
        turtle_obj.shape("square")
        x_cordinate = x_cordinate + 0
        y_cordinate = y_cordinate + 2
        # print(turtle_obj.shapesize())


# move snake along the screen
def move_snake_fwd():
    turtle_obj.penup()
    turtle_obj.forward(5)
    screen_obj.listen()
    screen_obj.onkey(move_snake_up, "Up")
    turtle_obj.heading()
    screen_obj.onkey(move_snake_down, "Down")
    screen_obj.onkey(move_snake_left, "Left")
    screen_obj.onkey(move_snake_right, "Right")


def move_snake_up():
    turtle_obj.setheading(90)


def move_snake_down():
    turtle_obj.setheading(270)


def move_snake_left():
    turtle_obj.setheading(180)


def move_snake_right():
    turtle_obj.setheading(0)


#while is_game_on:
#    snake_body()
    #move_snake_fwd()

snake_body()

screen_obj.exitonclick()
