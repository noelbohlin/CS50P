""" från uppgiften Outdated från CS50 """


alphabetic_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def main():
    y, m, d = format_date()
    print(f"{y:0004}-{m:02}-{d:02}")


def format_date():
    while True:
        inputdate = input("Date: ").strip()
        try:
            month, day, year = inputdate.split("/")
            month, day, year = int(month), int(day), int(year)

            if 0 < month <= 12 and 0 < day <= 31 and year > 0:
                break
        except (ValueError, IndexError) as e:
            try:
                if not "," in inputdate:
                    raise ValueError from e

                month, day, year = inputdate.split(" ")
                month, day, year = month.title(), int(day.rstrip(",")), int(year)

                if month in alphabetic_months:
                    month = int(alphabetic_months.index(month)) + 1

                    if 0 < month <= 12 and 0 < day <= 31 and year > 0:
                        break
            except (ValueError, IndexError):
                pass

    return year, month, day


main()
