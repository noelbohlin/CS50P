def main():
    s = input("Input: ")
    s = shorten(s)
    print("Output:", s)


def shorten(word):
    output = ""
    # checks if letter is vowel
    for letter in word:
        # checks if each letter is vowel
        letter = letter.rstrip("aAeEiIoOuU")
        output += letter
    return output.strip()


if __name__ == "__main__":
    main()
