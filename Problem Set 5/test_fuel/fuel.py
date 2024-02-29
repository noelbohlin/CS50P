""" Från uppgiften TEst Fuel från CS50 """

def main():
    while True:
        try:
            s = input("Fraction: ")
            fuelstate = convert(s)
            break
        except (ValueError, ZeroDivisionError):
            pass

    print(gauge(fuelstate))


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            z = (int(x) / int(y)) * 100

            if 0 <= z <= 100:
                return z
            raise ValueError

        except ValueError as e:
            raise ValueError from e
        except ZeroDivisionError as e:
            raise ZeroDivisionError from e


def gauge(percentage):
    if percentage <= 1:
        return "E"
    if percentage >= 99:
        return "F"
    return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
