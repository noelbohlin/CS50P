""" Från uppgiften Test Twitter från CS50 """

def main():
    """
    Main function of the program. Takes an input string, shortens it by removing all vowels, 
    and prints the result.
    """
    print("Output:", shorten(input("Input: ")))


def shorten(word):
    """
    Shortens the given word by removing all vowels.

    Parameters:
    word (str): The word to be shortened.

    Returns:
    str: The shortened word.
    """
    output = ""
    for letter in word:
        output += letter.rstrip("aAeEiIoOuU")
    return output.strip()


if __name__ == "__main__":
    main()
