# från uppgiften Adieu, Adieu från CS50

import inflect
p = inflect.engine()

# initializes empty list
name = []

while True:
    try:
        name += [input("Name: ").strip().title()]
        # append also works, and is probably "better". but this works too.

    except EOFError:
        # new line before break
        print()
        break

print(f"Adieu, adieu, to {p.join(name)}")
