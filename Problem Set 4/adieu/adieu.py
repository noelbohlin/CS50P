""" från uppgiften Adieu, Adieu från CS50 """

import inflect

name = []

while True:
    try:
        name += [input("Name: ").strip().title()]
    except EOFError:
        print()
        break

print(f"Adieu, adieu, to {inflect.engine().join(name)}")
