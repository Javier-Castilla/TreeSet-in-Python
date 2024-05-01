
import unittest

from TreeSet import *


class TestInt(unittest.TestCase):
        def setUp(self):
            self.tree_set = TreeSet(int)


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

        def test_remove_node_with_single_child(self):
            """Tests removing a node with a single child."""
            self.tree_set.add(10)
            self.tree_set.add(20)
            self.tree_set.add(5)

            self.assertTrue(self.tree_set.remove(10))
            self.assertEqual(self.tree_set.size(), 2)
            self.assertFalse(10 in self.tree_set)
            self.assertTrue(5 in self.tree_set)
            self.assertTrue(20 in self.tree_set)

        def test_remove_node_with_two_children(self):
            """Tests removing a node with two children (replaces with successor)."""
            self.tree_set.add(10)
            self.tree_set.add(5)
            self.tree_set.add(15)
            self.tree_set.add(12)

            self.assertTrue(self.tree_set.remove(10))
            self.assertEqual(self.tree_set.size(), 3)
            self.assertFalse(10 in self.tree_set)
            self.assertTrue(5 in self.tree_set)
            self.assertTrue(12 in self.tree_set)
            self.assertTrue(15 in self.tree_set)

        def test_remove_root_node(self):
            """Tests removing the root node ."""
            self.tree_set.add(10)
            self.tree_set.add(5)
            self.tree_set.add(15)

            self.assertTrue(self.tree_set.remove(10))
            self.assertEqual(self.tree_set.size(), 2)
            self.assertFalse(10 in self.tree_set)
            self.assertTrue(5 in self.tree_set)
            self.assertTrue(15 in self.tree_set)
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

        def test_clear(self):
            """Tests clearing the TreeSet from all its inserted elements."""
            values = TreeSet(int, [1, 2, 3, 4, 5])
            self.assertEqual(len(values), 5)

            self.assertNotEqual(values.clear(), 5)
            self.assertEqual(values.clear(), None)

        def test_clone_multiple_elements(self):
            """Tests cloning  multiples elements TreeSet."""
            self.tree_set.add_all([10, 20, 30])
            cloned_tree_set = self.tree_set.clone()
            self.assertEqual(self.tree_set.size(), cloned_tree_set.size())
            for value in self.tree_set:
                self.assertTrue(cloned_tree_set.contains(value))
        def test_clone_one_element(self):
            """Tests cloning  one element TreeSet."""
            self.tree_set.add(10)
            cloned_tree_set = self.tree_set.clone()
            self.assertEqual(self.tree_set.size(), cloned_tree_set.size())
            for value in self.tree_set:
                self.assertTrue(cloned_tree_set.contains(value))

        def test_is_empty(self):
            """Test the is_empty method for different scenarios"""
            self.assertTrue(self.tree_set.is_empty())
            self.tree_set.add_all([12, 13, 14])
            self.assertFalse(self.tree_set.is_empty())
            self.tree_set.remove(12)
            self.assertFalse(self.tree_set.is_empty())


        def test_contains_empty_set(self):
            """Tests contains method on an empty TreeSet."""
            self.assertFalse(self.tree_set.contains(10))


        def test_contains_single_element(self):
            """Tests contains method on a TreeSet with a single element."""
            self.tree_set.add(10)
            self.assertTrue(self.tree_set.contains(10))
            self.assertFalse(self.tree_set.contains(20))


        def test_contains_multiple_elements(self):
            """Tests contains method on a TreeSet with multiple elements."""
            self.tree_set.add_all([10, 20, 30, 40, 50])
            self.assertTrue(self.tree_set.contains(10))
            self.assertTrue(self.tree_set.contains(30))
            self.assertFalse(self.tree_set.contains(15))

        def test_ceiling_empty_set(self):
            """Test ceiling method on an empty set."""
            self.assertIsNone(self.tree_set.ceiling(10))

        def test_ceiling_elements_greater_equal(self):
            """Test ceiling method when set contains elements greater than or equal to the given value."""
            self.tree_set.add_all([2, 5, 10, 15])
            self.assertEqual(self.tree_set.ceiling(10), 10)
            self.assertEqual(self.tree_set.ceiling(12), 15)

        def test_ceiling_elements_only_greater(self):
            """Test ceiling method when set contains only elements greater than the given value."""
            self.tree_set.add_all([15, 20, 25])
            self.assertEqual(self.tree_set.ceiling(10), 15)

        def test_ceiling_elements_only_smaller(self):
            """Test ceiling method when set contains only elements smaller than the given value."""
            self.tree_set.add_all([2, 5, 7])
            self.assertEqual(self.tree_set.ceiling(10), None)

        def test_floor_empty_set(self):
            """Test floor method on an empty set."""
            self.assertIsNone(self.tree_set.floor(10))

        def test_floor_smaller_than_min(self):
            """Test floor method when the value is smaller than the minimum value in the set."""
            self.tree_set.add(5)
            self.assertEqual(self.tree_set.floor(3), None)

        def test_floor_equal_to_value_in_set(self):
            """Test floor method when the value is equal to a value in the set."""
            self.tree_set.add(5)
            self.tree_set.add(10)
            self.assertEqual(self.tree_set.floor(5), 5)

        def test_floor_greater_than_max(self):
            """Test floor method when the value is greater than the maximum value in the set."""
            self.tree_set.add(5)
            self.tree_set.add(10)
            self.assertEqual(self.tree_set.floor(15), 10)

        def test_floor_between_values(self):
            """Test floor method when the value is between two values in the set."""
            self.tree_set.add(5)
            self.tree_set.add(10)
            self.tree_set.add(15)
            self.assertEqual(self.tree_set.floor(12), 10)

        def test_poll_first_empty_set(self):
            """Test pollFirst method on an empty set."""
            self.assertIsNone(self.tree_set.pollFirst())

        def test_poll_first_non_empty_set(self):
            """Test pollFirst method on a non-empty set."""
            self.tree_set.add_all([5, 10, 15])
            self.assertEqual(self.tree_set.pollFirst(), 5)
            self.assertEqual(self.tree_set.size(), 2)
            self.assertEqual(list(self.tree_set), [10, 15])

        def test_poll_first_single_element_set(self):
            """Test pollFirst method on a set with a single element."""
            self.tree_set.add(5)
            self.assertEqual(self.tree_set.pollFirst(), 5)
            self.assertEqual(self.tree_set.size(), 0)
            self.assertEqual(list(self.tree_set), [])

        def test_poll_last_empty_set(self):
            """Test pollLast method on an empty set."""
            self.assertIsNone(self.tree_set.pollLast())

        def test_poll_last_non_empty_set(self):
            """Test pollLast method on a non-empty set."""
            self.tree_set.add_all([5, 10, 15])
            self.assertEqual(self.tree_set.pollLast(), 15)
            self.assertEqual(self.tree_set.size(), 2)
            self.assertEqual(list(self.tree_set), [5, 10])

        def test_poll_last_single_element_set(self):
            """Test pollLast method on a set with a single element."""
            self.tree_set.add(5)
            self.assertEqual(self.tree_set.pollLast(), 5)
            self.assertEqual(self.tree_set.size(), 0)
            self.assertEqual(list(self.tree_set), [])

        def test_iterator_multiple_elements(self):
            """Test iterator  method for multiple elements."""
            self.tree_set.add_all([15, 20, 25])
            elements = [elem for elem in self.tree_set.iterator()]
            self.assertListEqual(elements, [15, 20, 25])

        def test_iterator_empty_set(self):
            """Test iterator method on an empty set."""
            elements = [elem for elem in self.tree_set.iterator()]
            self.assertListEqual(elements, [])

        def test_iterator_single_element(self):
            """Test iterator method with a single element."""
            self.tree_set.add(10)
            elements = [elem for elem in self.tree_set.iterator()]
            self.assertListEqual(elements, [10])

        def test_descending_iterator_empty_set(self):
            """Test descending_iterator method on an empty set."""
            elements = [elem for elem in self.tree_set.descending_iterator()]
            self.assertListEqual(elements, [])

        def test_descending_iterator_single_element(self):
            """Test descending_iterator method with a single element."""
            self.tree_set.add(10)
            elements = [elem for elem in self.tree_set.descending_iterator()]
            self.assertListEqual(elements, [10])


        def test_descending_iterator_multiples_elements(self):
            """Test descending_iterator method with multiple elements."""
            self.tree_set.add_all([12, 13, 30])
            elements = [elem for elem in self.tree_set.descending_iterator()]
            self.assertListEqual(elements, [30, 13, 12])

        def test_lower_empty(self):
            """Test lower that an empty set"""
            self.assertIsNone(self.tree_set.lower(10))

        def test_lower_smaller_than_min(self):
            """Test lower method when the value is smaller than the minimum value in the set."""
            self.tree_set.add(5)
            self.assertIsNone(self.tree_set.lower(3))

        def test_lower_equal_to_value_in_set(self):
            """Test lower method when the value is equal to a value in the set."""
            self.tree_set.add_all([5, 10])
            self.assertEqual(self.tree_set.lower(5), None)

        def test_lower_greater_than_max(self):
            """Test lower method when the value is greater than the maximum value in the set."""
            self.tree_set.add(5)
            self.tree_set.add(10)
            self.assertEqual(self.tree_set.lower(15), 10)

        def test_lower_between_values(self):
            """Test lower method when the value is between two values in the set."""
            self.tree_set.add(5)
            self.tree_set.add(10)
            self.tree_set.add(15)
            self.assertEqual(self.tree_set.lower(12), 10)

        def test_higher_empty_set(self):
            """Test higher method on an empty set."""
            self.assertIsNone(self.tree_set.higher(10))

        def test_higher_greater_than_max(self):
            """Test higher method when the value is greater than the maximum value in the set."""
            self.tree_set.add_all([5, 10, 15])
            self.assertIsNone(self.tree_set.higher(20))

        def test_higher_elements_greater_than_value(self):
            """Test higher method when set contains elements greater than the given value."""
            self.tree_set.add_all([5, 10, 15])
            self.assertEqual(self.tree_set.higher(8), 10)

        def test_higher_elements_only_smaller(self):
            """Test higher method when set contains only elements smaller than the given value."""
            self.tree_set.add_all([2, 5, 7])
            self.assertEqual(self.tree_set.higher(10), None)
        
        def test_first_element_black(self):
            """Test first node in the tree black."""
            self.tree_set.add(1)
            self.assertEqual(self.tree_set.__get_color__(1), TreeNode.Color.BLACK)

        def test_right_child_red(self):
            """Test right child of root in the tree red."""
            self.tree_set.add(2)
            self.tree_set.add(3)
            self.assertEqual(self.tree_set.__get_color__(3), TreeNode.Color.RED)

        def test_left_child_red(self):
            """Test left child of root in the tree red."""
            self.tree_set.add(2)
            self.tree_set.add(1)
            self.assertEqual(self.tree_set.__get_color__(1), TreeNode.Color.RED)

        def test_root_recolor(self):
            """Test recolor of the root when in is changed."""
            self.tree_set.add(1)
            self.assertEqual(self.tree_set.__get_color__(1), TreeNode.Color.BLACK)
            self.tree_set.add(2)
            self.tree_set.add(3)
            self.assertEqual(self.tree_set.__get_color__(1), TreeNode.Color.RED)

        def test_left_rotation_recolor(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set.add_all([1,2,3,4,5,6,7])
            self.assertEqual(self.tree_set.__get_color__(1), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(2), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(3), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(4), TreeNode.Color.RED)
            self.assertEqual(self.tree_set.__get_color__(5), TreeNode.Color.RED)
            self.assertEqual(self.tree_set.__get_color__(6), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(7), TreeNode.Color.RED)
            self.tree_set.add(8)
            self.assertEqual(self.tree_set.__get_color__(1), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(2), TreeNode.Color.RED)
            self.assertEqual(self.tree_set.__get_color__(3), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(4), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(5), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(6), TreeNode.Color.RED)
            self.assertEqual(self.tree_set.__get_color__(7), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(8), TreeNode.Color.RED)

        def test_right_rotation_recolor(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set.add_all([8,7,6,5,4,3,2])
            self.assertEqual(self.tree_set.__get_color__(2), TreeNode.Color.RED)
            self.assertEqual(self.tree_set.__get_color__(3), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(4), TreeNode.Color.RED)
            self.assertEqual(self.tree_set.__get_color__(5), TreeNode.Color.RED)
            self.assertEqual(self.tree_set.__get_color__(6), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(7), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(8), TreeNode.Color.BLACK)
            self.tree_set.add(1)
            self.assertEqual(self.tree_set.__get_color__(1), TreeNode.Color.RED)
            self.assertEqual(self.tree_set.__get_color__(2), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(3), TreeNode.Color.RED)
            self.assertEqual(self.tree_set.__get_color__(4), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(5), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(6), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set.__get_color__(7), TreeNode.Color.RED)
            self.assertEqual(self.tree_set.__get_color__(8), TreeNode.Color.BLACK)

if __name__ == '__main__':
    unittest.main()
