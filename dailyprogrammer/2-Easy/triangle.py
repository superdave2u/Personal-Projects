#!/usr/bin/env python3

import turtle
import trig

hypotenuse = trig.find_missing_side(sin=trig.sin(degrees=35), opposite=2.8)
total = trig.pythagorean(opposite=2.8, hypotenuse=hypotenuse['hypotenuse'])

print(total)
board = turtle.Turtle()

board.forward(total['hypotenuse'])  # draw base

board.left(90)
board.forward(total['opposite'])

board.left(135)
board.forward(total['adjacent'])

turtle.done()
