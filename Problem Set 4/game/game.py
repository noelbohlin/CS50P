""" från uppgiften Guessing Game från CS50 """

import random


def main():
    """
    Main function. It generates a random number and prompts the user to guess it.
    The game continues until the user guesses correctly.
    """
    n = get_random_int(get_integer("Level: "))

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
    """
    Generates a random integer between 1 and n.

    Args:
        n (int): The upper limit for the random number.

    Returns:
        int: A random integer between 1 and n.
    """
    return random.randint(1, n)


def get_integer(prompt):
    """
    Prompts the user for input until a valid integer greater than 0 is entered.

    Args:
        prompt (str): The string to display as a prompt to the user.

    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass


if __name__ == "__main__":
    main()
