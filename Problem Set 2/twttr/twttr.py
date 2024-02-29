""" från uppgiften just setting up my twttr från CS50 """


def main():
    print("Output:", convert(input("Input: ")))


def convert(string):
    output = ""
    for letter in string:
        output += letter.rstrip("aAeEiIoOuU")
    return output.strip()


main()
