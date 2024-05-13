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

    def test_add2(self):
        tree = TreeSet(Professor)
        items = [Professor(f"Person{num}", num) for num in range(10)]

        for item in items:
            self.assertTrue(tree.add(item), "Wrong value after inserting new value")

        self.assertEqual(tree.size(), 10, "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")

    def test_empty_tree(self):
        tree = TreeSet(Person)
        self.assertTrue(tree.is_empty(), "Tree should be empty")

    def test_add_and_check_empty(self):
        tree = TreeSet(Person)
        tree.add(Person("Person1", 10))
        self.assertFalse(tree.is_empty(), "Tree should not be empty")

    def test_add_and_remove_check_empty(self):
        tree = TreeSet(Person)
        person = Person("Person1", 10)
        tree.add(person)
        tree.remove(person)
        self.assertTrue(tree.is_empty(), "Tree should be empty after removing the element")

    def test_tree_size(self):
        tree = TreeSet(Person)
        items = [Person(f"Person{num}", num*10) for num in range(10)]
        for item in items:
            tree.add(item)
        self.assertEqual(tree.size(), 10, "Tree size should be 10")

    def test_contains(self):
        tree = TreeSet(Person)
        person = Person("Person1", 10)
        tree.add(person)
        self.assertTrue(tree.contains(person), "Tree should contain the added element")

    def test_not_contains(self):
        tree = TreeSet(Person)
        person1 = Person("Person1", 10)
        person2 = Person("Person2", 20)
        tree.add(person1)
        self.assertFalse(tree.contains(person2), "Tree should not contain an element that was not added")

    def test_first_last(self):
        tree = TreeSet(Person)
        items = [Person(f"Person{num}", num*10) for num in range(10)]
        for item in items:
            tree.add(item)
        self.assertEqual(tree.first(), items[0], "First element should be Person0")
        self.assertEqual(tree.last(), items[-1], "Last element should be Person9")

    def test_poll_first_last(self):
        tree = TreeSet(Person)
        items = [Person(f"Person{num}", num*10) for num in range(10)]
        for item in items:
            tree.add(item)
        self.assertEqual(tree.poll_first(), items[0], "Poll first should return Person0")
        self.assertEqual(tree.poll_last(), items[-1], "Poll last should return Person9")


if __name__ == '__main__':
    unittest.main()
