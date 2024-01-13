""" från upggiften Fuel Guage från CS50 """


def main():
    """
    Main function of the program.

    This function gets the fuel state as a fraction from the user,
    checks the fuel state, and prints out the corresponding character or percentage.
    """
    fuelstate = get_fraction("Fraction: ")

    if fuelstate <= 0.01:
        print("E")
    elif fuelstate >= 0.99:
        print("F")
    else:
        print(f"{round(fuelstate * 100)}%")


# gets decimal number from input
def get_fraction(prompt):
    """
    Prompts the user for a fraction and returns it as a decimal.

    Args:
        prompt (str): The string to display as a prompt to the user.

    Returns:
        float: The decimal equivalent of the fraction entered by the user.
    """
    while True:
        try:
            x, y = input(prompt).split("/")
            z = int(x) / int(y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if z <= 1:
                return z


main()
