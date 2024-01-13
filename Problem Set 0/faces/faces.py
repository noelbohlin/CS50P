""" från uppgiften Making Faces från CS50 """

def main():
    print(convert(input()))

def convert(emoticon):
    return emoticon.replace(":)", "🙂").replace(":(", "🙁")

main()
