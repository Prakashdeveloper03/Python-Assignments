consumption = int(input("Enter Your consumption units : "))
if consumption >= 0 and consumption <= 150:
    print(f"Your electricity bill is {consumption * 3}")
elif consumption >= 151 and consumption <= 350:
    print(f"Your electricity bill is {100 + (consumption * 3.75)}")
elif consumption >= 351 and consumption <= 450:
    print(f"Your electricity bill is {250 + (consumption * 4)}")
elif consumption >= 451 and consumption <= 600:
    print(f"Your electricity bill is {300 + (consumption * 4.25)}")
else:
    print(f"Your electricity bill is {400 + (consumption * 5)}")
