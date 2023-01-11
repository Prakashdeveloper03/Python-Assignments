l = list(map(int, input("Enter the values by space separation : ").split()))
print(
    f"Filter out only even numbers from the given list : {list(filter(lambda x: x % 2 == 0, l))}"
)
