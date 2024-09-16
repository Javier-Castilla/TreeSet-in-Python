
import unittest

from tests_classes import *
from tree_set import *


class TestInt(unittest.TestCase):
    def setUp(self):
        self.tree_int = TreeSet(int, [10])
        self.tree_str = TreeSet(str, ["A"])
        self.tree_person = TreeSet(Person, [Person("John", 20)])

    def test_size_int(self):
        self.assertEqual(self.tree_int.size(), 1, "Size of tree is not 1")

    def test_is_empty_int(self):
        self.assertFalse(self.tree_int.is_empty(), "Tree is empty")

    def test_clone_int(self):
        self.assertEqual(self.tree_int.clone().size(), 1, "Clone size is not 1")

    def test_first_int(self):
        self.assertEqual(self.tree_int.first(), 10, "First element is not 10")

    def test_last_int(self):
        self.assertEqual(self.tree_int.last(), 10, "Last element is not 10")

    def test_iterator_int(self):
        self.assertEqual(next(self.tree_int.iterator()), 10, "Iterator element is not 10")

    def test_descending_iterator_int(self):
        self.assertEqual(next(self.tree_int.descending_iterator()), 10, "Descending iterator element is not 10")

    def tes1_add_int(self):
        self.tree_int.add(5)
        self.assertEqual(self.tree_int.size(), 2, "Size of tree is not 2")
        self.assertEqual(self.tree_int.first(), 5, "First element is not 5")
        self.assertEqual(self.tree_int.last(), 10, "Last element is not 10")
        self.assertTrue(self.tree_int.contains(5), "Tree does not contain 5")
        self.assertFalse(self.tree_int.is_empty(), "Tree is empty")

    def test2_add_int(self):
        with self.assertRaises(TypeError):
            self.tree_int.add("10")

    def test1_add_all_int(self):
        self.tree_int.add_all([num for num in range(10)])
        self.assertEqual(self.tree_int.size(), 11, "Size of tree is not 10")
        self.assertEqual(self.tree_int.first(), 0, "First element is not 0")
        self.assertEqual(self.tree_int.last(), 10, "Last element is not 10")

    def test2_add_all_int(self):
        with self.assertRaises(TypeError):
            self.tree_int.add_all([str(num) for num in range(10)])

    def test3_add_all_int(self):
        with self.assertRaises(TypeError):
            self.tree_int.add_all([str(num) if num % 2 == 0 else num for num in range(10)])

    def test_add_none_int(self):
        with self.assertRaises(NullPointerException):
            self.tree_int.add(None)

    def test_add_all_none_int(self):
        with self.assertRaises(NullPointerException):
            self.tree_int.add_all([None])

    def test1_contains_int(self):
        self.assertTrue(self.tree_int.contains(10), "Tree does not contain 10")
        self.assertFalse(self.tree_int.contains(5), "Tree contains 5")

    def test2_contains_int(self):
        with self.assertRaises(NullPointerException):
            self.tree_int.contains(None)

    def test_poll_first_int(self):
        self.assertEqual(self.tree_int.poll_first(), 10, "First element is not 10")
        self.assertEqual(self.tree_int.size(), 0, "Size of tree is not 0")
        self.assertTrue(self.tree_int.is_empty(), "Tree is not empty")

    def test_poll_last_int(self):
        self.assertEqual(self.tree_int.poll_last(), 10, "Last element is not 10")
        self.assertEqual(self.tree_int.size(), 0, "Size of tree is not 0")
        self.assertTrue(self.tree_int.is_empty(), "Tree is not empty")

    def test_floor_int(self):
        self.assertEqual(self.tree_int.floor(10), 10, "Floor element is not 10")
        self.assertIsNone(self.tree_int.floor(5), "Floor element is not None")


if __name__ == '__main__':
    unittest.main()