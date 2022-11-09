def factorial(num: int) -> int:
    return 1 if num == 1 else num * factorial(num - 1)


num = int(input("Enter the number : "))
print(f"Factorial of {num} is {factorial(num)}")
