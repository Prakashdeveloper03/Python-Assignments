d = {"m1": 85, "m2": 85, "m3": 75, "m4": 100, "m5": 75}
print("Before removing duplicates : {}".format(d))
print(
    "After removing duplicates : {}".format(
        {v: k for k, v in {v: k for k, v in d.items()}.items()}
    )
)
