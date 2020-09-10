#!/usr/bin/env python3

def BottlesOfBeer(number):
    return("{} bottles of beer on the wall, {} bottles of beer. Take one down, pass it around, {} bottles of beer on the wall.".format(number, number, number - 1))


if __name__ == "__main__":
    for i in range(99, 1, -1):
        print(BottlesOfBeer(i), end='')
