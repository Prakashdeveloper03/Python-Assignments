s = input("Enter the string : ")
words = input("Enter the set of characters to be stripped : ")
print(f"Before stripping : {s}")
res = [c for c in s if c not in words]
print(f"After stripping : {''.join(res)}")
