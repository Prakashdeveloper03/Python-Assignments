wage = float(input("Enter the wage: "))
regular_hours = float(input("Enter the regular hours: "))
overtime_hours = float(input("Enter the overtime hours: "))
print(
    f"The total weekly pay is {round(regular_hours * wage + overtime_hours * wage * 1.5, 2)}"
)
