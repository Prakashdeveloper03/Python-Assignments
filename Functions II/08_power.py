from typing import Union


def power(x: int, y: int) -> Union[int, float]:
    return x**y


x, y = map(int, input("Enter two numbers by space separation : ").split())
print(f"{x} ** {y} = {power(x, y)}")
