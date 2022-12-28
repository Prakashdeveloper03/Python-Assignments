s = input("Enter the string : ")
c = input("Enter the character to be searched : ")
f = 0
for x in range(len(s)):
    if s[x] == c:
        print(f"{c} presented at index {x} in {s}")
        f += 1
if f == 0:
    print(f"{c} not presented in {s}")
