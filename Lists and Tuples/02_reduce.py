from functools import reduce

print(
    f"The sum of first 10 natural numbers is {reduce(lambda x, y : x + y, range(1, 11))}"
)
