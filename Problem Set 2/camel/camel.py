""" från uppgiften camelCase från CS50 """


def main():
    print("snake_case: ", convert(input("camelCase: ")))


def convert(string):
    output = ""
    for letter in string:
        if letter.isupper():
            output += "_" + letter.lower()
        else:
            output += letter
    return output.lstrip("_")


main()
