class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Capacity exceeded")

        self._size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError("Not enough cookies")

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar(12)

    print("Capacity:", jar.capacity)
    print("Size:", jar.size)
    print("Jar:", jar)

    jar.deposit(5)

    print("After depositing 5:")
    print("Size:", jar.size)
    print("Jar:", jar)

    jar.withdraw(2)

    print("After withdrawing 2:")
    print("Size:", jar.size)
    print("Jar:", jar)


if __name__ == "__main__":
    main()
