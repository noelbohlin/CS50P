""" från uppgiften Meal Time från CS50 """

def main():
    """
    Main function of the program.
    Converts the input time to a decimal number representing the hour and minute.
    Then, it prints out whether it's breakfast, lunch, or dinner time based on the converted time.
    """
    time = convert(input("What time is is? ").strip().lower())

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(t):
    """
    Converts the input time string to a decimal number representing the hour and minute.
    Handles both AM and PM times.
    """
    if t.endswith("p.m."):
        hours, minutes = t.removesuffix("p.m.").rstrip().split(":")
        return int(hours) + (int(minutes) / 60) + 12

    t = t.removesuffix("a.m.").rstrip()
    hours, minutes = t.split(":")
    return int(hours) + (int(minutes) / 60)

if __name__ == "__main__":
    main()
