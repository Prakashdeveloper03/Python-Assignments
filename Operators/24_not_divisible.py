# every number divisible by 2 is also divisible by 4
not_divisible = [x for x in range(1, 101) if x % 2 != 0]
print("Numbers between 1 and 100 that are not divisible by 2 and 4 : ")
for num in not_divisible:
    print(num, end=" ")
