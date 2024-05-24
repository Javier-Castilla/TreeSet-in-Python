import random
import unittest
from tree_set import *
from tree_gui import GUI
import ast
import inspect
import sys
from tests.tests_classes import *
import time
import data_utils


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromName("tests.test_empty_tree_set"))
    suite.addTest(loader.loadTestsFromName("tests.test_many_items_tree_set"))
    suite.addTest(loader.loadTestsFromName("tests.test_other_items_tree_set"))
    suite.addTest(loader.loadTestsFromName("tests.test_simple_queue"))
    suite.addTest(loader.loadTestsFromName("tests.test_simple_stack"))
    return suite


def fill_list(list: list, size):
    auxiliar_items = set()
    while len(list) != size:
        if (num := random.randint(0, size)) not in auxiliar_items:
            auxiliar_items.add(size)
            list.append(num)


def test_times():
    with open("data/timesBST.csv", mode="w", encoding="utf-8") as fw1, open(
            "data/timesIN.csv", mode="w", encoding="utf-8") as fw2:
        size = 1
        print("size;milliseconds;seconds;iterations", file=fw1)

        while size < 17 * 10 ** 6:
            fill_list(items := list(), size)
            start_time = time.perf_counter()

            tree = TreeSet(int, items)
            for i in range(size):
                tree.add(i)

            tree.count = True
            tree.add(size)

            end_time = time.perf_counter()
            duration = (end_time - start_time) * 1000
            print(f"Tiempo de ejecución ({size}):", duration,
                  f"milisegundos ({tree.iterations})")
            print(
                f"{size};{round(duration, 3)};{round(duration / 1000, 3)};{tree.iterations}".replace(
                    ".", ","), file=fw1)

            size <<= 1


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
    # test_times()
    tree = TreeSet(int)
    app = GUI(tree)
    app.mainloop()
