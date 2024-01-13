""" från uppgiften Coke Maschine från CS50 """

DUE = 50
print(f"Amount Due: {DUE}")

while DUE > 0:
    n = int(input("Insert Coin: "))
    if n in (25, 10, 5):
        DUE -= n

    if DUE <= 0:
        owed = DUE * -1
        print(f"Change Owed: {owed}")
    else:
        print(f"Amount Due: {DUE}")
