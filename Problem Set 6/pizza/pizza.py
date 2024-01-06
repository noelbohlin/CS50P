# Från uppgiften Pizza Py från CS50
import sys, csv
from tabulate import tabulate

def main():
    if valid_input():
        print(tabulate(read_lines()[1:], read_lines()[0], tablefmt="grid"))


def read_lines():
    lines = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                lines.append(row)
        return lines
    except FileNotFoundError:
        sys.exit("File does not exist")


def valid_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".csv" in sys.argv[1]:
        return True
    else:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
