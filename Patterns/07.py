num = input("Enter the number : ")
length = len(num)
for i in range(length):
    print(f"{num[i:length]:>{length}}", num[: i + 1], sep="\t")
