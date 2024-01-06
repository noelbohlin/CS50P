# * från uppgiften Grocery List från CS50


grocerylist = {}

while True:
    try:
        # take input
        item = input().upper().strip()

        # add number in value to corresponding added item
        if item in grocerylist:
            grocerylist[item] += 1
        else:
            grocerylist[item] = 1

    except EOFError:
        print()

        # print sorted list
        for item, values in sorted(grocerylist.items()):
            print(values, item)

        break
