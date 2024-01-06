# från uppgiften CS50 P-shirt från CS50
import sys
from PIL import Image, ImageOps


def main():
    if valid_input():
        overlay()


def overlay():
    try:
        # open up both pictures
        with Image.open("shirt.png") as shirt:
            with Image.open(sys.argv[1]) as image:

                # get size of shirt and fits muppet to it
                image = ImageOps.fit(image, shirt.size)
                # overlay shirt over image
                image.paste(shirt, shirt)
                # save
                image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("File does not exist")


def valid_input():
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
