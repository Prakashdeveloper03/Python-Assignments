s = input("Enter the string : ")
k = int(input("Enter the key value : "))
encrypted = "".join(chr(ord(c) + k) for c in s)
print(f"Encrypted string for {s} is {encrypted}")
