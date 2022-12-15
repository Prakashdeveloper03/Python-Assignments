from typing import List, Union


def divisible(m: int, n: int) -> Union[List[int], int]:
    return [x for x in range(1, n + 1) if x % m == 0] if m <= n else 0


m, n = map(int, input("Enter two numbers by space separation : ").split())
print(divisible(m, n))
