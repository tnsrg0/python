import math


def square(side):
    if side % 1 != 0:
        print(math.ceil(side) * math.ceil(side))
    else:
        print(side * side)


square(4.2)
