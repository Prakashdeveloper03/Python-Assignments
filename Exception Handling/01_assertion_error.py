def find_smaller(num1: int, num2: int) -> int:
    assert num1 > num2, "First number is not greater than second number"
    return min(num1, num2)


num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))
print(find_smaller(num1, num2))
