#!/usr/bin/env python

"""
# This module creates a turtle crossing game.
# Move turtle forward using the player class.
# Cars move continously using carmanager class.
# Each time turtle crosses the road then new level will start.
# Turtle is moved forward using onkey method.
# Page is refreshed using screen.update() method.
"""

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
carmanager = CarManager()
player = Player()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")
player.create_turtle()

#Create first car

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_cars()
    #Make cars move in the screen
    carmanager.move_car()
    #Reset turtle when road is crossed
    if player.crossed():
        player.crossed()
        carmanager.accelerate()
    for car in carmanager.TURTLE_LIST:
        if car.distance(player) < 20:
            player.gameover()
            game_is_on = False


screen.exitonclick()
