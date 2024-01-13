# från uppgiften Cookie Jar från CS50


class Jar:
    def __init__(self, capacity=12):
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError
        self._size = 0

    def __str__(self):
        return f"{'🍪' * self.size}"

    def deposit(self, n):
        if n + self.size <= self._capacity:
            self._size += n
        else:
            raise ValueError

    def withdraw(self, n):
        if n <= self.size:
            self._size -= n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


"""
def main():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    print(jar.capacity)
    print(jar.size)
    print(jar)

if __name__ == "__main__":
    main()
"""
