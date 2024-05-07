import random
import unittest

from TreeSet import TreeSet
from tests.tests_classes import *

class TestOtherItemsTreeSet(unittest.TestCase):
    def test_add1(self):
        tree = TreeSet(Person)
        items = [Person(f"Person{num}", num*10) for num in range(10)]

        for item in items:
            self.assertTrue(tree.add(item), "Wrong value after inserting new value")

        self.assertEqual(tree.size(), 10, "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")

        with self.assertRaises(TypeError):
            tree.add(Worker("Worker", 28, "Technician"))

    def test_add2(self):
        tree = TreeSet(Professor)
        items = [Professor(f"Person{num}", num) for num in range(10)]

        for item in items:
            self.assertTrue(tree.add(item), "Wrong value after inserting new value")

        self.assertEqual(tree.size(), 10, "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")

if __name__ == '__main__':
    unittest.main()
