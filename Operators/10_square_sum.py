num = int(input("Enter the number : "))
print(
    f"Sum of squares of first {num} natural numbers is {sum(x**2 for x in range(1, num + 1))}"
)
