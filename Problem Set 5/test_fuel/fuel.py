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
            X, Y = fraction.split("/")
            Z = (int(X) / int(Y)) * 100

            if 0 <= Z <= 100:
                return Z
            else:
                raise ValueError

        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
