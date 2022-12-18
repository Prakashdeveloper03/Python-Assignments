def is_prime(num: int) -> int:
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return 0
    return 1


num = int(input("Enter the number : "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
