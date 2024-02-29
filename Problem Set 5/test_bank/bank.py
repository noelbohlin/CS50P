"""Från uppgiften test Bank från CS50 """

def main():
    print(f"${value(input('Greeting: '))}")


def value(greeting):
    if greeting.lower().lstrip().startswith("hello"):
        return 0
    if greeting.lower().lstrip().startswith("h"):
        return 20
    return 100


if __name__ == "__main__":
    main()
