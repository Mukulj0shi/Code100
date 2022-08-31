from turtle import Turtle, Screen
import spot_color
import random

turtle_object = Turtle()
screen_object = Screen()
screen_object.colormode(255)
colors = spot_color.color_list
turtle_object.speed(0)
turtle_object.hideturtle()
turtle_object.penup()
turtle_object.setheading(230)
turtle_object.forward(190)
turtle_object.setheading(0)


for line in range(1, 100+1):
    #turtle_object.showturtle()
    turtle_object.pendown()
    turtle_object.dot(20, random.choice(colors))
    turtle_object.penup()
    turtle_object.forward(50)
    if line % 10 == 0:
        #turtle_object.hideturtle()
        turtle_object.left(90)
        turtle_object.forward(50)
        turtle_object.right(90)
        turtle_object.backward(500)

screen_object.exitonclick()

