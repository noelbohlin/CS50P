# från uppgiften Math Interpreter från CS50

x, y, z = input("Expression: ").split(" ")

if y == "+":
    print(f"{round(float(x) + float(z), 1)}")
elif y == "-":
    print(f"{round(float(x) - float(z), 1)}")
elif y == "*":
    print(f"{round(float(x) * float(z), 1)}")
elif y == "/":
    print(f"{round(float(x) / float(z), 1)}")
else:
    print("error")
