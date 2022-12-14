def fahrenheit(celsius: float) -> float:
    return (celsius * 1.8) + 32


celsius = float(input("Enter the celsius : "))
print(f"Fahrenheit of {celsius} celsius is {fahrenheit(celsius) :.2f}")
