n, l = 5, []
while n > 0:
    word = input("Enter the word (length >= 6) : ")
    if len(word) >= 6:
        l.append(word)
        n -= 1
    else:
        print("The given word's length is lesser than 6\nTry again...")
print(f"The given words are : {l}")
