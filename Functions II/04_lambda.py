def compute(num: int) -> int:
    return 0 if num < 1 else compute(num / 2) + 1


num = int(input("Enter the number : "))
print(f"lambda({num}) -> {compute(num)}")
