""" måste börja med 2 bokstäver
    måste vara mellan 2 och 6 karaktärer långt
    måste vara antingen bokstäver eller siffror
    första siffran som förekommer får inte vara en 0a
    efter första siffran får inga bokstäver förekomma
"""

def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if (
        startwith2letters(s)
        and platelengthcorrect(s)
        and correctcharacters(s)
        and numberplacement(s)
    ):
        return True
    return False


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


if __name__ == "__main__":
    main()
