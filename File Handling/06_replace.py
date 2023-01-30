text = "hello world. this is a test 1.2.3.4"
file_name = "files/replace.txt"
with open(file_name, "w") as f:
    for i, char in enumerate(text):
        if char == ".":
            f.write(char)
            f.write(text[i + 1].upper())
            i += 1
        elif char.isdigit():
            f.write(f"({char})")
        else:
            f.write(char)
