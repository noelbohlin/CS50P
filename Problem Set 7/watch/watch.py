# från uppgiften watch on youtube från cs50

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        s = re.search(r"embed/(\w+)\"", s)
        return f"https://youtu.be/{s.group(1)}"
    except Exception:
        return None


if __name__ == "__main__":
    main()
