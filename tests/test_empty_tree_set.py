import unittest
from tree_set import *
from tree_set_exceptions import *
import random


class TestEmptyTreeSet(unittest.TestCase):
    """
    A test class for the TreeSet class when the TreeSet is empty.
    """

    def setUp(self) -> None:
        """
        Sets up the test fixture before exercising it.
        """
        self.tree_int = TreeSet(int)
        self.tree_float = TreeSet(float)
        self.tree_str = TreeSet(str)

    def test_size_int(self):
        """
        Tests the size of the empty TreeSet.
        """
        self.assertEqual(self.tree_int.size(), 0, "Size must be 0")

    def test_is_empty_int(self):
        """
        Tests if the TreeSet is empty.
        """
        self.assertTrue(self.tree_int.is_empty(), "TreeSet must be empty")

    def test_clone_int(self):
        """
        Tests the clone method on an empty TreeSet.
        """
        tree_clone = self.tree_int.clone()
        self.assertEqual(self.tree_int, tree_clone, "TreeSets must be equal")
        self.assertEqual(tree_clone.size(), 0, "Empty tree clone size must be 0")
        self.assertTrue(self.tree_int.is_empty(), "Cloned tree must be empty")

    def test_first_int(self):
        """
        Tests the first method on an empty TreeSet.
        """
        with self.assertRaises(NoSuchElementException):
            self.tree_int.first()

    def test_last_int(self):
        """
        Tests the last method on an empty TreeSet.
        """
        with self.assertRaises(NoSuchElementException):
            self.tree_int.last()

    def test_iterator_int(self):
        """
        Tests the iterator method on an empty TreeSet.
        """
        self.assertEqual(
            [], list(self.tree_int.iterator()),
            "Wrong values given by TreeSet iterator"
        )

    def test_descending_iterator_int(self):
        """
        Tests the descending_iterator method on an empty TreeSet.
        """
        self.assertEqual(
            [], list(self.tree_int.descending_iterator()),
            "Wrong values given by TreeSet descending iterator"
        )

    def test1_add_int(self):
        """
        Tests the add method on an empty TreeSet with a valid value.
        """
        self.tree_int.add(1)
        self.assertEqual(self.tree_int.size(), 1, "Size must be 1 after adding 1 value")
        self.assertEqual(self.tree_int.first(), 1, "First value must be 1")
        self.assertEqual(self.tree_int.last(), 1, "Last value must be 1")
        self.assertTrue(self.tree_int.contains(1), "Wrong value for TreeSet contains")
        self.assertFalse(self.tree_int.is_empty(), "TreeSet must not be empty after adding 1 value")
        self.assertFalse(self.tree_int.add(1), "add must return False if the value is already in the TreeSet")
        self.assertEqual(self.tree_int.size(), 1, "Size must be 1 after adding 1 value twice")

    def test2_add_int(self):
        """
        Tests the add method on an empty TreeSet with an invalid value.
        """
        with self.assertRaises(TypeError):
            self.tree_int.add("1")

    def test1_add_all_int(self):
        """
        Tests the add_all method on an empty TreeSet with a valid list of values.
        """
        self.assertTrue(self.tree_int.add_all([num for num in range(10)]), "add_all must return True if all values have been added")
        self.assertEqual(self.tree_int.size(), 10, "Size must be 10 after adding 10 value")
        self.assertEqual(self.tree_int.first(), 0, "First value must be 0")
        self.assertEqual(self.tree_int.last(), 9, "Last value must be 9")

        for num in range(10):
            self.assertTrue(self.tree_int.contains(num), "Wrong value for TreeSet contains")

        self.assertFalse(self.tree_int.is_empty(), "TreeSet must not be empty after adding 10 value")
        self.assertFalse(self.tree_int.add_all([num for num in range(5)] + [num for num in range(10, 15)]), "add_all must return False if all values have been added")
        self.assertEqual(self.tree_int.size(), 15, "Size must be 15 after adding 5 new values")

    def test2_add_all_int(self):
        """
        Tests the add_all method on an empty TreeSet with an invalid list of values.
        """
        with self.assertRaises(TypeError):
            self.tree_int.add_all([str(num) for num in range(10)])

    def test3_add_all_int(self):
        """
        Tests the add_all method on an empty TreeSet with a list of mixed valid and invalid values.
        """
        with self.assertRaises(TypeError):
            TreeSet(int, [str(num) if num % 2 == 0 else num for num in range(10)])

    def test_add_none_int(self):
        """
        Tests the add method on an empty TreeSet with a None value.
        """
        with self.assertRaises(NullPointerException):
            self.tree_int.add(None)

    def test_add_all_none_int(self):
        """
        Tests the add_all method on an empty TreeSet with a list containing None.
        """
        with self.assertRaises(NullPointerException):
            self.tree_int.add_all([1, None, 2])

    def test_add_all_not_list_int(self):
        """
        Tests the add_all method on an empty TreeSet with a non-list object.
        """
        with self.assertRaises(TypeError):
            self.tree_int.add_all(1)

    def test1_contains_int(self):
        """
        Tests the contains method on an empty TreeSet with a value that has not been added.
        """
        self.assertFalse(self.tree_int.contains(1), "TreeSet should not contain a value that has not been added")

    def test2_contains_int(self):
        """
        Tests the contains method on an empty TreeSet with a None value.
        """
        with self.assertRaises(NullPointerException):
            self.tree_int.contains(None)

    def test_poll_first_int(self):
        """
        Tests the poll_first method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_int.poll_first(), "poll_first must return None on an empty TreeSet")

    def test_poll_last_int(self):
        """
        Tests the poll_last method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_int.poll_last(), "poll_last must return None on an empty TreeSet")

    def test_floor_int(self):
        """
        Tests the floor method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_int.floor(1))

    def test_ceiling_int(self):
        """
        Tests the ceiling method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_int.ceiling(1))

    def test_higher_int(self):
        """
        Tests the higher method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_int.higher(1))

    def test_lower_int(self):
        """
        Tests the lower method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_int.lower(1))

    def test_size_str(self):
        """
        Tests the size of the empty TreeSet.
        """
        self.assertEqual(self.tree_str.size(), 0, "Size must be 0")

    def test_is_empty_str(self):
        """
        Tests if the TreeSet is empty.
        """
        self.assertTrue(self.tree_str.is_empty(), "TreeSet must be empty")

    def test_clone_str(self):
        """
        Tests the clone method on an empty TreeSet.
        """
        tree_clone = self.tree_str.clone()
        self.assertEqual(self.tree_str, tree_clone, "TreeSets must be equal")
        self.assertEqual(tree_clone.size(), 0, "Empty tree clone size must be 0")
        self.assertTrue(self.tree_str.is_empty(), "Cloned tree must be empty")

    def test_first_str(self):
        """
        Tests the first method on an empty TreeSet.
        """
        with self.assertRaises(NoSuchElementException):
            self.tree_str.first()

    def test_last_str(self):
        """
        Tests the last method on an empty TreeSet.
        """
        with self.assertRaises(NoSuchElementException):
            self.tree_str.last()

    def test_iterator_str(self):
        """
        Tests the iterator method on an empty TreeSet.
        """
        self.assertEqual(
            [], [value for value in self.tree_str.iterator()],
            "Wrong values given by TreeSet iterator"
        )

    def test_descending_iterator_str(self):
        """
        Tests the descending_iterator method on an empty TreeSet.
        """
        self.assertEqual(
            [], [value for value in self.tree_str.descending_iterator()],
            "Wrong values given by TreeSet descending iterator"
        )

    def test1_add_str(self):
        """
        Tests the add method on an empty TreeSet with a valid value.
        """
        self.tree_str.add("1")
        self.assertEqual(self.tree_str.size(), 1, "Size must be 1 after adding 1 value")
        self.assertEqual(self.tree_str.first(), "1", "First value must be '1'")
        self.assertEqual(self.tree_str.last(), "1", "Last value must be '1'")
        self.assertTrue(self.tree_str.contains("1"), "Wrong value for TreeSet contains")
        self.assertFalse(self.tree_str.is_empty(), "TreeSet must not be empty after adding 1 value")

    def test2_add_str(self):
        """
        Tests the add method on an empty TreeSet with an invalid value.
        """
        with self.assertRaises(TypeError):
            self.tree_str.add(1)

    def test1_add_all_str(self):
        """
        Tests the add_all method on an empty TreeSet with a valid list of values.
        """
        self.tree_str.add_all([str(num) for num in range(10)])
        self.assertEqual(self.tree_str.size(), 10, "Size must be 10 after adding 10 value")
        self.assertEqual(self.tree_str.first(), "0", "First value must be 0")
        self.assertEqual(self.tree_str.last(), "9", "Last value must be 9")

        for num in range(10):
            self.assertTrue(self.tree_str.contains(str(num)), "Wrong value for TreeSet contains")

        self.assertFalse(self.tree_str.is_empty(), "TreeSet must not be empty after adding 10 value")

    def test2_add_all_str(self):
        """
        Tests the add_all method on an empty TreeSet with an invalid list of values.
        """
        with self.assertRaises(TypeError):
            self.tree_str.add_all([num for num in range(10)])

    def test3_add_all_str(self):
        """
        Tests the add_all method on an empty TreeSet with a list of mixed valid and invalid values.
        """
        with self.assertRaises(TypeError):
            TreeSet(int, [str(num) if num % 2 == 0 else num for num in range(10)])

    def test_add_none_str(self):
        """
        Tests the add method on an empty TreeSet with a None value.
        """
        with self.assertRaises(NullPointerException):
            self.tree_str.add(None)

    def test_add_all_none_str(self):
        """
        Tests the add_all method on an empty TreeSet with a list containing None.
        """
        with self.assertRaises(TypeError):
            self.tree_str.add_all([2, "1", None])

        self.assertEqual(self.tree_str.size(), 0, "Size must be 0 after calling add_all with a list containing some non allowed types")
        self.assertTrue(self.tree_str.is_empty(), "TreeSet must be empty after calling add_all with a list containing some non allowed types")

    def test_add_all_not_list_str(self):
        """
        Tests the add_all method on an empty TreeSet with a non-list object.
        """
        with self.assertRaises(TypeError):
            self.tree_str.add_all(1)

    def test1_contains_str(self):
        """
        Tests the contains method on an empty TreeSet with a value that has not been added.
        """
        self.assertFalse(self.tree_str.contains("1"), "TreeSet should not contain a value that has not been added")

    def test2_contains_str(self):
        """
        Tests the contains method on an empty TreeSet with a None value.
        """
        with self.assertRaises(NullPointerException):
            self.tree_str.contains(None)

    def test_poll_first_str(self):
        """
        Tests the poll_first method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_str.poll_first(), "poll_first must return None on an empty TreeSet")

    def test_poll_last_str(self):
        """
        Tests the poll_last method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_str.poll_last(), "poll_last must return None on an empty TreeSet")

    def test_floor_str(self):
        """
        Tests the floor method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_str.floor("1"))

    def test_ceiling_str(self):
        """
        Tests the ceiling method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_str.ceiling("1"))

    def test_higher_str(self):
        """
        Tests the higher method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_str.higher("1"))

    def test_lower_str(self):
        """
        Tests the lower method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_str.lower("1"))

    def test2_add_float(self):
        """
        Tests the add method on an empty TreeSet with an invalid value.
        """
        with self.assertRaises(TypeError):
            self.tree_float.add(1)

    def test1_add_all_float(self):
        """
        Tests the add_all method on an empty TreeSet with a valid list of values.
        """
        self.tree_float.add_all(items := [num + random.random() for num in range(10)])
        self.assertEqual(self.tree_float.size(), 10, "Size must be 10 after adding 10 value")
        self.assertEqual(self.tree_float.first(), min(items), f"First value must be {min(items)}")
        self.assertEqual(self.tree_float.last(), max(items), f"Last value must be {max(items)}")

        for num in items:
            self.assertTrue(self.tree_float.contains(num), "Wrong value for TreeSet contains")

        self.assertFalse(self.tree_float.is_empty(), "TreeSet must not be empty after adding 10 value")

    def test2_add_all_float(self):
        """
        Tests the add_all method on an empty TreeSet with an invalid list of values.
        """
        with self.assertRaises(TypeError):
            self.tree_float.add_all([num for num in range(10)])

    def test3_add_all_float(self):
        """
        Tests the add_all method on an empty TreeSet with a list of mixed valid and invalid values.
        """
        with self.assertRaises(TypeError):
            TreeSet(int, [str(num) if num % 2 == 0 else num for num in range(10)])

    def test_add_none_float(self):
        """
        Tests the add method on an empty TreeSet with a None value.
        """
        with self.assertRaises(NullPointerException):
            self.tree_float.add(None)

    def test_add_all_none_float(self):
        """
        Tests the add_all method on an empty TreeSet with a list containing None.
        """
        with self.assertRaises(TypeError):
            self.tree_float.add_all([2.2, "1", None])

        self.assertEqual(self.tree_float.size(), 0, "Size must be 0 after calling add_all with a list containing some non allowed types")
        self.assertTrue(self.tree_float.is_empty(), "TreeSet must be empty after calling add_all with a list containing some non allowed types")

    def test_add_all_not_list_float(self):
        """
        Tests the add_all method on an empty TreeSet with a non-list object.
        """
        with self.assertRaises(TypeError):
            self.tree_float.add_all(1)

    def test1_contains_float(self):
        """
        Tests the contains method on an empty TreeSet with a value that has not been added.
        """
        self.assertFalse(self.tree_float.contains(1.1), "TreeSet should not contain a value that has not been added")

    def test2_contains_float(self):
        """
        Tests the contains method on an empty TreeSet with a None value.
        """
        with self.assertRaises(NullPointerException):
            self.tree_float.contains(None)

    def test_poll_first_float(self):
        """
        Tests the poll_first method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_float.poll_first(), "poll_first must return None on an empty TreeSet")

    def test_poll_last_float(self):
        """
        Tests the poll_last method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_float.poll_last(), "poll_last must return None on an empty TreeSet")

    def test_floor_float(self):
        """
        Tests the floor method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_float.floor(1.1))

    def test_ceiling_float(self):
        """
        Tests the ceiling method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_float.ceiling(1.1))

    def test_higher_float(self):
        """
        Tests the higher method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_float.higher(1.1))

    def test_lower_float(self):
        """
        Tests the lower method on an empty TreeSet.
        """
        self.assertIsNone(self.tree_float.lower(1.1))


if __name__ == '__main__':
    unittest.main()
