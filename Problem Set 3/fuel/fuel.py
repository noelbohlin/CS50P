""" från upggiften Fuel Guage från CS50 """


def main():
    fuelstate = get_fraction("Fraction: ")

    if fuelstate <= 0.01:
        print("E")
    elif fuelstate >= 0.99:
        print("F")
    else:
        print(f"{round(fuelstate * 100)}%")


def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            z = int(x) / int(y)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            if z <= 1:
                return z


main()
