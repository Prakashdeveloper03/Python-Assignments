n = int(input("Enter the number of terms : "))
l = [(x**2) / x for x in range(1, n + 1)]
print(f"Sum of the series is {sum(l)}")
