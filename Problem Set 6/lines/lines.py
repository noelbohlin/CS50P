# från uppgiften Lines of Code från CS50

import sys


def main():
    if valid_input():
        print(count_lines(read_lines()))


def valid_input():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" in sys.argv[1]:
        return True
    else:
        sys.exit("Not a Python file")

# read lines and writes to list, one line per index
def read_lines():
    lines = []

    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        sys.exit("File does not exist")


#count the number of lines and return int
def count_lines(lines):
    number_of_lines = 0

    for line in lines:
        # check that line is not empty and isnt a comment
        if len(line.strip()) > 0 and not line.lstrip().startswith("#"):
            number_of_lines += 1
    return number_of_lines


if __name__ == "__main__":
    main()
