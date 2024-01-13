""" från uppgiften figlet från CS50 """
import sys
import random
from pyfiglet import Figlet


figlet = Figlet()


def main():
    """
    Main function of the program. Detects invalid input, sets the font, and prints the output.
    """
    detect_invalid_input()
    set_font()
    print("Output:\n", figlet.renderText(input("Input: ")))


def detect_invalid_input():
    """
    Checks if the number of command line arguments is valid.
    Exits the program if the usage is invalid.
    """
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid Usage")


def set_font():
    """
    Sets the font for the figlet object. If no arguments are passed, a random font is selected.
    If a font argument is passed, it sets the font to the specified one if it exists.
    """
    if len(sys.argv) == 1:
        figlet.setFont(
            font=(figlet.getFonts()[random.randint(0, len(figlet.getFonts()))])
        )
    elif len(sys.argv) == 3:
        if sys.argv[1] == ("-f" or "--font"):
            if sys.argv[2] in figlet.getFonts():
                figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")


if __name__ == "__main__":
    main()
