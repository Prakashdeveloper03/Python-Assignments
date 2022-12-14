from typing import Tuple


def largest(*args: Tuple[int]) -> int:
    return max(args)


n1, n2, n3 = map(int, input("Enter the numbers by space separation : ").split())
print(f"Largest element among the three values is {largest(n1, n2, n3)}")
