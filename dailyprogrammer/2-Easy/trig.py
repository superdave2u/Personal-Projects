#!/usr/bin/env python3

import math


def sin_from_degrees(degrees):
    return math.sin(math.radians(degrees))


def sin_from_edges(*, opposite, hypotenuse):
    return(opposite / hypotenuse)


def cos_from_degrees(degrees):
    return math.cos(math.radians(degrees))


def cos_from_edges(*, adjacent, hypotenuse):
    return(adjacent / hypotenuse)


def tan_from_degrees(degrees):
    return math.tan(math.radians(degrees))


def tan_from_edges(*, opposite, adjacent):
    return(opposite / adjacent)


def opposite_from_sin(*, sin, hypotenuse):
    return(sin * hypotenuse)


def opposite_from_tan(*, tan, adjacent):
    return(tan * adjacent)


def adjacent_from_cos(*, cos, hypotenuse):
    return(cos * hypotenuse)


def adjacent_from_tan(*, tan, opposite):
    return(tan * opposite)


def hypotenuse_from_sin(*, sin, opposite):
    return(sin * opposite)


def hypotenuse_from_cos(*, cos, adjacent):
    return(cos * adjacent)


def pythagorean(opposite=None, hypotenuse=None, adjacent=None):
    if hypotenuse is not None and opposite is not None:
        adjacent = math.sqrt(hypotenuse * hypotenuse - opposite * opposite)
    elif adjacent is not None and opposite is not None:
        hypotenuse = math.sqrt(adjacent * adjacent + opposite * opposite)
    elif hypotenuse is not None and adjacent is not None:
        opposite = math.sqrt(hypotenuse * hypotenuse - adjacent * adjacent)

    return {'hypotenuse': hypotenuse, 'adjacent': adjacent,
            'opposite': opposite}


if __name__ == "__main__":
    # Testing sin, cos, tan functions.
    print(sin_from_degrees(degrees=35))  # Answer is .57
    print(sin_from_edges(opposite=2.8, hypotenuse=4.9))

    print(cos_from_degrees(degrees=35))  # Answer is .82
    print(cos_from_edges(adjacent=4.0, hypotenuse=4.9))

    print(tan_from_degrees(degrees=35))  # Answer is .70
    print(tan_from_edges(opposite=2.8, adjacent=4.0))

    # Testing find_missing_side function.
    print(hypotenuse_from_sin(sin=sin_from_degrees(degrees=35), opposite=2.8))
    print(adjacent_from_cos(cos=cos_from_degrees(degrees=35), hypotenuse=4.9))
    print(opposite_from_tan(tan=tan_from_degrees(degrees=35), adjacent=4.0))

    # Testing pythagorean function.
    hypotenuse = hypotenuse_from_sin(sin=sin_from_degrees(degrees=35),
                                     opposite=2.8)
    print(pythagorean(opposite=2.8, hypotenuse=4.7))
