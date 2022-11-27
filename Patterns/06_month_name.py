from calendar import month_name
month_number = int(input("Enter the month of the year as an int : "))
if(month_number <= 0 or month_number > 12):
    print("Invalid value...")
else:
    print(f"{month_number} -> {month_name[month_number]}")