file1, file2 = "files/origin.txt", "files/destination.txt"
with open(file1, "r") as f1, open(file2, "r") as f2:
    file1_contents = f1.read()
    file2_contents = f2.read()

with open(file1, "w") as f1, open(file2, "w") as f2:
    f1.write(file2_contents)
    f2.write(file1_contents)
