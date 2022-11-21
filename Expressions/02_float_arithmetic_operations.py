n1 = input("Enter the number 1 : ")
n2 = input("Enter the number 2 : ")
operators = ["+", "-", "*", "/", "//", "**"]
for x in operators:
    print(f"{n1} {x} {n2} = {eval(n1 + x + n2)}")
