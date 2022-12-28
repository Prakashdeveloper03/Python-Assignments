name = input("Enter your full name : ")
abbreviated = "".join(word[0] for word in name.split())
print(f"\nAbbreviated form for {name} is {abbreviated.upper()}")
