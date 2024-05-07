import unittest
from TreeSet import *
from treeset_exceptions import *


class TestEmptyTreeSet(unittest.TestCase):
    def setUp(self) -> None:
        self.tree_type = int
        self.tree = TreeSet(self.tree_type)

    def test_size(self):
        self.assertEqual(self.tree.size(), 0, "Size must be 0")

    def test_is_empty(self):
        self.assertTrue(self.tree.is_empty(), "TreeSet must be empty")

    def test_clone(self):
        tree_clone = self.tree.clone()
        self.assertEqual(self.tree, tree_clone, "TreeSets must be equal")
        self.assertEqual(tree_clone.size(), 0, "Empty tree clone size must be 0")
        self.assertTrue(self.tree.is_empty(), "Cloned tree must be empty")

    def test_first(self):
        with self.assertRaises(NoSuchElementError):
            self.tree.first()

    def test_last(self):
        with self.assertRaises(NoSuchElementError):
            self.tree.last()

    def test_iterator(self):
        self.assertEqual(
            [], [value for value in self.tree.iterator()],
            "Wrong values given by TreeSet iterator"
        )

    def test_descending_iterator(self):
        self.assertEqual(
            [], [value for value in self.tree.descending_iterator()],
            "Wrong values given by TreeSet descending iterator"
        )

    def test1_add(self):
        self.tree.add(1)
        self.assertEqual(self.tree.size(), 1, "Size must be 1 after adding 1 value")
        self.assertEqual(self.tree.first(), 1, "First value must be 1")
        self.assertEqual(self.tree.last(), 1, "Last value must be 1")
        self.assertTrue(self.tree.contains(1), "Wrong value for TreeSet contains")
        self.assertFalse(self.tree.is_empty(), "TreeSet must not be empty after adding 1 value")

    def test2_add(self):
        with self.assertRaises(TypeError):
            self.tree.add("1")

    def test1_add_all(self):
        self.tree.add_all([num for num in range(10)])
        self.assertEqual(self.tree.size(), 10, "Size must be 10 after adding 10 value")
        self.assertEqual(self.tree.first(), 0, "First value must be 1")
        self.assertEqual(self.tree.last(), 9, "Last value must be 9")

        for num in range(10):
            self.assertTrue(self.tree.contains(num), "Wrong value for TreeSet contains")

        self.assertFalse(self.tree.is_empty(), "TreeSet must not be empty after adding 10 value")

    def test2_add_all(self):
        with self.assertRaises(TypeError):
            self.tree.add_all([str(num) for num in range(10)])

    def test3_add_all(self):
        with self.assertRaises(TypeError):
            TreeSet(int, [str(num) if num % 2 == 0 else num for num in range(10)])

if __name__ == '__main__':
    unittest.main()
