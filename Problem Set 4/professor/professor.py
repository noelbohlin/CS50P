# från uppgiften Little Professor frånCS50

import random
import sys


def main():
    level = get_level()
    correct_answers = 0

    for i in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        EEE_count = 0

        answer = input(f"{X} + {Y} = ")

        while True:
            try:
                if int(answer) == X + Y:
                    correct_answers += 1
                    break
                elif EEE_count >= 2:
                    print("EEE")
                    print(f"{X} + {Y} = {X + Y}")
                    break
                else:
                    print("EEE")
                    EEE_count += 1

                    answer = input(f"{X} + {Y} = ")
            except ValueError:
                if EEE_count >= 2:
                    print("EEE")
                    print(f"{X} + {Y} = {X + Y}")
                    break
                else:
                    print("EEE")
                    EEE_count += 1

                    answer = input(f"{X} + {Y} = ")

    print("Score:", correct_answers)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n < 4:
                return n
            else:
                raise ValueError
        except ValueError:
            continue


# returns randomly generated integer with level digits
# or raises ValueError if level is not 1,2,3
def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
