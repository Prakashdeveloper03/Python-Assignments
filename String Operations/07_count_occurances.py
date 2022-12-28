s = input("Enter the string : ")
c = input("Enter the character to be counted : ")
cnt = sum(s[x] == c for x in range(len(s)))
print(f"No of occurances of {c} in {s} is {cnt}")
