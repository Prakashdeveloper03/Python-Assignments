def fibonacci(n: int) -> None:
    a, b = -1, 1
    for _ in range(n):
        c = a + b
        a, b = b, c
        print(c, end=" ")


def recur_fibo(n: int) -> int:
    return n if n <= 1 else (recur_fibo(n - 1) + recur_fibo(n - 2))


n = int(input("Enter the number of terms : "))
if n <= 0:
    print("Plese enter a positive integer")
else:
    print("\nFibonacci series with recursion : ")
    for i in range(n):
        print(recur_fibo(i), end=" ")
    print("\n\nFibonacci series without recursion : ")
    fibonacci(n)
