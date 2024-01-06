def main():
    phrase = input("Greeting: ")
    print(f"${value(phrase)}")

def value(greeting):
    if greeting.lower().lstrip().startswith("hello"):
        return 0
    elif greeting.lower().lstrip().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
