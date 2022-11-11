def factorial(num: int) -> (int | None):
    if num < 0:
        return None
    elif num == 0:
        return 1
    else:
        return num * factorial(num - 1)


num = int(input("Enter the number : "))
print(f"Factorial of {num} is {factorial(num)}")
