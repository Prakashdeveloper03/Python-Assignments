def compute(x: int, y: int) -> int:
    return 1 + compute(x - y, y) if y <= x else 0


x, y = map(int, input("Enter two numbers by space separation : ").split())
print(f"f({x}, {y}) -> {compute(x, y)}")
