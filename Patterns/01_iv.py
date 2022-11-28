from math import factorial

n = int(input("Enter the number of terms : "))
x = int(input("Enter the value of x : "))
total = 0
if n == 1:
    print(f"Sum of the series is {n}")
else:
    for i in range(1, n):
        total = (
            total + ((x**i) / factorial(i))
            if i % 2 == 0
            else total - ((x**i) / factorial(i))
        )
    total = 1 - total
    print(f"Sum of the series is {total :.2f}")
