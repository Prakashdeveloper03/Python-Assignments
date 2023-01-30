with open("files/print.txt", "r") as file:
    for line in file:
        if "print" in line:
            print(line)
