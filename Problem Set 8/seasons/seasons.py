""" från uppgiften Seasons från cS50 """

import sys
from datetime import date
import inflect

p = inflect.engine()


def main():
    """
    Main function of the program.

    This function prompts the user for their date of birth, 
    converts it to the number of days since then,
    and prints out the result.
    """
    try:
        year, month, day = input("Date of birth: ").split("-")
        year, month, day = int(year), int(month), int(day)
        print(convert(year, month, day))
    except Exception:
        sys.exit("Invalid date")


def convert(y, m, d):
    """
    Converts a given date to the number of minutes since that date.

    Parameters:
    y (int): Year of the date.
    m (int): Month of the date.
    d (int): Day of the date.

    Returns:
    str: Number of minutes since the given date, converted to words.
    """
    return (f"{p.number_to_words(int((date.today() - date(y, m, d)).days * 24 * 60))}"
            f" minutes").capitalize().replace("and ", "")


if __name__ == "__main__":
    main()
