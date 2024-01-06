# från uppgiften Coke Maschine från CS50

due = 50
print(f"Amount Due: {due}")

while due > 0:

    n = int(input("Insert Coin: "))
    # if its the correct coins, update value, else, just keep going
    if n == 25 or n == 10 or n == 5:
        due = due - n

    # if the cokes paid for, display possible change. else, restart loop
    if due <= 0:
        owed = due * -1
        print(f"Change Owed: {owed}")
    else:
        print(f"Amount Due: {due}")
