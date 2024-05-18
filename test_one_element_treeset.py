
import unittest

from Person import *
from TreeSet import *


class TestInt(unittest.TestCase):
        def setUp(self):
            self.tree_set_int = TreeSet(int)
            self.tree_set_str = TreeSet(str)
            self.tree_set_P = TreeSet(Person)
            self.person_test = Person("Name", "Surname", 20, "12345678A")
            self.person_test2 = Person("Name2", "Surname2", 10, "12345678B")
            self.person_test3 = Person("Name2", "Surname2", 30, "12345678C")
            self.person_test4 = Person("Name2", "Surname2", 30, "12345678D")
            self.person_test5 = Person("Name2", "Surname2", 30, "12345678E")
            self.person_test6 = Person("Name2", "Surname2", 30, "12345678F")
            self.tree_set_P3 = TreeSet(Person_HalfComparable)
            self.person_test_HC = Person_HalfComparable("Name", "Surname", 20, "12345678A")
            self.person_test2_HC = Person_HalfComparable("Name2", "Surname2", 10, "12345678B")
            self.person_test3_HC = Person_HalfComparable("Name2", "Surname2", 30, "12345678C")

        #------------------------TESTS INT------------------

        def test_clone_one_element_int(self):
            """Tests cloning  one element TreeSet."""
            self.tree_set_int.add(10)
            cloned_tree_set_int = self.tree_set_int.clone()
            self.assertEqual(self.tree_set_int.size(), cloned_tree_set_int.size())
            for value in self.tree_set_int:
                self.assertTrue(cloned_tree_set_int.contains(value))

        def test_contains_single_element_int(self):
            """Tests contains method on a TreeSet with a single element."""
            self.tree_set_int.add(10)
            self.assertTrue(self.tree_set_int.contains(10))
            self.assertFalse(self.tree_set_int.contains(20))

        def test_iterator_single_element_int(self):
            """Test iterator method with a single element."""
            self.tree_set_int.add(10)
            elements = [elem for elem in self.tree_set_int.iterator()]
            self.assertListEqual(elements, [10])

        def test_descending_iterator_single_element_int(self):
            """Test descending_iterator method with a single element."""
            self.tree_set_int.add(10)
            elements = [elem for elem in self.tree_set_int.descending_iterator()]
            self.assertListEqual(elements, [10])

        def test_poll_last_single_element_set_int(self):
            """Test poll_last method on a set with a single element."""
            self.tree_set_int.add(5)
            self.assertEqual(self.tree_set_int.poll_last(), 5)
            self.assertEqual(self.tree_set_int.size(), 0)
            self.assertEqual(list(self.tree_set_int), [])

        def test_poll_first_single_element_set_int(self):
            """Test poll_first method on a set with a single element."""
            self.tree_set_int.add(5)
            self.assertEqual(self.tree_set_int.poll_first(), 5)
            self.assertEqual(self.tree_set_int.size(), 0)
            self.assertEqual(list(self.tree_set_int), [])

        #--------------------TESTS PERSON------------------

        def test_clone_one_element_Person(self):
            """Tests cloning  one element TreeSet."""
            self.tree_set_P.add(self.person_test)
            cloned_tree_set_P = self.tree_set_P.clone()
            self.assertEqual(self.tree_set_P.size(), cloned_tree_set_P.size())
            for value in self.tree_set_P:
                self.assertTrue(cloned_tree_set_P.contains(value))

        def test_contains_single_element_Person(self):
            """Tests contains method on a TreeSet with a single element."""
            self.tree_set_P.add(self.person_test)
            self.assertTrue(self.tree_set_P.contains(self.person_test))
            self.assertFalse(self.tree_set_P.contains(self.person_test2))

        def test_poll_first_single_element_set_Person(self):
            """Test pollFirst method on a set with a single element."""
            self.tree_set_P.add(self.person_test)
            self.assertEqual(self.tree_set_P.poll_first(), self.person_test)
            self.assertEqual(self.tree_set_P.size(), 0)
            self.assertEqual(list(self.tree_set_P), [])

        def test_poll_last_single_element_set_Person(self):
            """Test poll_last method on a set with a single element."""
            self.tree_set_P.add(self.person_test)
            self.assertEqual(self.tree_set_P.poll_last(), self.person_test)
            self.assertEqual(self.tree_set_P.size(), 0)
            self.assertEqual(list(self.tree_set_P), [])

        def test_iterator_single_element_Person(self):
            """Test iterator method with a single element."""
            self.tree_set_P.add(self.person_test)
            elements = [elem for elem in self.tree_set_P.iterator()]
            self.assertListEqual(elements, [self.person_test])

        def test_descending_iterator_single_element_Person(self):
            """Test descending_iterator method with a single element."""
            self.tree_set_P.add(self.person_test)
            elements = [elem for elem in self.tree_set_P.descending_iterator()]
            self.assertListEqual(elements, [self.person_test])

        #------------------------TESTS STR------------------

        def test_clone_one_element_str(self):
            """Tests cloning  one element TreeSet."""
            self.tree_set_str.add("C")
            cloned_tree_set_str = self.tree_set_str.clone()
            self.assertEqual(self.tree_set_str.size(), cloned_tree_set_str.size())
            for value in self.tree_set_str:
                self.assertTrue(cloned_tree_set_str.contains(value))

        def test_contains_single_element_str(self):
            """Tests contains method on a TreeSet with a single element."""
            self.tree_set_str.add("C")
            self.assertTrue(self.tree_set_str.contains("C"))
            self.assertFalse(self.tree_set_str.contains("E"))

        def test_poll_first_single_element_set_str(self):
            """Test poll_first method on a set with a single element."""
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str.poll_first(), "A")
            self.assertEqual(self.tree_set_str.size(), 0)
            self.assertEqual(list(self.tree_set_str), [])

        def test_poll_last_single_element_set_str(self):
            """Test poll_last method on a set with a single element."""
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str.poll_last(), "A")
            self.assertEqual(self.tree_set_str.size(), 0)
            self.assertEqual(list(self.tree_set_str), [])

        def test_iterator_single_element_str(self):
            """Test iterator method with a single element."""
            self.tree_set_str.add("A")
            elements = [elem for elem in self.tree_set_str.iterator()]
            self.assertListEqual(elements, ["A"])

        def test_descending_iterator_single_element_str(self):
            """Test descending_iterator method with a single element."""
            self.tree_set_str.add("A")
            elements = [elem for elem in self.tree_set_str.descending_iterator()]
            self.assertListEqual(elements, ["A"])


if __name__ == '__main__':
    unittest.main()
