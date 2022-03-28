# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 12:38:30 2021

@author: Aditya
"""

import arcade
import random

SCREEN_WIDTH = 600

SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

x = 300

y = 300

radius = 200

arcade.draw_circle_filled(x, y, radius, arcade.color.YELLOW)

x = 370

y = 350

radius = 20

arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 230

y = 350

radius = 20

arcade.draw_circle_filled(x, y, radius, arcade.color.BLACK)

x = 300

y = 280

width = 120

height = 100

start_angle = 360

end_angle = 190

arcade.draw_arc_outline(x, y, width, height, arcade.color.BLACK, start_angle, end_angle, 10)

arcade.finish_render()

arcade.run()