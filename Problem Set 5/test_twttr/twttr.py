""" Från uppgiften Test Twitter från CS50 """

def main():
    print("Output:", shorten(input("Input: ")))


def shorten(word):
    output = ""
    for letter in word:
        output += letter.rstrip("aAeEiIoOuU")
    return output.strip()


if __name__ == "__main__":
    main()
