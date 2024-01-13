""" måste börja med 2 bokstäver
    måste vara mellan 2 och 6 karaktärer långt
    måste vara antingen bokstäver eller siffror
    första siffran som förekommer får inte vara en 0a
    efter första siffran får inga bokstäver förekomma
"""

def main():
    """
    Main function of the program.

    Takes user input for a license plate, converts it to uppercase, 
    strips leading and trailing whitespace,
    and checks if it's valid according to certain conditions. 
    Prints "Valid" if the plate is valid, "Invalid" otherwise.
    """
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Checks if the given string is valid according to certain conditions.

    Parameters:
    s (str): The string to check.

    Returns:
    bool: True if the string is valid, False otherwise.
    """
    if (
        startwith2letters(s)
        and platelengthcorrect(s)
        and correctcharacters(s)
        and numberplacement(s)
    ):
        return True
    return False


def startwith2letters(plate):
    """
    Checks if the given plate starts with two letters.

    Parameters:
    plate (str): The license plate string.

    Returns:
    bool: True if the plate starts with two letters, False otherwise.
    """
    return plate[0:2].isalpha()


def platelengthcorrect(plate):
    """
    Checks if the length of the plate is between 2 and 6 characters.

    Parameters:
    plate (str): The license plate string.

    Returns:
    bool: True if the length is correct, False otherwise.
    """
    return 2 <= len(plate) <= 6


def correctcharacters(plate):
    """
    Checks if the given plate consists of alphanumeric characters only.

    Parameters:
    plate (str): The license plate string.

    Returns:
    bool: True if the plate consists of alphanumeric characters only, False otherwise.
    """
    return plate.isalnum()


def numberplacement(plate):
    """
    Checks the placement of numbers in the given plate.

    Parameters:
    plate (str): The license plate string.

    Returns:
    bool: True if the placement of numbers is correct, False otherwise.
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


if __name__ == "__main__":
    main()
