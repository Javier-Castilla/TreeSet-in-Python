from TreeSet import TreeSet
from random import randint


if __name__ == "__main__":
    items = [randint(0, 100) for _ in range(12)]
    t = TreeSet(int, items)
    print(t, items)
