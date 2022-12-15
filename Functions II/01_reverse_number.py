from typing import Optional


def reverse(num: int, res: Optional[int] = 0) -> int:
    return res if num == 0 else reverse(num // 10, res * 10 + num % 10)


num = int(input("Enter the number : "))
print(f"Reverse of {num} is {reverse(num)}")
