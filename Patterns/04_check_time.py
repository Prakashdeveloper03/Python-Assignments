from datetime import datetime

print("Enter Time in 24 hr in HH:MM format")
entry_time = input("Enter vehicle entry time : ")
leave_time = input("Enter vehicle leaving time : ")
duration = datetime.strptime(leave_time, "%H:%M") - datetime.strptime(
    entry_time, "%H:%M"
)
hours = abs(duration.total_seconds() // (60 * 60))
print(
    "\nChoose Type of Vehicle\n1. Truck / Bus\n2. Car\n3. Cycle / Motor Cycle / Scooter"
)
choose = int(input("Enter Your Choice : "))
amount = 0
match choose:
    case 1:
        amount = 20 if hours <= 3 else 30
    case 2:
        amount = 10 if hours <= 3 else 20
    case 3:
        amount = 5 if hours <= 3 else 10
    case _:
        print("\nInvalid Choice...")
print(f"You have to pay {amount}")
