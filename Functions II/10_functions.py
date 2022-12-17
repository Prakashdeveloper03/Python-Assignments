from typing import Tuple, Optional

# Required arguments
def say_name(name: str) -> None:
    print(f"Hello {name}")


# Keyword arguments
def factorial(n: int) -> int:
    return 1 if n == 0 else n * factorial(n - 1)


# Default arguments
def reverse(num: int, res: Optional[int] = 0) -> int:
    return res if num == 0 else reverse(num // 10, res * 10 + num % 10)


# Variable-length arguments
def largest(*args: Tuple[int]) -> int:
    return max(args)


say_name("Siva Prakash")
print(f"Factorial of 5 is {factorial(5)}")
print(f"Reverse of 1234 is {reverse(1234)}")
print(f"Largest number amoung 10, 35, 8 is {largest(10, 35, 8)}")
