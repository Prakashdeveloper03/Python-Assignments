name = input("Enter your name : ")
pan_no = input("Enter your pan number : ")
print(f"If name only contains alphabets : {name.isalpha()}")
print(f"If pan number contains both alphabets & numbers : {pan_no.isalnum()}")
