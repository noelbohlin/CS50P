""" från uppgiften just setting up my twttr från CS50 """


def main():
    """
    Main function of the program.

    This function takes an input string, converts it by removing all vowels,
    and prints the converted string.
    """
    print("Output:", convert(input("Input: ")))


def convert(string):
    """
    Converts a given string by removing all vowels.

    Args:
        string (str): The input string.

    Returns:
        str: The converted string without vowels.
    """
    output = ""
    for letter in string:
        output += letter.rstrip("aAeEiIoOuU")
    return output.strip()


main()
