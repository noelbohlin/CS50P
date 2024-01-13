""" från uppgiften Grocery List från CS50 """

grocerylist = {}

while True:
    try:
        item = input().upper().strip()

        if item in grocerylist:
            grocerylist[item] += 1
        else:
            grocerylist[item] = 1
    except EOFError:
        print()

        for item, values in sorted(grocerylist.items()):
            print(values, item)
        break
