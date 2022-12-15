from typing import Callable

cube: Callable[[int], int] = lambda x: x**3
square: Callable[[int], int] = lambda x: x**2

num = int(input("Enter the number : "))
print(f"Square of {num} is {square(num)}")
print(f"Cube of {square(num)} is {cube(square(num))}")
