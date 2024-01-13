"""Från uppgiften test Bank från CS50 """

def main():
    """
    Main function of the program.
    """
    print(f"${value(input('Greeting: '))}")


def value(greeting):
    """
    This function takes a greeting as input and returns a value based on the greeting.
    If the greeting starts with "hello", it returns 0.
    If the greeting starts with "h", it returns 20.
    Otherwise, it returns 100.
    """
    if greeting.lower().lstrip().startswith("hello"):
        return 0
    if greeting.lower().lstrip().startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()
