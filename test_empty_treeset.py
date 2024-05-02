import unittest
from TreeSet import *
from treeset_exceptions import *


class TestEmptyTreeSet(unittest.TestCase):
    def setUp(self) -> None:
        self.tree_type = int
        self.tree =  TreeSet(self.tree_type)

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
        with self.assertRaises(AssertionError):
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
        with self.assertRaises(AssertionError):
            self.tree.add_all([str(num) for num in range(10)])

    def test_add_single_element(self):
            """Tests adding a single element to an empty TreeSet."""
            self.tree_set.add(10)
            self.assertEqual(self.tree_set.size(), 1)
            self.assertTrue(10 in self.tree_set)

    def test_add_all_empty_sequence(self):
        """Tests adding from an empty sequence ."""
        self.tree_set.add_all([])
        self.assertEqual(self.tree_set.size(), 0)

    def test_add_all_multiple_elements(self):
            """Tests adding from a sequence with multiple elements ."""
            values = [2, 15, 5, 30, 25, 12]
            original_size = self.tree_set.size()  # Track initial size
            self.tree_set.add_all(values)

            expected_list = sorted(values)
            self.assertEqual(self.tree_set.size(), len(expected_list) + original_size)  # Consider initial size
            self.assertListEqual(list(self.tree_set), expected_list)

    def test_add_all_duplicates(self):
        """Tests adding from a sequence with duplicates."""
        values = [20, 15, 5, 30, 25, 12, 20, 15]
        original_size = self.tree_set.size()  # Track initial size
        self.tree_set.add_all(values)

        expected_list = sorted(set(values))

    def test_remove_from_empty_set(self):
        """Tests removing from an empty TreeSet."""
        self.assertFalse(self.tree_set.remove(10))
        self.assertEqual(self.tree_set.size(), 0)

    def test_remove_non_existent_element(self):
        """Tests removing a non-existent element."""
        self.tree_set.add(20)
        self.tree_set.add(30)

        self.assertFalse(self.tree_set.remove(15))
        self.assertEqual(self.tree_set.size(), 2)
        self.assertTrue(20 in self.tree_set)
        self.assertTrue(30 in self.tree_set)

    def test_remove_leaf_node(self):
        """Tests removing a leaf node."""
        self.tree_set.add(10)
        self.tree_set.add(20)

        self.assertTrue(self.tree_set.remove(10))
        self.assertEqual(self.tree_set.size(), 1)
        self.assertFalse(10 in self.tree_set)
        self.assertTrue(20 in self.tree_set)

    def test_size_empty(self):
            """Tests size of an empty set."""
            self.assertEqual(self.tree_set.size(), 0)

    def test_size_adding_one_element(self):
        """Tests size after adding one element."""
        self.tree_set.add(10)
        self.assertEqual(self.tree_set.size(), 1)

    def test_size_adding_multiple_elements(self):
        """Tests size after adding multiple elements."""

        values = TreeSet(int, [20, 4, 2, 1, 0])
        self.assertEqual(values.size(), 5)
    
    def test_is_empty_tree_empty(self):
            """Test the is_empty method for different scenarios"""
            self.assertTrue(self.tree_set.is_empty())

    def test_contains_empty_set(self):
            """Tests contains method on an empty TreeSet."""
            self.assertFalse(self.tree_set.contains(10))

    def test_ceiling_empty_set(self):
            """Test ceiling method on an empty set."""
            self.assertIsNone(self.tree_set.ceiling(10))

    def test_ceiling_empty_set(self):
            """Test ceiling method on an empty set."""
            self.assertIsNone(self.tree_set.ceiling(10))

    def test_floor_empty_set(self):
            """Test floor method on an empty set."""
            self.assertIsNone(self.tree_set.floor(10))

    def test_poll_first_empty_set(self):
            """Test pollFirst method on an empty set."""
            self.assertIsNone(self.tree_set.pollFirst())

    def test_poll_last_empty_set(self):
            """Test pollLast method on an empty set."""
            self.assertIsNone(self.tree_set.pollLast())

    def test_iterator_empty_set(self):
            """Test iterator method on an empty set."""
            elements = [elem for elem in self.tree_set.iterator()]
            self.assertListEqual(elements, [])

    def test_descending_iterator_empty_set(self):
            """Test descending_iterator method on an empty set."""
            elements = [elem for elem in self.tree_set.descending_iterator()]
            self.assertListEqual(elements, [])
    
    def test_lower_empty(self):
            """Test lower that an empty set"""
            self.assertIsNone(self.tree_set.lower(10))

    def test_higher_empty_set(self):
            """Test higher method on an empty set."""
            self.assertIsNone(self.tree_set.higher(10))

    



if __name__ == '__main__':
    unittest.main()