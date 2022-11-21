def say_name(first_name: str, last_name: str) -> None:
    print(f"Hello, {first_name} {last_name}\nWelcome to Python!")


first_name = input("Enter your firstname : ")
last_name = input("Enter your lastname : ")
say_name(first_name, last_name)
