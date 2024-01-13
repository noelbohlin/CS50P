""" från uppgiften Numb3rs från CS50 """

def main():
    """
    Main function of the program.

    This function prompts the user for an IP address, validates it, 
    and prints whether it's valid or not.
    """
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    """
    Validates an IP address.

    Args:
        ip (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    try:
        a, b, c, d = ip.split(".")

        if (
            0 <= int(a) <= 255
            and 0 <= int(b) <= 255
            and 0 <= int(c) <= 255
            and 0 <= int(d) <= 255
        ):
            return True
        return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()
