num = input("Enter the number : ")
print(f"Left fill : {num.rjust(10, ' ')}")
print(f"Right fill : {num.ljust(10, ' ')}")
print(f"Center fill : {num.center(10, ' ')}")
