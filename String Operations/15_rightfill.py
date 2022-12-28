num = input("Enter the number : ")
width = int(input("Enter the width : "))
print(
    f"{num} with * on the right of specified width {width} is {num.ljust(width, '*')}"
)
