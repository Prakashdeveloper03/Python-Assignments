num = int(input("Enter the number : "))
print(
    f"Sum of cubes of first {num} natural numbers is {sum(x**3 for x in range(1, num + 1))}"
)
