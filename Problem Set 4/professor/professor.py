""" från uppgiften Little Professor frånCS50 """

import random


def main():
    """
    Main function of the program.

    This function gets the level of difficulty from the user, generates 10 pairs of random integers,
    and checks if the user's answers are correct.
    """
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
    """
    Prompts the user to enter a level and validates the input.

    Returns:
        int: The level entered by the user.
    """
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n < 4:
                return n
            raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    """
    Generates a random integer based on the given level.

    Args:
        level (int): The level of difficulty. Must be between 1 and 3.

    Returns:
        int: A random integer within the appropriate range for the given level.
    """
    if level == 1:
        return random.randint(0, 9)
    if level == 2:
        return random.randint(10, 99)
    if level == 3:
        return random.randint(100, 999)
    raise ValueError


if __name__ == "__main__":
    main()
