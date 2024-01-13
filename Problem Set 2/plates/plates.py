""" från uppgiften Vanity Plates från CS50 """

def main():
    """
    Main function of the program.

    This function takes a plate as input, checks if it's valid, 
    and prints whether it's valid or not.
    """
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    """
    Checks if the given string s is a valid plate.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is a valid plate, False otherwise.
    """
    return (startwith2letters(s) and
            platelengthcorrect(s) and
            correctcharacters(s) and
            numberplacement(s))

def startwith2letters(plate):
    """
    Checks if the given plate string starts with exactly 2 letters.

    Parameters:
    plate (str): The plate string to check.

    Returns:
    bool: True if the plate string starts with exactly 2 letters, False otherwise.
    """
    return plate[0:2].isalpha()

def platelengthcorrect(plate):
    """
    Checks if the length of the given plate string is between 2 and 6.

    Parameters:
    plate (str): The plate string to check.

    Returns:
    bool: True if the length of the plate string is between 2 and 6, False otherwise.
    """
    return 2 <= len(plate) <= 6

def correctcharacters(plate):
    """
    Checks if all characters in the given plate string are alphanumeric.

    Parameters:
    plate (str): The plate string to check.

    Returns:
    bool: True if all characters are alphanumeric, False otherwise.
    """
    return plate.isalnum()

def numberplacement(plate):
    """
    Checks the placement of numbers in the given plate string.

    Parameters:
    plate (str): The plate string to check.

    Returns:
    bool: True if the placement of numbers is valid, False otherwise.
    """
    numberfound = False
    for character in plate:
        if character.isdigit():
            if character == "0":
                if not numberfound:
                    return False
            numberfound = True
        elif character.isalpha():
            if numberfound:
                return False
        else:
            return False
    return True

main()
