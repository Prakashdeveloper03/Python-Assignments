def compound_interest(
    principle_amt: int, time_period: int, rate_of_interest: int
) -> float:
    return (
        principle_amt * (pow((1 + rate_of_interest / 100), time_period))
    ) - principle_amt


principle_amt = int(input("Enter the principal amount : "))
time_period = int(input("Enter the time period in years : "))
rate_of_interest = int(input("Enter the rate of interest : "))
print(
    f"The Compound Interest is {compound_interest(principle_amt, time_period, rate_of_interest):.2f}"
)
