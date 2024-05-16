import unittest

from TreeSet import TreeSet
from treeset_exceptions import *
from Person import *


class TestEmptyTreeSet(unittest.TestCase):
        def setUp(self):
                self.tree_type = int
                self.tree =  TreeSet(self.tree_type)
                self.tree_set = TreeSet(int)
                self.tree_set_P = TreeSet(Person)
                self.person_test = Person("Name", "Surname", 20, "12345678A")
                self.person_test2 = Person("Name2", "Surname2", 10, "12345678X")
                self.person_test3 = Person("Name2", "Surname2", 30, "12345678B")
                self.tree_set_str = TreeSet(str)

        #------------------------TESTS INT------------------

        def test_add_single_element_int(self):
                """Tests adding a single element to an empty TreeSet."""
                self.tree_set.add(10)
                self.assertEqual(self.tree_set.size(), 1)
                self.assertTrue(10 in self.tree_set)

        def test_add_all_empty_sequence_int(self):
                """Tests adding from an empty sequence ."""
                self.tree_set.add_all([])
                self.assertEqual(self.tree_set.size(), 0)

        def test_add_all_multiple_elements_int(self):
                """Tests adding from a sequence with multiple elements ."""
                values = [2, 15, 5, 30, 25, 12]
                original_size = self.tree_set.size()
                self.tree_set.add_all(values)

                expected_list = sorted(values)
                self.assertEqual(self.tree_set.size(), len(expected_list) + original_size)
                self.assertListEqual(list(self.tree_set), expected_list)

        def test_add_all_duplicates_int(self):
                """Tests adding from a sequence with duplicates."""
                values = [20, 15, 5, 30, 25, 12, 20, 15]
                original_size = self.tree_set.size()
                self.tree_set.add_all(values)

                expected_list = sorted(set(values))

        def test_remove_from_empty_set_int(self):
                """Tests removing from an empty TreeSet."""
                self.assertFalse(self.tree_set.remove(10))
                self.assertEqual(self.tree_set.size(), 0)

        def test_remove_non_existent_element_int(self):
                """Tests removing a non-existent element."""
                self.tree_set.add(20)
                self.tree_set.add(30)

                self.assertFalse(self.tree_set.remove(15))
                self.assertEqual(self.tree_set.size(), 2)
                self.assertTrue(20 in self.tree_set)
                self.assertTrue(30 in self.tree_set)

        def test_remove_leaf_node_int(self):
                """Tests removing a leaf node."""
                self.tree_set.add(10)
                self.tree_set.add(20)

                self.assertTrue(self.tree_set.remove(10))
                self.assertEqual(self.tree_set.size(), 1)
                self.assertFalse(10 in self.tree_set)
                self.assertTrue(20 in self.tree_set)

        def test_size_empty_int(self):
                """Tests size of an empty set."""
                self.assertEqual(self.tree_set.size(), 0)

        def test_size_adding_one_element_int(self):
                """Tests size after adding one element."""
                self.tree_set.add(10)
                self.assertEqual(self.tree_set.size(), 1)

        def test_size_adding_multiple_elements_int(self):
                """Tests size after adding multiple elements."""

                values = TreeSet(int, [20, 4, 2, 1, 0])
                self.assertEqual(values.size(), 5)

        def test_is_empty_tree_empty_int(self):
                """Test the is_empty method for different scenarios"""
                self.assertTrue(self.tree_set.is_empty())

        def test_contains_empty_set_int(self):
                """Tests contains method on an empty TreeSet."""
                self.assertFalse(self.tree_set.contains(10))

        def test_ceiling_empty_set_int(self):
                """Test ceiling method on an empty set."""
                self.assertIsNone(self.tree_set.ceiling(10))

        def test_floor_empty_set_int(self):
                """Test floor method on an empty set."""
                self.assertIsNone(self.tree_set.floor(10))

        def test_poll_first_empty_set_int(self):
                """Test poll_first method on an empty set."""
                with self.assertRaises(NoSuchElementError):
                        self.tree_set.poll_first()

        def test_poll_last_empty_set_int(self):
                """Test poll_last method on an empty set."""
                with self.assertRaises(NoSuchElementError):
                        self.tree_set.poll_last()

        def test_iterator_empty_set_int(self):
                """Test iterator method on an empty set."""
                elements = [elem for elem in self.tree_set.iterator()]
                self.assertListEqual(elements, [])

        def test_descending_iterator_empty_set_int(self):
                """Test descending_iterator method on an empty set."""
                elements = [elem for elem in self.tree_set.descending_iterator()]
                self.assertListEqual(elements, [])

        def test_lower_empty_int(self):
                """Test lower that an empty set"""
                self.assertIsNone(self.tree_set.lower(10))

        def test_higher_empty_set_int(self):
                """Test higher method on an empty set."""
                self.assertIsNone(self.tree_set.higher(10))

        def test_case_1_remove_int(self):
                """Test Case 1: Node to be removed is the root of the tree."""
                self.tree_set.add(10)
                self.tree_set.remove(10)
                tree_colors = self.tree_set._TreeSet__array_color()
                self.assertEqual(tree_colors, [])

        #--------------------TESTS PERSON------------------

        def test_add_single_element_Person(self):
                        """Tests adding a single element to an empty TreeSet."""
                        self.tree_set_P.add(self.person_test)
                        self.assertEqual(self.tree_set_P.size(), 1)
                        self.assertTrue(self.person_test in self.tree_set_P)

        def test_add_all_empty_sequence_Person(self):
                """Tests adding from an empty sequence ."""
                self.tree_set_P.add_all([])
                self.assertEqual(self.tree_set_P.size(), 0)

        def test_add_all_multiple_elements_Person(self):
                """Tests adding from a sequence with multiple elements ."""
                values = [self.person_test, self.person_test2, self.person_test3]
                original_size = self.tree_set_P.size()
                self.tree_set_P.add_all(values)

                expected_list = sorted(values)
                self.assertEqual(self.tree_set_P.size(), len(expected_list) + original_size) 
                self.assertListEqual(list(self.tree_set_P), expected_list)

        def test_add_all_duplicates_Person(self):
                """Tests adding from a sequence with duplicates."""
                values = [self.person_test, self.person_test2, self.person_test3, self.person_test3, self.person_test]
                original_size = self.tree_set_P.size()
                self.tree_set_P.add_all(values)

                expected_list = sorted(set(values))

        def test_remove_from_empty_set_Person(self):
                """Tests removing from an empty TreeSet."""
                self.assertFalse(self.tree_set_P.remove(self.person_test))
                self.assertEqual(self.tree_set_P.size(), 0)

        def test_remove_non_existent_element_Person(self):
                """Tests removing a non-existent element."""
                self.tree_set_P.add(self.person_test)
                self.tree_set_P.add(self.person_test2)

                self.assertFalse(self.tree_set_P.remove(self.person_test3))
                self.assertEqual(self.tree_set_P.size(), 2)
                self.assertTrue(self.person_test in self.tree_set_P)
                self.assertTrue(self.person_test2 in self.tree_set_P)

        def test_remove_leaf_node_Person(self):
                """Tests removing a leaf node."""
                self.tree_set_P.add(self.person_test)
                self.tree_set_P.add(self.person_test2)

                self.assertTrue(self.tree_set_P.remove(self.person_test))
                self.assertEqual(self.tree_set_P.size(), 1)
                self.assertFalse(self.person_test in self.tree_set_P)
                self.assertTrue(self.person_test2 in self.tree_set_P)

        def test_size_empty_Person(self):
                """Tests size of an empty set."""
                self.assertEqual(self.tree_set_P.size(), 0)

        def test_size_adding_one_element_Person(self):
                """Tests size after adding one element."""
                self.tree_set_P.add(self.person_test)
                self.assertEqual(self.tree_set_P.size(), 1)

        def test_size_adding_multiple_elements_Person(self):
                """Tests size after adding multiple elements."""

                values = TreeSet(Person, [self.person_test, self.person_test2, self.person_test3])
                self.assertEqual(values.size(), 3)

        def test_is_empty_tree_empty_Person(self):
                """Test the is_empty method for different scenarios"""
                self.assertTrue(self.tree_set_P.is_empty())

        def test_contains_empty_set_Person(self):
                """Tests contains method on an empty TreeSet."""
                self.assertFalse(self.tree_set_P.contains(self.person_test))

        def test_ceiling_empty_set_Person(self):
                """Test ceiling method on an empty set."""
                self.assertIsNone(self.tree_set_P.ceiling(self.person_test))

        def test_ceiling_empty_set_Person(self):
                """Test ceiling method on an empty set."""
                self.assertIsNone(self.tree_set_P.ceiling(self.person_test))

        def test_floor_empty_set_Person(self):
                """Test floor method on an empty set."""
                self.assertIsNone(self.tree_set_P.floor(self.person_test))

        def test_poll_first_empty_set_Person(self):
                """Test poll_first method on an empty set."""
                with self.assertRaises(NoSuchElementError):
                        self.tree_set_P.poll_first()

        def test_poll_last_empty_set_Person(self):
                """Test poll_last method on an empty set."""
                with self.assertRaises(NoSuchElementError):
                        self.tree_set_P.poll_last()

        def test_iterator_empty_set_Person(self):
                """Test iterator method on an empty set."""
                elements = [elem for elem in self.tree_set_P.iterator()]
                self.assertListEqual(elements, [])

        def test_descending_iterator_empty_set_Person(self):
                """Test descending_iterator method on an empty set."""
                elements = [elem for elem in self.tree_set_P.descending_iterator()]
                self.assertListEqual(elements, [])

        def test_lower_empty_Person(self):
                """Test lower that an empty set"""
                self.assertIsNone(self.tree_set_P.lower(self.person_test))

        def test_higher_empty_set_Person(self):
                """Test higher method on an empty set."""
                self.assertIsNone(self.tree_set_P.higher(self.person_test))

        def test_case_1_remove_Person(self):
                """Test Case 1: Node to be removed is the root of the tree."""
                self.tree_set_P.add(self.person_test)
                self.tree_set_P.remove(self.person_test)
                tree_colors = self.tree_set._TreeSet__array_color()
                self.assertEqual(tree_colors, [])

        #------------------------TESTS STR------------------

        def test_add_single_element_str(self):
                """Tests adding a single element to an empty TreeSet."""
                self.tree_set_str.add("A")
                self.assertEqual(self.tree_set_str.size(), 1)
                self.assertTrue("A" in self.tree_set_str)

        def test_add_all_empty_sequence_str(self):
                """Tests adding from an empty sequence ."""
                self.tree_set_str.add_all([])
                self.assertEqual(self.tree_set_str.size(), 0)

        def test_add_all_multiple_elements_str(self):
                """Tests adding from a sequence with multiple elements ."""
                values = ["C", "A", "F", "G", "I", "B"]
                original_size = self.tree_set_str.size()
                self.tree_set_str.add_all(values)

                expected_list = sorted(values)
                self.assertEqual(self.tree_set_str.size(), len(expected_list) + original_size) 
                self.assertListEqual(list(self.tree_set_str), expected_list)

        def test_add_all_duplicates_str(self):
            """Tests adding from a sequence with duplicates."""
            values = ["C", "C", "F", "F", "I", "B"]
            original_size = self.tree_set_str.size()
            self.tree_set_str.add_all(values)

            expected_list = sorted(set(values))

        def test_remove_from_empty_set_str(self):
            """Tests removing from an empty TreeSet."""
            self.assertFalse(self.tree_set_str.remove("A"))
            self.assertEqual(self.tree_set_str.size(), 0)

        def test_remove_non_existent_element_str(self):
            """Tests removing a non-existent element."""
            self.tree_set_str.add("C")
            self.tree_set_str.add("A")

            self.assertFalse(self.tree_set_str.remove("B"))
            self.assertEqual(self.tree_set_str.size(), 2)
            self.assertTrue("C" in self.tree_set_str)
            self.assertTrue("A" in self.tree_set_str)

        def test_remove_leaf_node_str(self):
            """Tests removing a leaf node."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("D")
            self.assertTrue(self.tree_set_str.remove("B"))
            self.assertEqual(self.tree_set_str.size(), 1)
            self.assertFalse("B" in self.tree_set_str)
            self.assertTrue("D" in self.tree_set_str)

        def test_size_empty_str(self):
            """Tests size of an empty set."""
            self.assertEqual(self.tree_set_str.size(), 0)

        def test_size_adding_one_element_str(self):
            """Tests size after adding one element."""
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str.size(), 1)

        def test_size_adding_multiple_elements_str(self):
            """Tests size after adding multiple elements."""

            values = TreeSet(str, ["G", "E", "C", "B", "A"])
            self.assertEqual(values.size(), 5)

        def test_is_empty_str(self):
            """Test the is_empty method for different scenarios"""
            self.assertTrue(self.tree_set_str.is_empty())
            self.tree_set_str.add_all(["N", "M", "R"])
            self.assertFalse(self.tree_set_str.is_empty())
            self.tree_set_str.remove("M")
            self.assertFalse(self.tree_set_str.is_empty())

        def test_contains_empty_set_str(self):
            """Tests contains method on an empty TreeSet."""
            self.assertFalse(self.tree_set_str.contains("B"))

        def test_ceiling_empty_set_str(self):
            """Test ceiling method on an empty set."""
            self.assertIsNone(self.tree_set_str.ceiling("A"))

        def test_floor_empty_set_str(self):
            """Test floor method on an empty set."""
            self.assertIsNone(self.tree_set_str.floor("A"))

        def test_poll_first_empty_set_str(self):
            """Test poll_first method on an empty set."""
            with self.assertRaises(NoSuchElementError):
                self.tree_set_str.poll_first()

        def test_poll_last_empty_set_str(self):
            """Test poll_last method on an empty set."""
            with self.assertRaises(NoSuchElementError):
                self.tree_set_str.poll_last()

        def test_iterator_empty_set_str(self):
            """Test iterator method on an empty set."""
            elements = [elem for elem in self.tree_set_str.iterator()]
            self.assertListEqual(elements, [])

        def test_descending_iterator_empty_set_str(self):
            """Test descending_iterator method on an empty set."""
            elements = [elem for elem in self.tree_set_str.descending_iterator()]
            self.assertListEqual(elements, [])

        def test_lower_empty_str(self):
            """Test lower that an empty set"""
            self.assertIsNone(self.tree_set_str.lower("A"))

        def test_higher_empty_set_str(self):
            """Test higher method on an empty set."""
            self.assertIsNone(self.tree_set_str.higher("A"))

        def test_case_1_remove_str(self):
            """Test Case 1: Node to be removed is the root of the tree."""
            self.tree_set_str.add("J")
            self.tree_set_str.remove("J")
            tree_colors = self.tree_set_str._TreeSet__array_color()
            self.assertEqual(tree_colors, [])




if __name__ == '__main__':
    unittest.main()