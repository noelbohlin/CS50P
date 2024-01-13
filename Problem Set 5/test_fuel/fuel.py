""" Från uppgiften TEst Fuel från CS50 """

def main():
    """
    Main function of the program.

    This function prompts the user for a fraction, converts it to a percentage, 
    and prints the result.
    """
    while True:
        try:
            s = input("Fraction: ")
            fuelstate = convert(s)
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(fuelstate))


def convert(fraction):
    """
    Converts a fraction to a percentage.

    Parameters:
    fraction (str): The fraction to convert.

    Returns:
    float: The converted percentage.
    """
    while True:
        try:
            x, y = fraction.split("/")
            z = (int(x) / int(y)) * 100

            if 0 <= z <= 100:
                return z
            raise ValueError

        except ValueError as e:
            raise ValueError from e
        except ZeroDivisionError as e:
            raise ZeroDivisionError from e


def gauge(percentage):
    """
    Converts a percentage value to a string representation.

    Parameters:
    percentage (float): The percentage value to convert.

    Returns:
    str: The string representation of the percentage.
    """
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
