#!/usr/bin/env python3

import turtle
import trig

hypotenuse = trig.find_missing_side(sin=trig.sin(degrees=35), opposite=2.8)
total = trig.pythagorean(opposite=2.8, hypotenuse=hypotenuse['hypotenuse'])

print(total)
board = turtle.Turtle()

board.forward(total['adjacent'] * 50)  # draw base

board.left(90)
board.forward(total['opposite'] * 50)

board.left(125)
board.forward(total['hypotenuse'] * 50)

turtle.done()
