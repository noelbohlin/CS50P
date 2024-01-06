# från uppgiften Felipe's Taqueria från CS50


menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

while True:
    try:
        item = input("Item: ").title()

        if item in menu:
            # add cost to total
            total += menu[item]
            # round to 2 decimals
            total = round(total, 2)
            # force print with 2 decimals always
            print(f"Total: ${total:.2f}")

    except EOFError:
        # new line before break
        print()
        break

