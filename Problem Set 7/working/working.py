""" från uppgiften Working 9 to 5 från CS50 """

import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(s):
    if s := re.search(
        r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s
    ):
        start_hours = int(s.group(1))
        start_minutes = s.group(2)
        start_timeofday = s.group(3)
        end_hours = int(s.group(4))
        end_minutes = s.group(5)
        end_timeofday = s.group(6)

        # make sure noon and midnight are right
        if start_timeofday == "AM" and start_hours == 12:
            start_hours = 0
        elif start_timeofday == "PM" and start_hours != 12:
            start_hours += 12

        # make sure noon and midnight are right
        if end_timeofday == "AM" and end_hours == 12:
            end_hours = 0
        elif end_timeofday == "PM" and end_hours != 12:
            end_hours += 12

        # makes the minutes usable
        if start_minutes is None and end_minutes is None:
            start_minutes = int(0)
            end_minutes = int(0)
        else:
            start_minutes = int(start_minutes)
            end_minutes = int(end_minutes)
        if (
            0 <= start_hours < 24
            and 0 <= start_minutes < 60
            and 0 <= end_hours < 24
            and 0 <= end_minutes < 60
        ):
            return f"{start_hours:02d}:{start_minutes:02d} to {end_hours:02d}:{end_minutes:02d}"
        raise ValueError("Invalid input")
    raise ValueError("Invalid input")


if __name__ == "__main__":
    main()
