
import unittest

from Person import Person
from TreeSet import *


class TestPerson(unittest.TestCase):
        def setUp(self):
            self.tree_set_P = TreeSet(Person)
            self.person_test = Person("Name", "Surname", 20, "12345678A")
            self.person_test2 = Person("Name2", "Surname2", 10, "12345678X")
            self.person_test3 = Person("Name2", "Surname2", 30, "12345678B")

        def test_add_single_element(self):
                """Tests adding a single element to an empty TreeSet."""
                self.tree_set_P.add(self.person_test)
                self.assertEqual(self.tree_set_P.size(), 1)
                self.assertTrue(self.person_test in self.tree_set_P)

        def test_add_all_empty_sequence(self):
            """Tests adding from an empty sequence ."""
            self.tree_set_P.add_all([])
            self.assertEqual(self.tree_set_P.size(), 0)

        def test_add_all_multiple_elements(self):
                """Tests adding from a sequence with multiple elements ."""
                values = [self.person_test, self.person_test2, self.person_test3]
                original_size = self.tree_set_P.size()  # Track initial size
                self.tree_set_P.add_all(values)

                expected_list = sorted(values)
                self.assertEqual(self.tree_set_P.size(), len(expected_list) + original_size)  # Consider initial size
                self.assertListEqual(list(self.tree_set_P), expected_list)

        def test_add_all_duplicates(self):
            """Tests adding from a sequence with duplicates."""
            values = [self.person_test, self.person_test2, self.person_test3, self.person_test3, self.person_test]
            original_size = self.tree_set_P.size()  # Track initial size
            self.tree_set_P.add_all(values)

            expected_list = sorted(set(values))

        def test_remove_from_empty_set(self):
            """Tests removing from an empty TreeSet."""
            self.assertFalse(self.tree_set_P.remove(self.person_test))
            self.assertEqual(self.tree_set_P.size(), 0)

        def test_remove_non_existent_element(self):
            """Tests removing a non-existent element."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)

            self.assertFalse(self.tree_set_P.remove(self.person_test3))
            self.assertEqual(self.tree_set_P.size(), 2)
            self.assertTrue(self.person_test in self.tree_set_P)
            self.assertTrue(self.person_test2 in self.tree_set_P)

        def test_remove_leaf_node(self):
            """Tests removing a leaf node."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)

            self.assertTrue(self.tree_set_P.remove(self.person_test))
            self.assertEqual(self.tree_set_P.size(), 1)
            self.assertFalse(self.person_test in self.tree_set_P)
            self.assertTrue(self.person_test2 in self.tree_set_P)

        def test_size_empty(self):
                """Tests size of an empty set."""
                self.assertEqual(self.tree_set_P.size(), 0)

        def test_size_adding_one_element(self):
            """Tests size after adding one element."""
            self.tree_set_P.add(self.person_test)
            self.assertEqual(self.tree_set_P.size(), 1)

        def test_size_adding_multiple_elements(self):
            """Tests size after adding multiple elements."""

            values = TreeSet(Person, [self.person_test, self.person_test2, self.person_test3])
            self.assertEqual(values.size(), 3)
        
        def test_is_empty_tree_empty(self):
                """Test the is_empty method for different scenarios"""
                self.assertTrue(self.tree_set_P.is_empty())

        def test_contains_empty_set(self):
                """Tests contains method on an empty TreeSet."""
                self.assertFalse(self.tree_set_P.contains(self.person_test))

        def test_ceiling_empty_set(self):
                """Test ceiling method on an empty set."""
                self.assertIsNone(self.tree_set_P.ceiling(self.person_test))

        def test_ceiling_empty_set(self):
                """Test ceiling method on an empty set."""
                self.assertIsNone(self.tree_set_P.ceiling(self.person_test))

        def test_floor_empty_set(self):
                """Test floor method on an empty set."""
                self.assertIsNone(self.tree_set_P.floor(self.person_test))

        def test_poll_first_empty_set(self):
                """Test pollFirst method on an empty set."""
                self.assertIsNone(self.tree_set_P.pollFirst())

        def test_poll_last_empty_set(self):
                """Test pollLast method on an empty set."""
                self.assertIsNone(self.tree_set_P.pollLast())

        def test_iterator_empty_set(self):
                """Test iterator method on an empty set."""
                elements = [elem for elem in self.tree_set_P.iterator()]
                self.assertListEqual(elements, [])

        def test_descending_iterator_empty_set(self):
                """Test descending_iterator method on an empty set."""
                elements = [elem for elem in self.tree_set_P.descending_iterator()]
                self.assertListEqual(elements, [])
        
        def test_lower_empty(self):
                """Test lower that an empty set"""
                self.assertIsNone(self.tree_set_P.lower(self.person_test))

        def test_higher_empty_set(self):
                """Test higher method on an empty set."""
                self.assertIsNone(self.tree_set_P.higher(self.person_test))



if __name__ == '__main__':
    unittest.main()
