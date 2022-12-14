def is_prime(num: int) -> str:
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
    return "0" if flag else "1"


num = int(input("Enter the number : "))
if is_prime(num) == "1":
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
