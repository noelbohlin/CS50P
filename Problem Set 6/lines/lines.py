""" från uppgiften Lines of Code från CS50 """

import sys


def main():
    """
    Main function of the program.

    This function first checks if the input is valid using the valid_input() function.
    If the input is valid, it reads the lines from the file specified in the command-line argument
    and counts the number of lines using the count_lines() function. Finally, it prints the result.
    """
    if valid_input():
        print(count_lines(read_lines()))


def valid_input():
    """
    Checks if the input is valid.

    Returns:
        bool: True if the input is valid, False otherwise.
    """
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if ".py" in sys.argv[1]:
        return True
    sys.exit("Not a Python file")


def read_lines():
    """
    Reads lines from a file and returns them as a list.

    The file is specified by the command-line argument passed to the script.

    Returns:
        list: A list of strings, each string being a line from the file.
    """
    lines = []
    
    try:
        with open(sys.argv[1], encoding="utf-8") as file:
            lines = file.readlines()
        return lines
    except FileNotFoundError:
        sys.exit("File does not exist")


def count_lines(lines):
    """
    Counts the number of lines in the given list of lines.

    Parameters:
    lines (list): A list of strings representing lines.

    Returns:
    int: The number of lines in the list.
    """
    number_of_lines = 0

    for line in lines:
        if len(line.strip()) > 0 and not line.lstrip().startswith("#"):
            number_of_lines += 1
    return number_of_lines


if __name__ == "__main__":
    main()
