
import unittest

from Person import Person
from TreeSet import *


class TestPerson(unittest.TestCase):
        def setUp(self):
                self.tree_set_P = TreeSet(Person)
                self.person_test = Person("Name", "Surname", 20, "12345678A")
                self.person_test2 = Person("Name2", "Surname2", 10, "12345678X")
                self.person_test3 = Person("Name2", "Surname2", 30, "12345678B")
                self.person_test4 = Person("Name2", "Surname2", 30, "12345678Z")
                self.person_test5 = Person("Name2", "Surname2", 30, "12345678F")
                self.person_test6 = Person("Name2", "Surname2", 30, "12345678W")
            
        def test_remove_node_with_single_child_Person(self):
            """Tests removing a node with a single child."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.tree_set_P.add(self.person_test3)

            self.assertTrue(self.tree_set_P.remove(self.person_test))
            self.assertEqual(self.tree_set_P.size(), 2)
            self.assertFalse(10 in self.tree_set_P)
            self.assertTrue(5 in self.tree_set_P)
            self.assertTrue(20 in self.tree_set_P)

        def test_remove_node_with_two_children_Person(self):
            """Tests removing a node with two children (replaces with successor)."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.tree_set_P.add(self.person_test3)
            self.tree_set_P.add(self.person_test4)

            self.assertTrue(self.tree_set_P.remove(self.person_test))
            self.assertEqual(self.tree_set_P.size(), 3)
            self.assertFalse(10 in self.tree_set_P)
            self.assertTrue(5 in self.tree_set_P)
            self.assertTrue(12 in self.tree_set_P)
            self.assertTrue(15 in self.tree_set_P)

        def test_remove_root_node_Person(self):
            """Tests removing the root node ."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.tree_set_P.add(self.person_test3)

            self.assertTrue(self.tree_set_P.remove(self.person_test))
            self.assertEqual(self.tree_set_P.size(), 2)
            self.assertFalse(10 in self.tree_set_P)
            self.assertTrue(5 in self.tree_set_P)
            self.assertTrue(15 in self.tree_set_P)

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

        

        '''def test_ceiling_elements_greater_equal_Person(self):
            """Test ceiling method when set contains elements greater than or equal to the given value."""
            self.tree_set_P.add_all([2, 5, 10, 15])
            self.assertEqual(self.tree_set_P.ceiling(10), 10)
            self.assertEqual(self.tree_set_P.ceiling(12), 15)

        def test_ceiling_elements_only_greater_Person(self):
            """Test ceiling method when set contains only elements greater than the given value."""
            self.tree_set_P.add_all([15, 20, 25])
            self.assertEqual(self.tree_set_P.ceiling(10), 15)

        def test_ceiling_elements_only_smaller_Person(self):
            """Test ceiling method when set contains only elements smaller than the given value."""
            self.tree_set_P.add_all([2, 5, 7])
            self.assertEqual(self.tree_set_P.ceiling(10), None)

        def test_ceiling_between_values_Person(self):
            """Test ceiling method when the value is between two values in the set."""
            self.tree_set_P.add(5)
            self.tree_set_P.add(10)
            self.tree_set_P.add(15)
            self.assertEqual(self.tree_set_P.ceiling(8), 10)

        def test_floor_smaller_than_min_Person(self):
            """Test floor method when the value is smaller than the minimum value in the set."""
            self.tree_set_P.add(5)
            self.assertEqual(self.tree_set_P.floor(3), None)

        def test_floor_equal_to_value_in_set_Person(self):
            """Test floor method when the value is equal to a value in the set."""
            self.tree_set_P.add(5)
            self.tree_set_P.add(10)
            self.assertEqual(self.tree_set_P.floor(5), 5)

        def test_floor_greater_than_max_Person(self):
            """Test floor method when the value is greater than the maximum value in the set."""
            self.tree_set_P.add(5)
            self.tree_set_P.add(10)
            self.assertEqual(self.tree_set_P.floor(15), 10)

        def test_floor_between_values_Person(self):
            """Test floor method when the value is between two values in the set."""
            self.tree_set_P.add(5)
            self.tree_set_P.add(10)
            self.tree_set_P.add(15)
            self.assertEqual(self.tree_set_P.floor(12), 10)

        

        def test_poll_first_non_empty_set_Person(self):
            """Test pollFirst method on a non-empty set."""
            self.tree_set_P.add_all([5, 10, 15])
            self.assertEqual(self.tree_set_P.pollFirst(), 5)
            self.assertEqual(self.tree_set_P.size(), 2)
            self.assertEqual(list(self.tree_set_P), [10, 15])

        def test_poll_first_single_element_set_Person(self):
            """Test pollFirst method on a set with a single element."""
            self.tree_set_P.add(5)
            self.assertEqual(self.tree_set_P.pollFirst(), 5)
            self.assertEqual(self.tree_set_P.size(), 0)
            self.assertEqual(list(self.tree_set_P), [])

        

        def test_poll_last_non_empty_set_Person(self):
            """Test pollLast method on a non-empty set."""
            self.tree_set_P.add_all([5, 10, 15])
            self.assertEqual(self.tree_set_P.pollLast(), 15)
            self.assertEqual(self.tree_set_P.size(), 2)
            self.assertEqual(list(self.tree_set_P), [5, 10])

        def test_poll_last_single_element_set_Person(self):
            """Test pollLast method on a set with a single element."""
            self.tree_set_P.add(5)
            self.assertEqual(self.tree_set_P.pollLast(), 5)
            self.assertEqual(self.tree_set_P.size(), 0)
            self.assertEqual(list(self.tree_set_P), [])

        def test_iterator_multiple_elements_Person(self):
            """Test iterator  method for multiple elements."""
            self.tree_set_P.add_all([15, 20, 25])
            elements = [elem for elem in self.tree_set_P.iterator()]
            self.assertListEqual(elements, [15, 20, 25])


        def test_iterator_single_element_Person(self):
            """Test iterator method with a single element."""
            self.tree_set_P.add(10)
            elements = [elem for elem in self.tree_set_P.iterator()]
            self.assertListEqual(elements, [10])

        

        def test_descending_iterator_single_element_Person(self):
            """Test descending_iterator method with a single element."""
            self.tree_set_P.add(10)
            elements = [elem for elem in self.tree_set_P.descending_iterator()]
            self.assertListEqual(elements, [10])


        def test_descending_iterator_multiples_elements_Person(self):
            """Test descending_iterator method with multiple elements."""
            self.tree_set_P.add_all([12, 13, 30])
            elements = [elem for elem in self.tree_set_P.descending_iterator()]
            self.assertListEqual(elements, [30, 13, 12])

        def test_lower_smaller_than_min_Person(self):
            """Test lower method when the value is smaller than the minimum value in the set."""
            self.tree_set_P.add(5)
            self.assertIsNone(self.tree_set_P.lower(3))

        def test_lower_equal_to_value_in_set_Person(self):
            """Test lower method when the value is equal to a value in the set."""
            self.tree_set_P.add_all([5, 10])
            self.assertEqual(self.tree_set_P.lower(5), None)

        def test_lower_greater_than_max_Person(self):
            """Test lower method when the value is greater than the maximum value in the set."""
            self.tree_set_P.add(5)
            self.tree_set_P.add(10)
            self.assertEqual(self.tree_set_P.lower(15), 10)

        def test_lower_between_values_Person(self):
            """Test lower method when the value is between two values in the set."""
            self.tree_set_P.add(5)
            self.tree_set_P.add(10)
            self.tree_set_P.add(15)
            self.assertEqual(self.tree_set_P.lower(12), 10)

        def test_higher_greater_than_max_Person(self):
            """Test higher method when the value is greater than the maximum value in the set."""
            self.tree_set_P.add_all([5, 10, 15])
            self.assertIsNone(self.tree_set_P.higher(20))

        def test_higher_elements_greater_than_value_Person(self):
            """Test higher method when set contains elements greater than the given value."""
            self.tree_set_P.add_all([5, 10, 15])
            self.assertEqual(self.tree_set_P.higher(8), 10)

        def test_higher_elements_only_smaller_Person(self):
            """Test higher method when set contains only elements smaller than the given value."""
            self.tree_set_P.add_all([2, 5, 7])
            self.assertEqual(self.tree_set_P.higher(10), None)
        
        def test_first_element_black_Person(self):
            """Test first node in the tree black."""
            self.tree_set_P.add(1)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(1), TreeNode.Color.BLACK)

        def test_right_child_red_Person(self):
            """Test right child of root in the tree red."""
            self.tree_set_P.add(2)
            self.tree_set_P.add(3)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(3), TreeNode.Color.RED)

        def test_left_child_red_Person(self):
            """Test left child of root in the tree red."""
            self.tree_set_P.add(2)
            self.tree_set_P.add(1)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(1), TreeNode.Color.RED)

        def test_root_recolor_Person(self):
            """Test recolor of the root when in is changed."""
            self.tree_set_P.add(1)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(1), TreeNode.Color.BLACK)
            self.tree_set_P.add(2)
            self.tree_set_P.add(3)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(1), TreeNode.Color.RED)

        def test_left_rotation_recolor_Person(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set_P.add_all([1,2,3,4,5,6,7])
            tree_colors = self.tree_set_P._TreeSet__array_color()
            real_colors = [TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.RED]
            self.tree_set_P.add(8)
            tree_colors = self.tree_set_P._TreeSet__array_color()
            real_colors = [TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.RED]
            self.assertEqual(tree_colors, real_colors)

        def test_right_rotation_recolor_Person(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set_P.add_all([8,7,6,5,4,3,2])
            tree_colors = self.tree_set_P._TreeSet__array_color()
            real_colors = [TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.BLACK]
            self.assertEqual(tree_colors, real_colors)
            self.tree_set_P.add(1)
            tree_colors = self.tree_set_P._TreeSet__array_color()
            real_colors = [TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_case_4_1_Person(self):
            """Test Case 4: Uncle is red and the violator node is in external position."""

            self.tree_set_P.add_all([10, 5, 15, 3, 7])
            self.tree_set_P.add(2)
            tree_colors = self.tree_set_P._TreeSet__array_color()
            real_colors = [TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.BLACK,
                        TreeNode.Color.BLACK, TreeNode.Color.BLACK]
            self.assertEqual_Person(tree_colors, real_colors)
        def test_case_4_2(self):
            """Test Case 4: Uncle is red and the violator node is in Personernal position."""

            self.tree_set_P.add_all([10, 5, 15, 3, 7])
            self.tree_set_P.add(4)
            tree_colors = self.tree_set_P._TreeSet__array_color()
            real_colors = [TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.RED, TreeNode.Color.BLACK,
                        TreeNode.Color.BLACK, TreeNode.Color.BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_Case_5_Person(self):
            """Test Case 5: Uncle is black and the violator node is in external position."""
            self.tree_set_P.add_all([10, 5, 15, 3])
            self.tree_set_P.add(2)
            tree_colors = self.tree_set_P._TreeSet__array_color()
            real_colors = [TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.RED, TreeNode.Color.BLACK,
                        TreeNode.Color.BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_case_6_Person(self):
            """Test Case 6: Uncle is black and the violator node is in Personernal position."""
            self.tree_set_P.add_all([10, 5, 15, 6])
            self.tree_set_P.add(7)
            tree_colors = self.tree_set_P._TreeSet__array_color()
            real_colors = [TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.RED,
                        TreeNode.Color.BLACK, TreeNode.Color.BLACK]
            self.assertEqual(tree_colors, real_colors)

        
        def test_case_1_b_remove_Person(self):
            "Test Case 1b: Node to be removed is the root and have a red son"
            self.tree_set_P.add_all([10, 12])
            self.tree_set_P.remove(10)
            tree_colors = self.tree_set_P._TreeSet__array_color()
            real_colors = [TreeNode.Color.BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_Case_2_b_Person(self):
            """Test Case 2: Node to be removed is red"""
            self.tree_set_P.add_all([10, 5])
            self.tree_set_P.remove(5)
            tree_color = self.tree_set_P._TreeSet__array_color()
            real_colors = [TreeNode.Color.BLACK]
            self.assertEqual(tree_color, real_colors)

        def test_case_5_remove_Person(self):
            """Test Case 5: The sibling is red, and both the parent and the sibling's children are black."""
            self.tree_set_P.add_all([10, 3, 13, 16, 20, 12, 2, 5])
            self.tree_set_P.remove(3)

            tree_colors = self.tree_set_P._TreeSet__array_color()
            real_colors = [TreeNode.Color.RED, TreeNode.Color.BLACK, TreeNode.Color.BLACK, TreeNode.Color.RED,
                        TreeNode.Color.BLACK,TreeNode.Color.RED,TreeNode.Color.BLACK]

            self.assertEqual(tree_colors, real_colors)

        def test_case_6_remove_Person(self):
            """Test Case 6: The sibling is black, and both nephew are also black but the parent is red."""
            self.tree_set_P.add_all([10, 5, 17, 3, 7, 15, 25])
            self.tree_set_P._TreeSet__root.color=TreeNode.Color.RED
            self.tree_set_P._TreeSet__root.left.color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.right.color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.right.right.color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.right.left.color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.left.left.color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.left.right.color=TreeNode.Color.BLACK
            self.tree_set_P.remove(5)
            self.assertEqual(self.tree_set_P._TreeSet__root.color, TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_P._TreeSet__root.right.color, TreeNode.Color.RED)

        def test_case_7_remove_Person(self):
            """Test Case 7: The sibling is black, and furthest nephew is red."""
            self.tree_set_P.add_all([10, 5, 19, 3, 7, 15, 25])
            for node in self.tree_set_P:
                self.tree_set_P._TreeSet__contains(node).color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.color=TreeNode.Color.RED
            self.tree_set_P._TreeSet__root.left.color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.right.color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.right.right.color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.right.right.color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.right.right.color=TreeNode.Color.RED
            self.tree_set_P._TreeSet__root.right.left.color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.left.left.color=TreeNode.Color.BLACK
            self.tree_set_P._TreeSet__root.left.right.color=TreeNode.Color.BLACK
            self.tree_set_P.remove(5)
            self.assertEqual(self.tree_set_P._TreeSet__root.color, TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_P._TreeSet__root.right.color, TreeNode.Color.BLACK)'''
        



if __name__ == '__main__':
    unittest.main()
