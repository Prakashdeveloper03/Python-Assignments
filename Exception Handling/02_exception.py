import math


def find_square_root(num: int) -> float:
    if num < 0:
        raise ValueError("Cannot find square root of a negative number")
    return math.sqrt(num)


num = int(input("Enter the number : "))
print(find_square_root(num))
