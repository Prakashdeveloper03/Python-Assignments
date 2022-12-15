from typing import Callable

product: Callable[[int, int], int] = lambda a, b: a * b

n1, n2 = map(int, input("Enter two numbers by space separation : ").split())
print(f"{n1} x {n2} = {product(n1, n2)}")
