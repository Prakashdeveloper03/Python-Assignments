principle_amt = int(input("Enter the principal amount : "))
time_period = int(input("Enter the time period : "))
rate_of_interest = int(input("Enter the rate of interest : "))
print(
    f"The Compound Interest is {(principle_amt * (pow((1 + rate_of_interest / 100), time_period))) - principle_amt :.2f}"
)
