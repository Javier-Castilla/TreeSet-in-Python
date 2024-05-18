
import random
import unittest
from TreeSet import *
import ast
import inspect
import sys

def listar_modulos_importados(source_code):
    tree = ast.parse(source_code)
    modulos_importados = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                modulos_importados.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            modulos_importados.append(node.module)

    return modulos_importados

def listar_clases_de_modulo(modulo):
    clases = []
    for nombre, objeto in inspect.getmembers(modulo):
        if inspect.isclass(objeto):
            clases.append(nombre)
    return clases

# Leer el código fuente del módulo actual (asumimos que este script está en el mismo archivo)
with open(__file__, 'r') as f:
    source_code = f.read()

modulos_importados = listar_modulos_importados(source_code)

print("Clases en cada módulo importado:")
for nombre_modulo in modulos_importados:
    try:
        if nombre_modulo in sys.modules:
            modulo = sys.modules[nombre_modulo]
        else:
            modulo = __import__(nombre_modulo)

        clases = listar_clases_de_modulo(modulo)
        if clases:
            print(f"Módulo: {nombre_modulo}")
            for clase in clases:
                print(f" - {clase}")
    except (AttributeError, ImportError):
        # En caso de que el módulo no pueda ser cargado o inspeccionado
        continue

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

def counting_sort(arr):
    # Encuentra el máximo y mínimo en el array
    max_val = max(arr)
    min_val = min(arr)

    # Calcula el rango de valores posibles
    range_val = max_val - min_val + 1

    # Inicializa un array de conteo con el rango
    count = [0] * range_val

    # Cuenta la frecuencia de cada elemento
    for num in arr:
        count[num - min_val] += 1

    # Reconstruye el array ordenado
    sorted_arr = []
    for i in range(range_val):
        sorted_arr.extend([i + min_val] * count[i])

    return sorted_arr

def test_times():
    with open("data/timesBST.csv", mode="w", encoding="utf-8") as fw1, open("data/timesIN.csv", mode="w", encoding="utf-8") as fw2:
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
            print(f"Tiempo de ejecución ({size}):", duration, f"milisegundos ({tree.iterations})")
            print(
                f"{size};{round(duration, 3)};{round(duration / 1000, 3)};{tree.iterations}".replace(
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
    runner = unittest.TextTestRunner()
    runner.run(suite())
    #test_times()
    """app = GUI()
    app.mainloop()"""
