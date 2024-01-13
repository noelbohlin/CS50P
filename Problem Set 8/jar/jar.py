""" från uppgiften Cookie Jar från CS50 """


class Jar:
    """
    Represents a jar that can hold cookies.

    Attributes:
        _capacity (int): The maximum number of cookies the jar can hold.
        _size (int): The current number of cookies in the jar.
    """
    def __init__(self, capacity=12):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError
        self._size = 0

    def __str__(self):
        return f"{'🍪' * self.size}"

    def deposit(self, n):
        """
        Deposits a specified amount of cookies into the jar.

        Args:
            n (int): The number of cookies to deposit.

        Raises:
            ValueError: If the number of cookies to deposit would exceed the jar's capacity.
        """
        if n + self.size <= self._capacity:
            self._size += n
        else:
            raise ValueError

    def withdraw(self, n):
        """
        Withdraws a specified amount of cookies from the jar.

        Args:
            n (int): The number of cookies to withdraw.

        Raises:
            ValueError: If the number of cookies to withdraw exceeds the current size of the jar.
        """
        if n <= self.size:
            self._size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        """
        Returns the capacity of the jar.
        
        Returns:
            int: The maximum number of cookies the jar can hold.
        """
        return self._capacity

    @property
    def size(self):
        """
        Returns the current number of cookies in the jar.

        Returns:
            int: The current number of cookies in the jar.
        """
        return self._size


# * def main():
#     jar = Jar()
#     jar.deposit(5)
#     jar.withdraw(2)
#     print(jar.capacity)
#     print(jar.size)
#     print(jar)
#
# if __name__ == "__main__":
# *   main()
