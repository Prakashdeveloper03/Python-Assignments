flag = True
nums = []
while flag:
    num = int(input("Enter the number : "))
    match num:
        case -1:
            flag = False
        case _:
            nums.append(num)
status = ["even" if x % 2 == 0 else "odd" for x in nums]
print(f"There are {status.count('even')} even numbers and {status.count('odd')} odd numbers")
