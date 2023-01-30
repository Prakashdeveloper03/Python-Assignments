file1, file2 = "files/input.txt", "files/reverse.txt"
with open(file1, "r") as f1:
    with open(file2, "w") as f2:
        f2.write(f1.read()[::-1])
