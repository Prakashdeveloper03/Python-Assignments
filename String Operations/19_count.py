string = input("Enter the string : ")
digits, uppers, lowers, special = 0, 0, 0, 0
for ch in string:
    if ch.isupper():
        uppers += 1
    elif ch.islower():
        lowers += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1
print(f"Total no of uppercase letters are {uppers}")
print(f"Total no of lowercase letters are {lowers}")
print(f"Total no of digits are {digits}")
print(f"Total no of special characters are {special}")
