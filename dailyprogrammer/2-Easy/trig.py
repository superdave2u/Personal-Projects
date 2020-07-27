#!/usr/bin/env python3

import math


def sin(*args, **kwargs):
    degrees = kwargs.get('degrees', None)
    opposite = kwargs.get('opposite', None)
    hypotenuse = kwargs.get('hypotenuse', None)

    if degrees:
        return math.sin(math.radians(degrees))
    elif opposite and hypotenuse:
        return(opposite / hypotenuse)


def cos(*args, **kwargs):
    degrees = kwargs.get('degrees', None)
    adjacent = kwargs.get('adjacent', None)
    hypotenuse = kwargs.get('hypotenuse', None)

    if degrees:
        return math.cos(math.radians(degrees))
    elif adjacent and hypotenuse:
        return(adjacent / hypotenuse)


def tan(*args, **kwargs):
    degrees = kwargs.get('degrees', None)
    adjacent = kwargs.get('adjacent', None)
    opposite = kwargs.get('opposite', None)

    if degrees:
        return math.tan(math.radians(degrees))
    elif opposite and adjacent:
        return(opposite / adjacent)


def find_missing_side(*args, **kwargs):
    sin = kwargs.get('sin', None)
    cos = kwargs.get('cos', None)
    tan = kwargs.get('tan', None)
    opposite = kwargs.get('opposite', None)
    hypotenuse = kwargs.get('hypotenuse', None)
    adjacent = kwargs.get('adjacent', None)

    if sin and hypotenuse:
        opposite = sin * hypotenuse
        return {'opposite': opposite}
    elif sin and opposite:
        hypotenuse = opposite / sin
        return {'hypotenuse': hypotenuse}
    elif cos and adjacent:
        hypotenuse = adjacent / cos
        return {'hypotenuse': hypotenuse}
    elif cos and hypotenuse:
        adjacent = cos * hypotenuse
        return {'adjacent': adjacent}
    elif tan and opposite:
        adjacent = opposite / tan
        return {'adjacent': adjacent}
    elif tan and adjacent:
        opposite = tan * adjacent
        return {'opposite': opposite}


def pythagorean(*args, **kwargs):
    opposite = kwargs.get('opposite', None)
    hypotenuse = kwargs.get('hypotenuse', None)
    adjacent = kwargs.get('adjacent', None)

    if hypotenuse and opposite:
        adjacent = math.sqrt(hypotenuse * hypotenuse - opposite * opposite)
    elif adjacent and opposite:
        hypotenuse = math.sqrt(adjacent * adjacent + opposite * opposite)
    elif hypotenuse and adjacent:
        opposite = math.sqrt(hypotenuse * hypotenuse - adjacent * adjacent)

    return {'hypotenuse': hypotenuse, 'adjacent': adjacent,
            'opposite': opposite}


if __name__ == "__main__":
    # Testing sin, cos, tan functions.
    print(sin(degrees=35))  # Answer is .57
    print(sin(opposite=2.8, hypotenuse=4.9))

    print(cos(degrees=35))  # Answer is .82
    print(cos(adjacent=4.0, hypotenuse=4.9))

    print(tan(degrees=35))  # Answer is .70
    print(tan(opposite=2.8, adjacent=4.0))

    # Testing find_missing_side function.
    print(find_missing_side(sin=sin(degrees=35), opposite=2.8))
    print(find_missing_side(cos=cos(degrees=35), hypotenuse=4.9))
    print(find_missing_side(tan=tan(degrees=35), adjacent=4.0))

    # Testing pythagorean function.
    hypotenuse = find_missing_side(sin=sin(degrees=35), opposite=2.8)
    print(pythagorean(opposite=2.8, hypotenuse=hypotenuse['hypotenuse']))
