def swap(a: int, b: int) -> None:
    global n1, n2
    n1, n2 = b, a


n1, n2 = map(int, input("Enter the numbers by space separation : ").split())
print(f"\nBefore swapping :\nn1 = {n1} n2 = {n2}\n")
swap(n1, n2)
print(f"After swapping :\nn1 = {n1} n2 = {n2}")
