n = 5
for m, i in enumerate(range(1, 6), start=1):
    for j in range(1, 6):
        if i == j:
            print("$", end="  ")
        elif i == m and j == n:
            print("$", end="  ")
        elif i > 1 and i < 5 and j >= 2 and j <= 4:
            print(" ", end="  ")
        else:
            print("*", end="  ")
    n -= 1
    print()
