# från uppgiften Deep Thought från CS50
answer = input ("What is the Answer to the Great Queation of Life, the Universe and Everything? ").strip().title()

match answer:
    case "Forty Two" | "Forty-Two" | "42":
        print("Yes")
    case _:
        print("No")
