file1, file2 = "files/input.txt", "files/commas.txt"
with open(file1, "r") as f1:
    with open(file2, "w") as f2:
        for line in f1:
            f2.write(line.replace(".", ","))
