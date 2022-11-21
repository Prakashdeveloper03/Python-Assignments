# sourcery skip: replace-interpolation-with-fstring, use-fstring-for-formatting
x, y = input("Enter the string by space separator : ").strip().split()
print("Using comma operator: ", x, y)
print("Using + operator: ", x, y)
print("Using format(): {} {} ".format(x, y))
print("Using modulus operator: %s %s" % (x, y))
print("Using join operator: ", " ".join([x, y]))
print(f"Using f-string: {x}{y}")
