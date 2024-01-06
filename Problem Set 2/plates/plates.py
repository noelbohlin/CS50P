# från uppgiften Vanity Plates från CS50


# måste börja med 2 bokstäver
# måste vara mellan 2 och 6 karaktärer långt
# måste vara antingen bokstäver eller siffror
# första siffran som förekommer får inte vara en 0a
# efter första siffran får inga bokstäver förekomma

def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# * is the plate valid. return bool

def is_valid(s):
    if startwith2letters(s) and platelengthcorrect(s) and correctcharacters(s) and numberplacement(s):
        return True
    else:
        return False

# is the first to characters letter, return bool
def startwith2letters(plate):
    return plate[0:2].isalpha()

# lenght of plate
def platelengthcorrect(plate):
    return 2 <= len(plate) <= 6

# is it alphanumeric characters, ie no specialcharacters
def correctcharacters(plate):
    return plate.isalnum()

# is any number followed by a letter
# is the first number a "0"
def numberplacement(plate):
    # intizialize bool variable
    numberfound = False

    # checks each character in order left to right
    for character in plate:

        # checks if first number is 0, returns false in that case
        if character.isdigit():

            if character == "0":
                if numberfound == False:
                    return False
            numberfound = True

        # checks if letter comes after a number, returns false
        elif character.isalpha():
            if numberfound:
                return False
        else:
            return False
    return True


main()
