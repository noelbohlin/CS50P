""" från uppgiften CS50 P-shirt från CS50 """

import sys
from PIL import Image, ImageOps


def main():
    """
    Main function of the program.

    This function checks if the input is valid and then calls the overlay function.
    """
    if valid_input():
        overlay()


def overlay():
    """
    Overlays the shirt image onto another image.

    This function opens the shirt image and the input image, 
    resizes the input image to fit the size of the shirt, 
    pastes the shirt onto the input image, and saves the result.
    """
    try:
        with Image.open("shirt.png") as shirt:
            with Image.open(sys.argv[1]) as image:
                image = ImageOps.fit(image, shirt.size)
                image.paste(shirt, shirt)
                image.save(sys.argv[2])
    except FileNotFoundError:
        sys.exit("File does not exist")


def valid_input():
    """
    Validates the command-line arguments passed to the script.
    Checks if the number of arguments is correct and if the input and output formats are supported.
    """
    input_format = sys.argv[1].split(".")[1].lower()
    output_format = sys.argv[2].split(".")[1].lower()
    supported_formats = ["jpg", "png", "jpeg"]

    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not input_format in supported_formats:
        sys.exit("Invalid input")
    elif not output_format in supported_formats:
        sys.exit("Invalid output")
    elif input_format != output_format:
        sys.exit("Input and output have different extensions")
    else:
        return True


if __name__ == "__main__":
    main()
