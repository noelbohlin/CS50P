# från uppgiften Guessing Game från CS50

import random


def main():
    level = get_integer("Level: ")
    n = get_random_int(level)

    while True:
        guess = get_integer("Guess: ")

        if guess > n:
            print("Too large!")
        elif guess < n:
            print("Too small!")
        else:
            print("Just right!")
            break


def get_random_int(n):
    return random.randint(1, n)


def get_integer(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
            else:
                pass
        except ValueError:
            pass


if __name__ == "__main__":
    main()
