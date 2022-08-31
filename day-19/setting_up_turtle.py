from turtle import Turtle, Screen
import random
from color_name import convert_rgb_to_names

is_race_on = False
screen_obj = Screen()
screen_obj.setup(height=400, width=500)
screen_obj.colormode(255)
y_axis = -150
list_obj = []
turtle_color_list = []

# Creating 5 turtle objects from the Turtle class.
for i in range(1, 6):
    turtle_obj = Turtle()
    list_obj.append(turtle_obj)
    turtle_obj.shape("turtle")
    # 3 set of random numbers from 1 to 255 represent r,g,b scale.
    turtle_obj.color(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
    turtle_color_list.append(convert_rgb_to_names(turtle_obj.pencolor()))
    turtle_obj.penup()
    turtle_obj.goto(-240, y_axis)
    y_axis = y_axis + 70

# print (turtle_color_list)
# print(list_obj)

user_bet = screen_obj.textinput(title="Enter race", prompt=f"Which color turtle you want to bet on {turtle_color_list}")
print(user_bet)

if user_bet:
    is_race_on = True


# Moving turtle
def move_object(turtle_obj1):
    turtle_obj1.speed(0)
    turtle_obj1.forward(10)


# Selecting one turtle object from list of Turtle objects and moving it forward.
while is_race_on:
    turtle_fwd = random.choice(list_obj)
    #print(turtle_fwd.pencolor())
    turtle_position = turtle_fwd.pos()
    move_object(turtle_fwd)
    if turtle_position[0] >= 230.00:
        is_race_on = False
        if user_bet == convert_rgb_to_names(turtle_fwd.pencolor()):
            print(f"Hurrah you won the bet !! your {convert_rgb_to_names(turtle_fwd.pencolor())} turtle won the race")
        else:
            print(f"Sorry you lost.{convert_rgb_to_names(turtle_fwd.pencolor())} turtle won the race")

screen_obj.exitonclick()
