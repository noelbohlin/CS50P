# från uppgiften Outdated från CS50


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
    "December"
]


def main():
    y, m, d = format_date()
    print(f"{y:0004}-{m:02}-{d:02}")


def format_date():
    while True:
        inputdate = input("Date: ").strip()
        # try for the date with / separator, then int the input and check for validity
        try:
            month, day, year = inputdate.split("/")
            month, day, year = int(month), int(day), int(year)

            if 0 < month <= 12 and 0 < day <= 31 and year > 0:
                break
        # if input isn't / then try for alphabetick month
        except Exception:
            try:
                # this line is needed to not accept more than the problem says
                # i would remove this if it wasnt needed for the check50
                if not "," in inputdate:
                    return gibberish

                month, day, year = inputdate.split(" ")
                month, day, year = month.title(), int(day.rstrip(",")), int(year)

                if month in alphabetic_months:
                    month = int(alphabetic_months.index(month)) + 1

                    if 0 < month <= 12 and 0 < day <= 31 and year > 0:
                        break
            except Exception:
                pass

    return year, month, day

main()
