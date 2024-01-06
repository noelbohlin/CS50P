from pyfiglet import Figlet
import sys
import random


figlet = Figlet()


def main():
    detect_invalid_input()
    set_font()

    print("Output:\n", figlet.renderText(input("Input: ")))


def detect_invalid_input():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid Usage")


def set_font():
    # set random font
    if len(sys.argv) == 1:
        # set font
        figlet.setFont(
            # get font from random int (0 - length of fontlist) pass to getfonts as index in fontlist
            font=(figlet.getFonts()[random.randint(0, len(figlet.getFonts()))])
        )
    # set font
    elif len(sys.argv) == 3:
        # set font if found
        if sys.argv[1] == ("-f" or "--font"):
            if sys.argv[2] in figlet.getFonts():
                figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")


if __name__ == "__main__":
    main()
