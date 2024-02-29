""" från uppgiften figlet från CS50 """
import sys
import random
from pyfiglet import Figlet


figlet = Figlet()


def main():
    detect_invalid_input()
    set_font()
    print("Output:\n", figlet.renderText(input("Input: ")))


def detect_invalid_input():
    if len(sys.argv) != 1 and len(sys.argv) != 3:
        sys.exit("Invalid Usage")


def set_font():
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
