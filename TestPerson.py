
import unittest

from Person import *
from TreeSet import *


class TestPerson(unittest.TestCase):
        def setUp(self):
                self.tree_set_P = TreeSet(Person)
                self.person_test = Person("Name", "Surname", 20, "12345678A")
                self.person_test2 = Person("Name2", "Surname2", 10, "12345678B")
                self.person_test3 = Person("Name2", "Surname2", 30, "12345678C")
                self.person_test4 = Person("Name2", "Surname2", 30, "12345678D")
                self.person_test5 = Person("Name2", "Surname2", 30, "12345678E")
                self.person_test6 = Person("Name2", "Surname2", 30, "12345678F")
                self.tree_set_P2 = TreeSet(Person_NoComparable)
                self.person_test_NC = Person_NoComparable("Name", "Surname", 20, "12345678A")
                self.person_test2_NC = Person_NoComparable("Name2", "Surname2", 10, "12345678B")
                self.person_test3_NC = Person_NoComparable("Name2", "Surname2", 30, "12345678C")
            
        def test_remove_node_with_single_child_Person(self):
            """Tests removing a node with a single child."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.tree_set_P.add(self.person_test3)
            self.assertTrue(self.tree_set_P.remove(self.person_test))
            self.assertEqual(self.tree_set_P.size(), 2)

        def test_remove_node_with_two_children_Person(self):
            """Tests removing a node with two children (replaces with successor)."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.tree_set_P.add(self.person_test3)
            self.tree_set_P.add(self.person_test4)
            self.assertTrue(self.tree_set_P.remove(self.person_test))
            self.assertEqual(self.tree_set_P.size(), 3)

        def test_remove_root_node_Person(self):
            """Tests removing the root node ."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.tree_set_P.add(self.person_test3)
            self.assertTrue(self.tree_set_P.remove(self.person_test))
            self.assertEqual(self.tree_set_P.size(), 2)

        def test_clear_Person(self):
            """Tests clearing the TreeSet from all its inserted elements."""
            values = TreeSet(Person, [self.person_test, self.person_test2, self.person_test3, self.person_test4, self.person_test5])
            self.assertEqual(len(values), 5)
            values.clear()
            self.assertNotEqual(values.size(), 5)
            self.assertEqual(values.size(), 0)

        def test_clone_multiple_elements_Person(self):
            """Tests cloning  multiples elements TreeSet."""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3])
            cloned_tree_set_P = self.tree_set_P.clone()
            self.assertEqual(self.tree_set_P.size(), cloned_tree_set_P.size())
            for value in self.tree_set_P:
                self.assertTrue(cloned_tree_set_P.contains(value))
        def test_clone_one_element_Person(self):
            """Tests cloning  one element TreeSet."""
            self.tree_set_P.add(self.person_test)
            cloned_tree_set_P = self.tree_set_P.clone()
            self.assertEqual(self.tree_set_P.size(), cloned_tree_set_P.size())
            for value in self.tree_set_P:
                self.assertTrue(cloned_tree_set_P.contains(value))

        def test_is_empty_Person(self):
            """Test the is_empty method for different scenarios"""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3])
            self.assertFalse(self.tree_set_P.is_empty())
            self.tree_set_P.remove(self.person_test)
            self.assertFalse(self.tree_set_P.is_empty())

        def test_contains_single_element_Person(self):
            """Tests contains method on a TreeSet with a single element."""
            self.tree_set_P.add(self.person_test)
            self.assertTrue(self.tree_set_P.contains(self.person_test))
            self.assertFalse(self.tree_set_P.contains(self.person_test2))

        def test_contains_multiple_elements_Person(self):
            """Tests contains method on a TreeSet with multiple elements."""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3, self.person_test4, self.person_test5])
            self.assertTrue(self.tree_set_P.contains(self.person_test))
            self.assertTrue(self.tree_set_P.contains(self.person_test2))
            self.assertFalse(self.tree_set_P.contains(self.person_test6))
        
        def test_ceiling_elements_greater_equal_Person(self):
            """Test ceiling method when set contains elements greater than or equal to the given value."""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3, self.person_test4])
            self.assertEqual(self.tree_set_P.ceiling(self.person_test), self.person_test)

        def test_ceiling_elements_only_greater_Person(self):
            """Test ceiling method when set contains only elements greater than the given value."""
            self.tree_set_P.add_all([self.person_test2, self.person_test3, self.person_test4])
            self.assertEqual(self.tree_set_P.ceiling(self.person_test), self.person_test2)

        def test_ceiling_elements_only_smaller_Person(self):
            """Test ceiling method when set contains only elements smaller than the given value."""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3])
            self.assertEqual(self.tree_set_P.ceiling(self.person_test4), None)

        def test_ceiling_between_values_Person(self):
            """Test ceiling method when the value is between two values in the set."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test3)
            self.tree_set_P.add(self.person_test4)
            self.assertEqual(self.tree_set_P.ceiling(self.person_test2), self.person_test3)

        def test_floor_smaller_than_min_Person(self):
            """Test floor method when the value is smaller than the minimum value in the set."""
            self.tree_set_P.add(self.person_test2)
            self.assertEqual(self.tree_set_P.floor(self.person_test), None)

        def test_floor_equal_to_value_in_set_Person(self):
            """Test floor method when the value is equal to a value in the set."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.assertEqual(self.tree_set_P.floor(self.person_test), self.person_test)

        def test_floor_greater_than_max_Person(self):
            """Test floor method when the value is greater than the maximum value in the set."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.assertEqual(self.tree_set_P.floor(self.person_test3), self.person_test2)

        def test_floor_between_values_Person(self):
            """Test floor method when the value is between two values in the set."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test3)
            self.tree_set_P.add(self.person_test4)
            self.assertEqual(self.tree_set_P.floor(self.person_test2), self.person_test)        

        def test_poll_first_non_empty_set_Person(self):
            """Test pollFirst method on a non-empty set."""
            self.tree_set_P.add_all([self.person_test, self.person_test3, self.person_test4])
            self.assertEqual(self.tree_set_P.pollFirst(), self.person_test)
            self.assertEqual(self.tree_set_P.size(), 2)
            self.assertEqual(list(self.tree_set_P), [self.person_test3, self.person_test4])

        def test_poll_first_single_element_set_Person(self):
            """Test pollFirst method on a set with a single element."""
            self.tree_set_P.add(self.person_test)
            self.assertEqual(self.tree_set_P.pollFirst(), self.person_test)
            self.assertEqual(self.tree_set_P.size(), 0)
            self.assertEqual(list(self.tree_set_P), [])

        def test_poll_last_non_empty_set_Person(self):
            """Test pollLast method on a non-empty set."""
            self.tree_set_P.add_all([self.person_test2, self.person_test3, self.person_test4])
            self.assertEqual(self.tree_set_P.pollLast(), self.person_test4)
            self.assertEqual(self.tree_set_P.size(), 2)
            self.assertEqual(list(self.tree_set_P), [self.person_test2, self.person_test3])

        def test_poll_last_single_element_set_Person(self):
            """Test pollLast method on a set with a single element."""
            self.tree_set_P.add(self.person_test)
            self.assertEqual(self.tree_set_P.pollLast(), self.person_test)
            self.assertEqual(self.tree_set_P.size(), 0)
            self.assertEqual(list(self.tree_set_P), [])

        def test_iterator_multiple_elements_Person(self):
            """Test iterator  method for multiple elements."""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3])
            elements = [elem for elem in self.tree_set_P.iterator()]
            self.assertListEqual(elements, [self.person_test, self.person_test2, self.person_test3])

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

        def test_descending_iterator_multiples_elements_Person(self):
            """Test descending_iterator method with multiple elements."""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3])
            elements = [elem for elem in self.tree_set_P.descending_iterator()]
            self.assertListEqual(elements, [self.person_test3, self.person_test2, self.person_test])

        def test_lower_smaller_than_min_Person(self):
            """Test lower method when the value is smaller than the minimum value in the set."""
            self.tree_set_P.add(self.person_test2)
            self.assertIsNone(self.tree_set_P.lower(self.person_test))

        def test_lower_equal_to_value_in_set_Person(self):
            """Test lower method when the value is equal to a value in the set."""
            self.tree_set_P.add_all([self.person_test, self.person_test2])
            self.assertEqual(self.tree_set_P.lower(self.person_test), None)

        def test_lower_greater_than_max_Person(self):
            """Test lower method when the value is greater than the maximum value in the set."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.assertEqual(self.tree_set_P.lower(self.person_test3), self.person_test2)

        def test_lower_between_values_Person(self):
            """Test lower method when the value is between two values in the set."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.tree_set_P.add(self.person_test4)
            self.assertEqual(self.tree_set_P.lower(self.person_test3), self.person_test2)

        def test_higher_greater_than_max_Person(self):
            """Test higher method when the value is greater than the maximum value in the set."""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3])
            self.assertIsNone(self.tree_set_P.higher(self.person_test4))

        def test_higher_elements_greater_than_value_Person(self):
            """Test higher method when set contains elements greater than the given value."""
            self.tree_set_P.add_all([self.person_test, self.person_test3, self.person_test4])
            self.assertEqual(self.tree_set_P.higher(self.person_test2), self.person_test3)

        def test_higher_elements_only_smaller_Person(self):
            """Test higher method when set contains only elements smaller than the given value."""
            self.tree_set_P.add_all([self.person_test, self.person_test3, self.person_test4])
            self.assertEqual(self.tree_set_P.higher(self.person_test5), None)
        
        def test_first_element_black_Person(self):
            """Test first node in the tree black."""
            self.tree_set_P.add(self.person_test)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(self.person_test), TreeNode.Color.BLACK)

        def test_right_child_red_Person(self):
            """Test right child of root in the tree red."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(self.person_test2), TreeNode.Color.RED)

        def test_left_child_red_Person(self):
            """Test left child of root in the tree red."""
            self.tree_set_P.add(self.person_test2)
            self.tree_set_P.add(self.person_test)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(self.person_test), TreeNode.Color.RED)

        def test_root_recolor_Person(self):
            """Test recolor of the root when in is changed."""
            self.tree_set_P.add(self.person_test)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(self.person_test), TreeNode.Color.BLACK)
            self.tree_set_P.add(self.person_test2)
            self.tree_set_P.add(self.person_test3)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(self.person_test), TreeNode.Color.RED)

        '''def test_remove_node_with_single_child_Person_NoComparable(self):
            """Tests removing a node with a single child."""
            self.tree_set_P2.add(self.person_test_NC)
            self.tree_set_P2.add(self.person_test2_NC)
            self.tree_set_P2.add(self.person_test3_NC)
            self.assertTrue(self.tree_set_P2.remove(self.person_test_NC))
            self.assertEqual(self.tree_set_P2.size(), 2)

        def test_remove_node_with_two_children_Person_NoComparable(self):
            """Tests removing a node with two children (replaces with successor)."""
            self.tree_set_P2.add(self.person_test_NC)
            self.tree_set_P2.add(self.person_test2_NC)
            self.tree_set_P2.add(self.person_test3_NC)
            self.assertTrue(self.tree_set_P2.remove(self.person_test2_NC))
            self.assertEqual(self.tree_set_P2.size(), 2)

        def test_remove_root_node_Person_NoComparable(self):
            """Tests removing the root node ."""
            self.tree_set_P2.add(self.person_test_NC)
            self.tree_set_P2.add(self.person_test2_NC)
            self.tree_set_P2.add(self.person_test3_NC)
            self.assertTrue(self.tree_set_P2.remove(self.person_test_NC))
            self.assertEqual(self.tree_set_P2.size(), 2)

        def test_clear_Person_NoComparable(self):
            """Tests clearing the TreeSet from all its inserted elements."""
            values = TreeSet(Person_NoComparable, [self.person_test_NC, self.person_test2_NC, self.person_test3_NC])
            self.assertEqual(len(values), 3)
            values.clear()
            self.assertNotEqual(values.size(), 3)
            self.assertEqual(values.size(), 0)'''

        
if __name__ == '__main__':
    unittest.main()
