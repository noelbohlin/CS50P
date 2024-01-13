""" från uppgiften Scourgify från CS50 """

import csv
import sys


def main():
    """
    Main function of the program.
    Calls the convert function if the input is valid.
    """
    if valid_input():
        convert()


def convert():
    """
    Converts the input CSV file to a new format.
    """
    try:
        with open(sys.argv[1], encoding='utf-8') as file:
            reader = csv.DictReader(file)
            with open(sys.argv[2], "w", encoding='utf-8') as output:
                writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    last, first = row["name"].split(",")
                    writer.writerow(
                        {
                            "first": first.strip(),
                            "last": last.strip(),
                            "house": row["house"],
                        }
                    )

    except FileNotFoundError:
        sys.exit("File does not exist")


def valid_input():
    """
    Checks if the correct number of command-line arguments are provided and if they are CSV files.
    Returns True if the input is valid, 
    otherwise exits the program with an appropriate error message.
    """
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" in sys.argv[1] and ".csv" in sys.argv[2]:
        return True
    sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
