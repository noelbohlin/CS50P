""" från uppgiften Seasons från cS50 """

import sys
from datetime import date
import inflect

p = inflect.engine()


def main():
    try:
        year, month, day = input("Date of birth: ").split("-")
        year, month, day = int(year), int(month), int(day)
        print(convert(year, month, day))
    except Exception:
        sys.exit("Invalid date")


def convert(y, m, d):
    return (f"{p.number_to_words(int((date.today() - date(y, m, d)).days * 24 * 60))}"
            f" minutes").capitalize().replace("and ", "")


if __name__ == "__main__":
    main()
