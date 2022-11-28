n, l = 5, []
while n > 0:
    word = input("Enter the word : ")
    if len(word) >= 6:
        l.append(word)
        n -= 1
    else:
        print("The given word's lenght is lesser than 6\nTry again...")
print(f"The given words are : {l}")
