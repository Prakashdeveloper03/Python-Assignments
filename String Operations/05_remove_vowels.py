s = input("Enter the string : ")
print(f"Before removing vowels : {s}")
s = "".join([c for c in s if c.lower() not in ["a", "e", "o", "i", "u"]])
print(f"After removing vowels : {s}")
