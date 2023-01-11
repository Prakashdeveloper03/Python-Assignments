s = input("Enter the string : ")
print(f"All consonants in {s} : {[c for c in s if c.lower() not in 'aieou']}")
