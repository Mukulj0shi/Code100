#!/usr/bin/env python

"""
# This module include Creating snake using turtle module.
# Moving snake forward and changing snake direction based on the inputs from keyword.
# Function snake_body defines the snake body.
# Function move_snake_fwd responsible for moving the snake and changing its direction.
"""

from turtle import Turtle, Screen
import time
from create_snakev2 import Snake
from food import SnakeFood
from score import Score

# turtle_obj1 = Turtle()
screen_obj = Screen()
screen_obj.tracer(0)
screen_obj.screensize(canvwidth=600, canvheight=600)
screen_obj.bgcolor("black")
screen_obj.title("Snake Game")  # Represent title of the screen.
screen_obj.listen()
snake = Snake()  # This will create the snake object and snake will appear in screen.
# This is because snake is defined in __init__ method
snake_food_obj = SnakeFood()
score_obj = Score()

screen_obj.onkey(snake.up, "Up")
screen_obj.onkey(snake.down, "Down")
screen_obj.onkey(snake.right, "Right")
screen_obj.onkey(snake.left, "Left")
is_game_on = True

while is_game_on:
    screen_obj.update()
    time.sleep(0.1)
    snake.move_snake()
    # snake.endgame()
    #print(snake.head.position()[1])
    if snake.endgame():                         #If snake endgame() conditions are true then stop game.
        print("Game ends")
        is_game_on = False
    else:
        print("Game Continues")
        if snake.head.distance(snake_food_obj) < 15:
            snake_food_obj.move_food()
            snake.addtail()
            score_obj.new_score()


score_obj.final_score()
screen_obj.exitonclick()
