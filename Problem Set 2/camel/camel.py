""" från uppgiften camelCase från CS50 """

def main():
    """
    Main function of the program.
    Takes input from the user, converts it from camelCase to snake_case, and prints the result.
    """
    print("snake_case: ", convert(input("camelCase: ")))

def convert(string):
    """
    Converts a camelCase string to snake_case.

    Parameters:
    string (str): The camelCase string to convert.

    Returns:
    str: The converted snake_case string.
    """
    output = ""
    for letter in string:
        if letter.isupper():
            output += "_" + letter.lower()
        else:
            output += letter
    return output.lstrip("_")

main()
