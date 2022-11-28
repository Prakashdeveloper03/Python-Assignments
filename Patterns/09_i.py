for i in range(1, 6):
    for j in range(1, 6):
        if (i > 1 and i < 5) and j >= 2 and j <= 4:
            print(" ", end="  ")
        else:
            print("*", end="  ")
    print()
