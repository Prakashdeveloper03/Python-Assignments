print("Prime numbers between 20 and 1 are : ")
for num in range(20, 0, -1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")
