""" från uppgiften Regular Um Expressions från CS50 """

import re


def main():
    """
    Main function of the program.
    Prompts the user for input and prints the count of 'um' in the input string.
    """
    print(count(input("Text: ")))


def count(s):
    """
    Counts the number of occurrences of the word 'um' in the input string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The number of occurrences of 'um'.
    """
    return len(re.findall(r"(\W|^)um(\W|$)", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
