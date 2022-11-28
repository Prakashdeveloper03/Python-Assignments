n = int(input("Enter the number of terms : "))
total = 0
for x in range(1, n + 1):
    for y in range(1, x + 1):
        total = total + y
print(f"Sum of the series is {total}")
