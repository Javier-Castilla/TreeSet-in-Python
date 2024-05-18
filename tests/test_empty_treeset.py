import unittest
from TreeSet import *
from treeset_exceptions import *


class TestEmptyTreeSet(unittest.TestCase):
    """
    A test class for the TreeSet class when the TreeSet is empty.
    """

    def setUp(self) -> None:
        """
        Sets up the test fixture before exercising it.
        """
        self.tree_type = int
        self.tree = TreeSet(self.tree_type)

    def test_size(self):
        """
        Tests the size of the empty TreeSet.
        """
        self.assertEqual(self.tree.size(), 0, "Size must be 0")

    def test_is_empty(self):
        """
        Tests if the TreeSet is empty.
        """
        self.assertTrue(self.tree.is_empty(), "TreeSet must be empty")

    def test_clone(self):
        """
        Tests the clone method on an empty TreeSet.
        """
        tree_clone = self.tree.clone()
        self.assertEqual(self.tree, tree_clone, "TreeSets must be equal")
        self.assertEqual(tree_clone.size(), 0, "Empty tree clone size must be 0")
        self.assertTrue(self.tree.is_empty(), "Cloned tree must be empty")

    def test_first(self):
        """
        Tests the first method on an empty TreeSet.
        """
        with self.assertRaises(NoSuchElementError):
            self.tree.first()

    def test_last(self):
        """
        Tests the last method on an empty TreeSet.
        """
        with self.assertRaises(NoSuchElementError):
            self.tree.last()

    def test_iterator(self):
        """
        Tests the iterator method on an empty TreeSet.
        """
        self.assertEqual(
            [], [value for value in self.tree.iterator()],
            "Wrong values given by TreeSet iterator"
        )

    def test_descending_iterator(self):
        """
        Tests the descending_iterator method on an empty TreeSet.
        """
        self.assertEqual(
            [], [value for value in self.tree.descending_iterator()],
            "Wrong values given by TreeSet descending iterator"
        )

    def test1_add(self):
        """
        Tests the add method on an empty TreeSet with a valid value.
        """
        self.tree.add(1)
        self.assertEqual(self.tree.size(), 1, "Size must be 1 after adding 1 value")
        self.assertEqual(self.tree.first(), 1, "First value must be 1")
        self.assertEqual(self.tree.last(), 1, "Last value must be 1")
        self.assertTrue(self.tree.contains(1), "Wrong value for TreeSet contains")
        self.assertFalse(self.tree.is_empty(), "TreeSet must not be empty after adding 1 value")

    def test2_add(self):
        """
        Tests the add method on an empty TreeSet with an invalid value.
        """
        with self.assertRaises(TypeError):
            self.tree.add("1")

    def test1_add_all(self):
        """
        Tests the add_all method on an empty TreeSet with a valid list of values.
        """
        self.tree.add_all([num for num in range(10)])
        self.assertEqual(self.tree.size(), 10, "Size must be 10 after adding 10 value")
        self.assertEqual(self.tree.first(), 0, "First value must be 0")
        self.assertEqual(self.tree.last(), 9, "Last value must be 9")

        for num in range(10):
            self.assertTrue(self.tree.contains(num), "Wrong value for TreeSet contains")

        self.assertFalse(self.tree.is_empty(), "TreeSet must not be empty after adding 10 value")

    def test2_add_all(self):
        """
        Tests the add_all method on an empty TreeSet with an invalid list of values.
        """
        with self.assertRaises(TypeError):
            self.tree.add_all([str(num) for num in range(10)])

    def test3_add_all(self):
        """
        Tests the add_all method on an empty TreeSet with a list of mixed valid and invalid values.
        """
        with self.assertRaises(TypeError):
            TreeSet(int, [str(num) if num % 2 == 0 else num for num in range(10)])

    def test_add_none(self):
        """
        Tests the add method on an empty TreeSet with a None value.
        """
        with self.assertRaises(TypeError):
            self.tree.add(None)

    def test_add_all_none(self):
        """
        Tests the add_all method on an empty TreeSet with a list containing None.
        """
        with self.assertRaises(TypeError):
            self.tree.add_all([1, None, 2])

    def test_add_all_not_list(self):
        """
        Tests the add_all method on an empty TreeSet with a non-list object.
        """
        with self.assertRaises(TypeError):
            self.tree.add_all(1)

    def test1_contains(self):
        """
        Tests the contains method on an empty TreeSet with a value that has not been added.
        """
        self.assertFalse(self.tree.contains(1), "TreeSet should not contain a value that has not been added")

    def test2_contains(self):
        """
        Tests the contains method on an empty TreeSet with a None value.
        """
        with self.assertRaises(TypeError):
            self.tree.contains(None)

    def test_poll_first(self):
        """
        Tests the poll_first method on an empty TreeSet.
        """
        with self.assertRaises(NoSuchElementError):
            self.tree.poll_first()

    def test_poll_last(self):
        """
        Tests the poll_last method on an empty TreeSet.
        """
        with self.assertRaises(NoSuchElementError):
            self.tree.poll_last()

    def test_floor(self):
        """
        Tests the floor method on an empty TreeSet.
        """
        self.assertIsNone(self.tree.floor(1))

    def test_ceiling(self):
        """
        Tests the ceiling method on an empty TreeSet.
        """
        self.assertIsNone(self.tree.ceiling(1))

    def test_higher(self):
        """
        Tests the higher method on an empty TreeSet.
        """
        self.assertIsNone(self.tree.higher(1))

    def test_lower(self):
        """
        Tests the lower method on an empty TreeSet.
        """
        self.assertIsNone(self.tree.lower(1))


if __name__ == '__main__':
    unittest.main()
