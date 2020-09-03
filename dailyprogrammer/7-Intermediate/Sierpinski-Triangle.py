#!/usr/bin/env python3

import turtle


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


def LeftTriangle(Length):
    # Draw a Left Triangle
    Coords = {}

    # Set the arrow to point East.
    turtle.setheading(0)

    for Count in range(0, 3):
        StartLocation = turtle.pos()

        # Get a bottom left coordinate.
        if Count == 0:
            Coords['BottomLeft'] = StartLocation

        turtle.forward(Length)
        turtle.left(120)
        EndLocation = turtle.pos()

        # Get each side of the Triangle
        if Count == 0:
            Coords['Bottom'] = getMidpoint(StartLocation, EndLocation)
        elif Count == 1:
            Coords['Right'] = getMidpoint(StartLocation, EndLocation)
        elif Count == 2:
            Coords['Left'] = getMidpoint(StartLocation, EndLocation)

    return(Coords)


def Fractol(Depth, Length, StartingPoint):
    if Depth == 0:
        return()
    else:
        MovePen(StartingPoint)
        IGotTheseCoords = LeftTriangle(Length)
        Depth = Depth - 1
        Length = Length * .5
        print("Depth: {}, Length: {}, StartingPoint{}".format(Depth, Length, StartingPoint))
        Fractol(Depth, Length, IGotTheseCoords['BottomLeft'])
        Fractol(Depth, Length, IGotTheseCoords['Bottom'])
        Fractol(Depth, Length, IGotTheseCoords['Left'])


if __name__ == "__main__":

    turtle.color('red', 'yellow')
    turtle.begin_fill()

    Length = 400
    turtle.speed(0)

    Fractol(5, Length, (0, 0))
