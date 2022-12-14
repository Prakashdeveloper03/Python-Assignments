def absolute(num: int) -> int:
    return -num if num < 0 else num


num = int(input("Enter the number : "))
print(f"Absolute value of {num} is {absolute(num)}")
