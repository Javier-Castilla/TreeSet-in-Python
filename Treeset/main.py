from TreeSet import TreeSet
from random import randint


if __name__ == "__main__":
    items = [randint(0, 100) for _ in range(30)]
    t = TreeSet(int, items)
    print(t, items)
    t.draw_tree()