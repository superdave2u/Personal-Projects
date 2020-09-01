import time
import math
import turtle
import random

FRACTAL_DEPTH = 6 # <=8 Exponential increase in draw time!

MAJOR_TRIANGLE_SIZE = 600 # <= 600 to fit in window

# Center the major triangle on the screen
START_POSITION = (0 - MAJOR_TRIANGLE_SIZE/2,
                  0 - MAJOR_TRIANGLE_SIZE/2)

TURTLE_SPEED = 0
HIDE_TURTLE = True

# Defining vars for easier usage of coordinates
X = 0
Y = 1

def draw_triangle(leg_length, start_point, color):
  turtle.setheading(0)
  turtle.setposition(start_point)
  turtle.fillcolor(color)
  turtle.begin_fill()
  for _ in range(3):
    turtle.forward(leg_length)
    turtle.left(120)
  turtle.end_fill()
  
def get_left_midpoint(leg_length, start_point):
  SIXTY_DEGREE_IN_RADIAN = math.radians(60)
  return (start_point[X] + (leg_length/2) * math.cos(SIXTY_DEGREE_IN_RADIAN),
          start_point[Y] + (leg_length/2) * math.sin(SIXTY_DEGREE_IN_RADIAN))

def get_bottom_midpoint(leg_length, start_point):
  return (start_point[X] + (leg_length / 2), start_point[Y])

def draw_fractal(depth, leg_length, start_point, colors):
  draw_triangle(leg_length, start_point, colors[depth])
  if depth != 1:    
    left_leg_midpoint   = get_left_midpoint(leg_length, start_point)
    bottom_leg_midpoint = get_bottom_midpoint(leg_length, start_point)

    next_level = depth - 1
    next_length = leg_length / 2
    draw_fractal(next_level, next_length, start_point, colors)
    draw_fractal(next_level, next_length, left_leg_midpoint, colors)
    draw_fractal(next_level, next_length, bottom_leg_midpoint, colors)

def get_random_color():
  r = lambda: random.randint(0,255)
  return('#%02X%02X%02X' % (r(),r(),r()))

def prepare_color_stack(count):
  stack = ['DEPTH_NOT_0_INDEXED']
  for _ in range(count):
    stack.append(get_random_color())
  return stack

COLOR_STACK = prepare_color_stack(FRACTAL_DEPTH)

if HIDE_TURTLE: 
  turtle.hideturtle()

turtle.penup()
turtle.speed(TURTLE_SPEED)
start_time = time.time()
draw_fractal(FRACTAL_DEPTH, MAJOR_TRIANGLE_SIZE, START_POSITION, COLOR_STACK)
draw_time = time.time() - start_time

print("--- Drawing took %s seconds ---" % draw_time)

turtle.done()