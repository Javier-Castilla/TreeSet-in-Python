from TreeSet import TreeSet
from random import randint


if __name__ == "__main__":
    #items = [randint(0, 100) for _ in range(12)]
    t = TreeSet(int)
    t.add(10)
    t.add(5)
    t.add(15)
    print(t)
    print(t.floor(6))
