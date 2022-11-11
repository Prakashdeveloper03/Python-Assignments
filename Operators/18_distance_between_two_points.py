import math

p1 = list(
    map(int, input("Enter the point 1 values by space separator : ").strip().split())
)
p2 = list(
    map(int, input("Enter the point 2 values by space separator : ").strip().split())
)
print(f"\nWith built-in dist function : {math.dist(p1, p2)}\n")
print(
    f"Without built-in dist function : {math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] -p2[1]) ** 2))}"
)
