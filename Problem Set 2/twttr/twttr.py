# från uppgiften just setting up my twttr från CS50

def main():
    s = input("Input: ")
    s = convert(s)
    print("Output:", s)

def convert(string):
    output = ""
    #checks if letter is vowel
    for letter in string:
        # checks if each letter is vowel
        letter = letter.rstrip("aAeEiIoOuU")
        output += letter
    return output.strip()

main()
