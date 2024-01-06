# från upggiften Fuel Guage från CS50


def main():
    fuelstate = get_fraction("Fraction: ")

    if fuelstate <= 0.01:
        print("E")
    elif fuelstate >= 0.99:
        print("F")
    else:
        fuelstate = round(fuelstate * 100)
        print(f"{fuelstate}%")


# gets decimal number from input
def get_fraction(prompt):
    while True:
        # maybe not best to have multiple lines in here but its easier to keep track of
        try:
            X, Y = (input(prompt).split("/"))
            Z = int(X) / int(Y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if Z <= 1:
                return Z
            else:
                pass

main()
