#
# från uppgiften Meal Time från CS50
#

def main():
    time = input("What time is is? ").strip().lower()
    time = convert(time)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

# * converts from hh:mm to hour in decimal form

def convert(t):
    if t.endswith("p.m."):
        # removes suffixes and whitespace
        t = t.removesuffix("p.m.").rstrip()
        hours, minutes = t.split(":")
        # * p.m. to 24h conversion and conversion to decimal
        t = int(hours) + (int(minutes) / 60) + 12
        return t
    else:
        # removes possible suffixes and whitespace
        t = t.removesuffix("a.m.").rstrip()
        hours, minutes = t.split(":")
        t = int(hours) + (int(minutes) / 60)
        return t

# ! what does line 34 mean?
if __name__ == "__main__":
    main()
