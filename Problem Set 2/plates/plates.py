""" från uppgiften Vanity Plates från CS50 """


def main():
    if is_valid(input("Plate: ").upper().strip()):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        startwith2letters(s)
        and platelengthcorrect(s)
        and correctcharacters(s)
        and numberplacement(s)
    )


def startwith2letters(plate):
    return plate[0:2].isalpha()


def platelengthcorrect(plate):
    return 2 <= len(plate) <= 6


def correctcharacters(plate):
    return plate.isalnum()


def numberplacement(plate):
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
