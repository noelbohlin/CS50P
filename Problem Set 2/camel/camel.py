# från uppgiften camelCase från CS50
def main():
    s = input("camelCase: ")
    s = convert(s)
    print("snake_case: ", s)

def convert(string):
    #clears output varible
    output = ""
    # checks each letter and writes it in output variable
    for letter in string:
        if letter.isupper():
            # if letter is uppercase it adds a underscore to the end of the output variable and then adds the letter in lowercase
            output += "_" + letter.lower()
        else:
            # else it adds the letter to the end of the output variable
            output += letter
    # removes extra underscores from the begining of words
    output = output.lstrip("_")
    return output

main()
