""" från uppgiften watch on youtube från cs50 """

import re


def main():
    """
    Main function of the program.

    This function takes user input, parses it, and prints the result.
    """
    print(parse(input("HTML: ")))


def parse(s):
    """
    Parses the input string to extract the YouTube video ID.

    Args:
        s (str): The input string containing the HTML embed code.

    Returns:
        str: The URL of the YouTube video if successful, otherwise None.
    """
    try:
        s = re.search(r"embed/(\w+)\"", s)
        return f"https://youtu.be/{s.group(1)}"
    except TypeError:
        return None


if __name__ == "__main__":
    main()
