# från uppgiften Making Faces från CS50
def main():
    text = input()
    print(convert(text))

def convert(emoticon):
    emoticon = emoticon.replace(":)", "🙂").replace(":(", "🙁")
    return emoticon

main()
