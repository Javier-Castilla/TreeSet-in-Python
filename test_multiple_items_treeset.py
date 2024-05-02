
import unittest

from TreeSet import *

class TestInt(unittest.TestCase):
        def setUp(self):
            self.tree_set_int = TreeSet(int)
            self.tree_set_str = TreeSet(str)
            

        def test_remove_node_with_single_child(self):
            """Tests removing a node with a single child."""
            self.tree_set_int.add(10)
            self.tree_set_int.add(20)
            self.tree_set_int.add(5)

            self.assertTrue(self.tree_set_int.remove(10))
            self.assertEqual(self.tree_set_int.size(), 2)
            self.assertFalse(10 in self.tree_set_int)
            self.assertTrue(5 in self.tree_set_int)
            self.assertTrue(20 in self.tree_set_int)

        def test_remove_node_with_two_children(self):
            """Tests removing a node with two children (replaces with successor)."""
            self.tree_set_int.add(10)
            self.tree_set_int.add(5)
            self.tree_set_int.add(15)
            self.tree_set_int.add(12)

            self.assertTrue(self.tree_set_int.remove(10))
            self.assertEqual(self.tree_set_int.size(), 3)
            self.assertFalse(10 in self.tree_set_int)
            self.assertTrue(5 in self.tree_set_int)
            self.assertTrue(12 in self.tree_set_int)
            self.assertTrue(15 in self.tree_set_int)

        def test_remove_root_node(self):
            """Tests removing the root node ."""
            self.tree_set_int.add(10)
            self.tree_set_int.add(5)
            self.tree_set_int.add(15)

            self.assertTrue(self.tree_set_int.remove(10))
            self.assertEqual(self.tree_set_int.size(), 2)
            self.assertFalse(10 in self.tree_set_int)
            self.assertTrue(5 in self.tree_set_int)
            self.assertTrue(15 in self.tree_set_int)

        def test_clear(self):
            """Tests clearing the TreeSet from all its inserted elements."""
            values = TreeSet(int, [1, 2, 3, 4, 5])
            self.assertEqual(len(values), 5)
            values.clear()
            self.assertNotEqual(values.size(), 5)
            self.assertEqual(values.size(), 0)

        def test_clone_multiple_elements(self):
            """Tests cloning  multiples elements TreeSet."""
            self.tree_set_int.add_all([10, 20, 30])
            cloned_tree_set_int = self.tree_set_int.clone()
            self.assertEqual(self.tree_set_int.size(), cloned_tree_set_int.size())
            for value in self.tree_set_int:
                self.assertTrue(cloned_tree_set_int.contains(value))
        def test_clone_one_element(self):
            """Tests cloning  one element TreeSet."""
            self.tree_set_int.add(10)
            cloned_tree_set_int = self.tree_set_int.clone()
            self.assertEqual(self.tree_set_int.size(), cloned_tree_set_int.size())
            for value in self.tree_set_int:
                self.assertTrue(cloned_tree_set_int.contains(value))

        def test_is_empty(self):
            """Test the is_empty method for different scenarios"""
            self.tree_set_int.add_all([12, 13, 14])
            self.assertFalse(self.tree_set_int.is_empty())
            self.tree_set_int.remove(12)
            self.assertFalse(self.tree_set_int.is_empty())

        def test_contains_single_element(self):
            """Tests contains method on a TreeSet with a single element."""
            self.tree_set_int.add(10)
            self.assertTrue(self.tree_set_int.contains(10))
            self.assertFalse(self.tree_set_int.contains(20))

        def test_contains_multiple_elements(self):
            """Tests contains method on a TreeSet with multiple elements."""
            self.tree_set_int.add_all([10, 20, 30, 40, 50])
            self.assertTrue(self.tree_set_int.contains(10))
            self.assertTrue(self.tree_set_int.contains(30))
            self.assertFalse(self.tree_set_int.contains(15))

        

        def test_ceiling_elements_greater_equal(self):
            """Test ceiling method when set contains elements greater than or equal to the given value."""
            self.tree_set_int.add_all([2, 5, 10, 15])
            self.assertEqual(self.tree_set_int.ceiling(10), 10)
            self.assertEqual(self.tree_set_int.ceiling(12), 15)

        def test_ceiling_elements_only_greater(self):
            """Test ceiling method when set contains only elements greater than the given value."""
            self.tree_set_int.add_all([15, 20, 25])
            self.assertEqual(self.tree_set_int.ceiling(10), 15)

        def test_ceiling_elements_only_smaller(self):
            """Test ceiling method when set contains only elements smaller than the given value."""
            self.tree_set_int.add_all([2, 5, 7])
            self.assertEqual(self.tree_set_int.ceiling(10), None)

        def test_ceiling_between_values(self):
            """Test ceiling method when the value is between two values in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.tree_set_int.add(15)
            self.assertEqual(self.tree_set_int.ceiling(8), 10)

        def test_floor_smaller_than_min(self):
            """Test floor method when the value is smaller than the minimum value in the set."""
            self.tree_set_int.add(5)
            self.assertEqual(self.tree_set_int.floor(3), None)

        def test_floor_equal_to_value_in_set(self):
            """Test floor method when the value is equal to a value in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.assertEqual(self.tree_set_int.floor(5), 5)

        def test_floor_greater_than_max(self):
            """Test floor method when the value is greater than the maximum value in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.assertEqual(self.tree_set_int.floor(15), 10)

        def test_floor_between_values(self):
            """Test floor method when the value is between two values in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.tree_set_int.add(15)
            self.assertEqual(self.tree_set_int.floor(12), 10)

        

        def test_poll_first_non_empty_set(self):
            """Test pollFirst method on a non-empty set."""
            self.tree_set_int.add_all([5, 10, 15])
            self.assertEqual(self.tree_set_int.pollFirst(), 5)
            self.assertEqual(self.tree_set_int.size(), 2)
            self.assertEqual(list(self.tree_set_int), [10, 15])

        def test_poll_first_single_element_set(self):
            """Test pollFirst method on a set with a single element."""
            self.tree_set_int.add(5)
            self.assertEqual(self.tree_set_int.pollFirst(), 5)
            self.assertEqual(self.tree_set_int.size(), 0)
            self.assertEqual(list(self.tree_set_int), [])

        

        def test_poll_last_non_empty_set(self):
            """Test pollLast method on a non-empty set."""
            self.tree_set_int.add_all([5, 10, 15])
            self.assertEqual(self.tree_set_int.pollLast(), 15)
            self.assertEqual(self.tree_set_int.size(), 2)
            self.assertEqual(list(self.tree_set_int), [5, 10])

        def test_poll_last_single_element_set(self):
            """Test pollLast method on a set with a single element."""
            self.tree_set_int.add(5)
            self.assertEqual(self.tree_set_int.pollLast(), 5)
            self.assertEqual(self.tree_set_int.size(), 0)
            self.assertEqual(list(self.tree_set_int), [])

        def test_iterator_multiple_elements(self):
            """Test iterator  method for multiple elements."""
            self.tree_set_int.add_all([15, 20, 25])
            elements = [elem for elem in self.tree_set_int.iterator()]
            self.assertListEqual(elements, [15, 20, 25])


        def test_iterator_single_element(self):
            """Test iterator method with a single element."""
            self.tree_set_int.add(10)
            elements = [elem for elem in self.tree_set_int.iterator()]
            self.assertListEqual(elements, [10])

        

        def test_descending_iterator_single_element(self):
            """Test descending_iterator method with a single element."""
            self.tree_set_int.add(10)
            elements = [elem for elem in self.tree_set_int.descending_iterator()]
            self.assertListEqual(elements, [10])


        def test_descending_iterator_multiples_elements(self):
            """Test descending_iterator method with multiple elements."""
            self.tree_set_int.add_all([12, 13, 30])
            elements = [elem for elem in self.tree_set_int.descending_iterator()]
            self.assertListEqual(elements, [30, 13, 12])

        def test_lower_smaller_than_min(self):
            """Test lower method when the value is smaller than the minimum value in the set."""
            self.tree_set_int.add(5)
            self.assertIsNone(self.tree_set_int.lower(3))

        def test_lower_equal_to_value_in_set(self):
            """Test lower method when the value is equal to a value in the set."""
            self.tree_set_int.add_all([5, 10])
            self.assertEqual(self.tree_set_int.lower(5), None)

        def test_lower_greater_than_max(self):
            """Test lower method when the value is greater than the maximum value in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.assertEqual(self.tree_set_int.lower(15), 10)

        def test_lower_between_values(self):
            """Test lower method when the value is between two values in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.tree_set_int.add(15)
            self.assertEqual(self.tree_set_int.lower(12), 10)

        def test_higher_greater_than_max(self):
            """Test higher method when the value is greater than the maximum value in the set."""
            self.tree_set_int.add_all([5, 10, 15])
            self.assertIsNone(self.tree_set_int.higher(20))

        def test_higher_elements_greater_than_value(self):
            """Test higher method when set contains elements greater than the given value."""
            self.tree_set_int.add_all([5, 10, 15])
            self.assertEqual(self.tree_set_int.higher(8), 10)

        def test_higher_elements_only_smaller(self):
            """Test higher method when set contains only elements smaller than the given value."""
            self.tree_set_int.add_all([2, 5, 7])
            self.assertEqual(self.tree_set_int.higher(10), None)
        
        def test_first_element_black(self):
            """Test first node in the tree black."""
            self.tree_set_int.add(1)
            self.assertEqual(self.tree_set_int._TreeSet__get_color(1), TreeNode.Color.BLACK)

        def test_right_child_red(self):
            """Test right child of root in the tree red."""
            self.tree_set_int.add(2)
            self.tree_set_int.add(3)
            self.assertEqual(self.tree_set_int._TreeSet__get_color(3), TreeNode.Color.RED)

        def test_left_child_red(self):
            """Test left child of root in the tree red."""
            self.tree_set_int.add(2)
            self.tree_set_int.add(1)
            self.assertEqual(self.tree_set_int._TreeSet__get_color(1), TreeNode.Color.RED)

        def test_root_recolor(self):
            """Test recolor of the root when in is changed."""
            self.tree_set_int.add(1)
            self.assertEqual(self.tree_set_int._TreeSet__get_color(1), TreeNode.Color.BLACK)
            self.tree_set_int.add(2)
            self.tree_set_int.add(3)
            self.assertEqual(self.tree_set_int._TreeSet__get_color(1), TreeNode.Color.RED)

        def test_left_rotation_recolor(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set_int.add_all([1,2,3,4,5,6,7])
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.RED]
            self.tree_set_int.add(8)
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.RED]
            self.assertEqual(tree_colors, real_colors)

        def test_right_rotation_recolor(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set_int.add_all([8,7,6,5,4,3,2])
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.BLACK]
            self.assertEqual(tree_colors, real_colors)
            self.tree_set_int.add(1)
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.BLACK]
            self.assertEqual(tree_colors, real_colors)

if __name__ == '__main__':
    unittest.main()
