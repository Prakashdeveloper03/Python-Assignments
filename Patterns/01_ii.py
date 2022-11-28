n = int(input("Enter the number of terms : "))
x = int(input("Enter the value of x : "))
total = 0
for i in range(1, n + 1):
    total = total + (x**i) if (i % 2 == 0) else +(-(x**i))
print(f"Sum of the series is {total}")
