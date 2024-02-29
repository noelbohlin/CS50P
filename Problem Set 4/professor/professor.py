""" från uppgiften Little Professor frånCS50 """

import random


def main():
    level = get_level()
    correct_answers = 0

    for _ in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)
        eee_count = 0

        answer = input(f"{X} + {Y} = ")

        while True:
            try:
                if int(answer) == X + Y:
                    correct_answers += 1
                    break
                if eee_count >= 2:
                    print("EEE")
                    print(f"{X} + {Y} = {X + Y}")
                    break
                print("EEE")
                eee_count += 1

                answer = input(f"{X} + {Y} = ")
            except ValueError:
                if eee_count >= 2:
                    print("EEE")
                    print(f"{X} + {Y} = {X + Y}")
                    break
                print("EEE")
                eee_count += 1

                answer = input(f"{X} + {Y} = ")

    print("Score:", correct_answers)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n < 4:
                return n
            raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)
    raise ValueError


if __name__ == "__main__":
    main()
