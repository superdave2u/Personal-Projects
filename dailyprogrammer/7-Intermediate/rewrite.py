#!/usr/bin/env python3

import turtle
from collections import deque
import time


def getMidpoint(StartCoordinate, EndCoordinate):
    # Midpoint Formula
    x = (StartCoordinate[0] + EndCoordinate[0]) / 2
    y = (StartCoordinate[1] + EndCoordinate[1]) / 2

    return((x, y))


def MovePen(position):
    # Move Pen to New location without drawing
    turtle.penup()
    turtle.setposition(position)
    turtle.pendown()


def RightTriangle(Length):
    Coords = []

    turtle.setheading(120)

    for _ in range(3):
        StartLocation = turtle.pos()
        turtle.forward(Length)
        turtle.left(120)
        EndLocation = turtle.pos()
        Coords.append(getMidpoint(StartLocation, EndLocation))

    return(tuple(Coords))


def LeftTriangle(Length):
    # count = 0
    Coords = {}

    turtle.setheading(0)

    for Count in range(0, 3):
        StartLocation = turtle.pos()
        turtle.forward(Length)
        turtle.left(120)
        EndLocation = turtle.pos()
        if Count == 0:
            Coords['Bottom'] = getMidpoint(StartLocation, EndLocation)
        elif Count == 1:
            Coords['Right'] = getMidpoint(StartLocation, EndLocation)
        elif Count == 2:
            Coords['Left'] = getMidpoint(StartLocation, EndLocation)

    return(Coords)


def LeftTriangleNoDraw(Length):
    # count = 0
    Coords = {}

    turtle.setheading(0)
    turtle.penup()
    for Count in range(0, 3):
        StartLocation = turtle.pos()
        turtle.forward(Length)
        turtle.left(120)
        EndLocation = turtle.pos()
        if Count == 0:
            Coords['Bottom'] = getMidpoint(StartLocation, EndLocation)
        elif Count == 1:
            Coords['Right'] = getMidpoint(StartLocation, EndLocation)
        elif Count == 2:
            Coords['Left'] = getMidpoint(StartLocation, EndLocation)

    return(Coords)


def TopTriangle(Length):
    Coords = []

    turtle.setheading(240)

    for _ in range(3):
        StartLocation = turtle.pos()
        turtle.forward(Length)
        turtle.left(120)
        EndLocation = turtle.pos()
        Coords.append(getMidpoint(StartLocation, EndLocation))

    return(tuple(Coords))


def InvertedTriangle(Length):
    Coords = {}

    turtle.setheading(60)

    for Count in range(3):
        StartLocation = turtle.pos()
        turtle.forward(Length)
        turtle.left(120)
        EndLocation = turtle.pos()
        if Count == 0:
            Coords['Right'] = getMidpoint(StartLocation, EndLocation)
        elif Count == 1:
            Coords['Top'] = getMidpoint(StartLocation, EndLocation)
        elif Count == 2:
            Coords['Left'] = getMidpoint(StartLocation, EndLocation)

    return(Coords)


def Fractol(Depth, Length, StartingPoint):
    if Depth == 0:
        MovePen(StartingPoint)
        LeftTriangle(Length)
    else:
        IGotTheseCoords = LeftTriangleNoDraw(Length)
        # MovePen(StartingPoint)
        # IGotTheseCoords = InvertedTriangle(Length)
        Depth = Depth - 1
        Length = Length * .5
        # print(StartingPoint)
        # Fractol(Depth, Length, IGotTheseCoords['Right'])
        Fractol(Depth, Length, IGotTheseCoords['Bottom'])
        Fractol(Depth, Length, IGotTheseCoords['Left'])



turtle.color('red', 'yellow')
turtle.begin_fill()

storage = []
AllCoordinates = deque()

Length = 200
turtle.speed(0)

Fractol(5, 200, (0, 0))
time.sleep(5)


# AllCoordinates.append(LeftTriangle(Length))
# print(AllCoordinates)
# for lst in AllCoordinates:
#     MovePen(lst[0])
#     AllCoordinates.append(RightTriangle(100))
#     MovePen(lst[1])
#     AllCoordinates.append(TopTriangle(100))
#     MovePen(lst[2])
#     AllCoordinates.append(LeftTriangle(100))

