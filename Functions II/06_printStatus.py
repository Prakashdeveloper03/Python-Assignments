def printStatus(status_code: str) -> str:
    """
    Function accepts status code 'S', 'M', 'D', or 'U' and
    returns the string 'Separated', 'Married', 'Divorced' or 'Unmarried' respectively.

    Args:
        status_code (str): required argument ['S' or 'M' or 'D' or 'U']

    Returns:
        str: returns corresponding value for the given status code
    """
    res = ""
    match status_code:
        case "S":
            res += "Separated"
        case "M":
            res += "Married"
        case "D":
            res += "Divorced"
        case "U":
            res += "Unmarried"
        case _:
            res += "Invalid, Status code..!"
    return res


status_code = input("Enter the status code : ")
print(f"{status_code} --> {printStatus(status_code)}")
