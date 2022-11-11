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
print("\nEven or odd status for other numbers : ")
if status is not None:
    for x, y in zip(nums, status):
        print(f"{x} is a {y} number")
