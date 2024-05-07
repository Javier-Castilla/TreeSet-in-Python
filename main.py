import random
import unittest
from TreeSet import *
import time


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromName("tests.test_empty_treeset"))
    suite.addTest(loader.loadTestsFromName("tests.test_many_items_treeset"))
    suite.addTest(loader.loadTestsFromName("tests.test_other_items_treeset"))
    return suite


def bubble_sort(arr):
    n = len(arr)
    # Iterar sobre todos los elementos de la lista
    for i in range(n):
        # Últimos i elementos ya están en su lugar correcto
        for j in range(0, n - i - 1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def fill_list(list: list, size):
    auxiliar_items = set()
    while len(list) != size:
        if (num := random.randint(0, size)) not in auxiliar_items:
            auxiliar_items.add(size)
            list.append(num)


def test_times():
    with open("data/timesBST.csv", mode="w", encoding="utf-8") as fw1, open("data/timesIN.csv", mode="w", encoding="utf-8") as fw2:
        size = 1
        print("size;miliseconds;seconds")

        while size < 16 * 10 ** 6:
            # Registro del tiempo de inicio
            fill_list(items := list(), size)
            start_time = time.perf_counter()

            tree = TreeSet(int, items)

            # Registro del tiempo de finalización
            end_time = time.perf_counter()
            duration = (end_time - start_time) * 1000
            print(f"Tiempo de ejecución ({size}):", duration, "milisegundos")
            print(
                f"{size};{round(duration, 3)};{round(duration / 1000, 3)}".replace(
                    ".", ","), file=fw1)
            """start_time = time.perf_counter()

            for i in items:
                i in items

            end_time = time.perf_counter()
            duration = (end_time - start_time) * 1000
            print(f"Tiempo de ejecución al buscar normal ({size}):", duration, "milisegundos")
            print(
                f"{size};{round(duration, 3)};{round(duration / 1000, 3)}".replace(
                    ".", ","), file=fw2)"""

            size <<= 1


if __name__ == "__main__":
    """runner = unittest.TextTestRunner()
    runner.run(suite())"""
    test_times()
