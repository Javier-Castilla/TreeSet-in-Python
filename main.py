import unittest
from TreeSet import *
from test_classes import *
import time


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromName("tests.test_empty_treeset"))
    suite.addTest(loader.loadTestsFromName("tests.test_many_items_treeset"))
    return suite


def test_times():
    with open("data/times.csv", mode="w", encoding="utf-8") as fw:
        size = 1
        print("size;miliseconds;seconds", file=fw)

        while size < 17 * 10 ** 6:
            # Registro del tiempo de inicio
            tree = TreeSet(int)
            start_time = time.perf_counter()

            for i in range(size):
                tree.add(i)

            # Registro del tiempo de finalización
            end_time = time.perf_counter()
            duration = (end_time - start_time) * 1000
            print("Tiempo de ejecución:", duration, "milisegundos")

            print(f"{size};{round(duration, 3)};{round(duration / 1000, 3)}".replace(".", ","), file=fw)

            size <<= 1


if __name__ == "__main__":
    """runner = unittest.TextTestRunner()
    runner.run(suite())"""

    test_times()
