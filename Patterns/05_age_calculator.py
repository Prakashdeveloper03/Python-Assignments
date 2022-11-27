from datetime import date
date_of_birth = list(map(int, input("Enter your date of birth in dd/mm/yyyy format : ").strip().split('/')))
date_of_birth = date(date_of_birth[2], date_of_birth[1], date_of_birth[0])
today = date.today()
age = today.year - date_of_birth.year -((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
print(f"Your age from {date_of_birth} - {today} is {age}")