print([f"{str(x)}a" for x in range(1, 5)])
print([x + y for x in "ab" for y in "bcd"])
print(([x + y for x in "ab" for y in "bcd"])[::2])
print([x * 10 for x in range(1, 11)])
