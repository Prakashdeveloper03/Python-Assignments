def is_leap_year(year: int) -> None:
    if (year % 400 == 0) and (year % 100 == 0):
        print(f"{year} is a leap year")
    elif (year % 4 == 0) and (year % 100 != 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


year = int(input("Enter a year : "))
is_leap_year(year)
