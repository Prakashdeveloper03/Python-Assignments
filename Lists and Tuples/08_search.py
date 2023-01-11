l = input("Enter the values by space separation : ").split()
s = input("Enter an alphabet : ")[0]
print(
    f"All the words that starts with `{s}` in the list : {[w for w in l if w.startswith(s)]}"
)
