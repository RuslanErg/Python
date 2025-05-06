import math


def square(side):
    area = side ** 2
    if not isinstance(side, int):
        return math.ceil(area)
    return area


print(square(33))
print(square(8.28))
