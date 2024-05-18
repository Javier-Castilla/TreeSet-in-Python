
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

        def test_remove_node_with_single_child_int(self):
            """Tests removing a node with a single child."""
            self.tree_set_int.add(10)
            self.tree_set_int.add(20)
            self.tree_set_int.add(5)

            self.assertTrue(self.tree_set_int.remove(10))
            self.assertEqual(self.tree_set_int.size(), 2)
            self.assertFalse(10 in self.tree_set_int)
            self.assertTrue(5 in self.tree_set_int)
            self.assertTrue(20 in self.tree_set_int)

        def test_remove_node_with_two_children_int(self):
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

        def test_remove_root_node_int(self):
            """Tests removing the root node ."""
            self.tree_set_int.add(10)
            self.tree_set_int.add(5)
            self.tree_set_int.add(15)

            self.assertTrue(self.tree_set_int.remove(10))
            self.assertEqual(self.tree_set_int.size(), 2)
            self.assertFalse(10 in self.tree_set_int)
            self.assertTrue(5 in self.tree_set_int)
            self.assertTrue(15 in self.tree_set_int)

        def test_remove_leaf_node_int(self):
                """Tests removing a leaf node."""
                self.tree_set_int.add(10)
                self.tree_set_int.add(20)

                self.assertTrue(self.tree_set_int.remove(10))
                self.assertEqual(self.tree_set_int.size(), 1)
                self.assertFalse(10 in self.tree_set_int)
                self.assertTrue(20 in self.tree_set_int)

        def test_remove_non_existent_element_int(self):
                """Tests removing a non-existent element."""
                self.tree_set_int.add(20)
                self.tree_set_int.add(30)

                self.assertFalse(self.tree_set_int.remove(15))
                self.assertEqual(self.tree_set_int.size(), 2)
                self.assertTrue(self.tree_set_int.contains(20))
                self.assertTrue(self.tree_set_int.contains(30))
                self.assertFalse(self.tree_set_int.contains(15))

        def test_clear_int(self):
            """Tests clearing the TreeSet from all its inserted elements."""
            self.tree_set_int.add_all([1, 2, 3, 4, 5])
            self.tree_set_int.clear()
            self.assertEqual(self.tree_set_int.size(), 0)

        def test_clone_multiple_elements_int(self):
            """Tests cloning  multiples elements TreeSet."""
            self.tree_set_int.add_all([10, 20, 30])
            cloned_tree_set_int = self.tree_set_int.clone()
            self.assertEqual(self.tree_set_int.size(), cloned_tree_set_int.size())
            self.assertEqual(self.tree_set_int, cloned_tree_set_int)

        def test_is_empty_int(self):
            """Test the is_empty method for different scenarios"""
            self.tree_set_int.add_all([12, 13, 14])
            self.assertFalse(self.tree_set_int.is_empty())
            self.tree_set_int.remove(12)
            self.assertFalse(self.tree_set_int.is_empty())

        def test_contains_multiple_elements_int(self):
            """Tests contains method on a TreeSet with multiple elements."""
            self.tree_set_int.add_all([10, 20, 30, 40, 50])
            self.assertTrue(self.tree_set_int.contains(10))
            self.assertTrue(self.tree_set_int.contains(30))
            self.assertFalse(self.tree_set_int.contains(15))

        

        def test_ceiling_elements_greater_equal_int(self):
            """Test ceiling method when set contains elements greater than or equal to the given value."""
            self.tree_set_int.add_all([2, 5, 10, 15])
            self.assertEqual(self.tree_set_int.ceiling(10), 10)
            self.assertEqual(self.tree_set_int.ceiling(12), 15)

        def test_ceiling_elements_only_greater_int(self):
            """Test ceiling method when set contains only elements greater than the given value."""
            self.tree_set_int.add_all([15, 20, 25])
            self.assertEqual(self.tree_set_int.ceiling(10), 15)

        def test_ceiling_elements_only_smaller_int(self):
            """Test ceiling method when set contains only elements smaller than the given value."""
            self.tree_set_int.add_all([2, 5, 7])
            self.assertEqual(self.tree_set_int.ceiling(10), None)

        def test_ceiling_between_values_int(self):
            """Test ceiling method when the value is between two values in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.tree_set_int.add(15)
            self.assertEqual(self.tree_set_int.ceiling(8), 10)

        def test_floor_smaller_than_min_int(self):
            """Test floor method when the value is smaller than the minimum value in the set."""
            self.tree_set_int.add(5)
            self.assertEqual(self.tree_set_int.floor(3), None)

        def test_floor_equal_to_value_in_set_int(self):
            """Test floor method when the value is equal to a value in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.assertEqual(self.tree_set_int.floor(5), 5)

        def test_floor_greater_than_max_int(self):
            """Test floor method when the value is greater than the maximum value in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.assertEqual(self.tree_set_int.floor(15), 10)

        def test_floor_between_values_int(self):
            """Test floor method when the value is between two values in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.tree_set_int.add(15)
            self.assertEqual(self.tree_set_int.floor(12), 10)
        
        def test_poll_first_non_empty_set_int(self):
            """Test poll_first method on a non-empty set."""
            self.tree_set_int.add_all([5, 10, 15])
            self.assertEqual(self.tree_set_int.poll_first(), 5)
            self.assertEqual(self.tree_set_int.size(), 2)
            self.assertEqual(list(self.tree_set_int), [10, 15])

        def test_poll_last_non_empty_set_int(self):
            """Test poll_last method on a non-empty set."""
            self.tree_set_int.add_all([5, 10, 15])
            self.assertEqual(self.tree_set_int.poll_last(), 15)
            self.assertEqual(self.tree_set_int.size(), 2)
            self.assertEqual(list(self.tree_set_int), [5, 10])

        def test_iterator_multiple_elements_int(self):
            """Test iterator  method for multiple elements."""
            self.tree_set_int.add_all([15, 20, 25])
            elements = [elem for elem in self.tree_set_int.iterator()]
            self.assertListEqual(elements, [15, 20, 25])

        def test_descending_iterator_multiples_elements_int(self):
            """Test descending_iterator method with multiple elements."""
            self.tree_set_int.add_all([12, 13, 30])
            elements = [elem for elem in self.tree_set_int.descending_iterator()]
            self.assertListEqual(elements, [30, 13, 12])

        def test_lower_smaller_than_min_int(self):
            """Test lower method when the value is smaller than the minimum value in the set."""
            self.tree_set_int.add(5)
            self.assertIsNone(self.tree_set_int.lower(3))

        def test_lower_equal_to_value_in_set_int(self):
            """Test lower method when the value is equal to a value in the set."""
            self.tree_set_int.add_all([5, 10])
            self.assertEqual(self.tree_set_int.lower(5), None)

        def test_lower_greater_than_max_int(self):
            """Test lower method when the value is greater than the maximum value in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.assertEqual(self.tree_set_int.lower(15), 10)

        def test_lower_between_values_int(self):
            """Test lower method when the value is between two values in the set."""
            self.tree_set_int.add(5)
            self.tree_set_int.add(10)
            self.tree_set_int.add(15)
            self.assertEqual(self.tree_set_int.lower(12), 10)

        def test_higher_greater_than_max_int(self):
            """Test higher method when the value is greater than the maximum value in the set."""
            self.tree_set_int.add_all([5, 10, 15])
            self.assertIsNone(self.tree_set_int.higher(20))

        def test_higher_elements_greater_than_value_int(self):
            """Test higher method when set contains elements greater than the given value."""
            self.tree_set_int.add_all([5, 10, 15])
            self.assertEqual(self.tree_set_int.higher(8), 10)

        def test_higher_elements_only_smaller_int(self):
            """Test higher method when set contains only elements smaller than the given value."""
            self.tree_set_int.add_all([2, 5, 7])
            self.assertEqual(self.tree_set_int.higher(10), None)
        
        def test_first_element_black_int(self):
            """Test first node in the tree black."""
            self.tree_set_int.add(1)
            self.assertEqual(self.tree_set_int._TreeSet__get_color(1), RedBlackTree._BLACK)

        def test_right_child_red_int(self):
            """Test right child of root in the tree red."""
            self.tree_set_int.add(2)
            self.tree_set_int.add(3)
            self.assertEqual(self.tree_set_int._TreeSet__get_color(3), RedBlackTree._RED)

        def test_left_child_red_int(self):
            """Test left child of root in the tree red."""
            self.tree_set_int.add(2)
            self.tree_set_int.add(1)
            self.assertEqual(self.tree_set_int._TreeSet__get_color(1), RedBlackTree._RED)

        def test_root_recolor_int(self):
            """Test recolor of the root when in is changed."""
            self.tree_set_int.add(1)
            self.assertEqual(self.tree_set_int._TreeSet__get_color(1), RedBlackTree._BLACK)
            self.tree_set_int.add(2)
            self.tree_set_int.add(3)
            self.assertEqual(self.tree_set_int._TreeSet__get_color(1), RedBlackTree._RED)

        def test_left_rotation_recolor_int(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set_int.add_all([1,2,3,4,5,6,7])
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [RedBlackTree._BLACK, RedBlackTree._BLACK, RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._RED]
            self.tree_set_int.add(8)
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._BLACK, RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._RED]
            self.assertEqual(tree_colors, real_colors)

        def test_right_rotation_recolor_int(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set_int.add_all([8,7,6,5,4,3,2])
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._BLACK, RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)
            self.tree_set_int.add(1)
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._BLACK, RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_case_4_1_int(self):
            """Test Case 4: Uncle is red and the violator node is in external position."""

            self.tree_set_int.add_all([10, 5, 15, 3, 7])
            self.tree_set_int.add(2)
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._BLACK,
                        RedBlackTree._BLACK, RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)
        def test_case_4_2(self):
            """Test Case 4: Uncle is red and the violator node is in internal position."""

            self.tree_set_int.add_all([10, 5, 15, 3, 7])
            self.tree_set_int.add(4)
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._RED, RedBlackTree._BLACK,
                        RedBlackTree._BLACK, RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_Case_5_int(self):
            """Test Case 5: Uncle is black and the violator node is in external position."""
            self.tree_set_int.add_all([10, 5, 15, 3])
            self.tree_set_int.add(2)
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._BLACK,
                        RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_case_6_int(self):
            """Test Case 6: Uncle is black and the violator node is in internal position."""
            self.tree_set_int.add_all([10, 5, 15, 6])
            self.tree_set_int.add(7)
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._RED,
                        RedBlackTree._BLACK, RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)

        
        def test_case_1_b_remove_int(self):
            "Test Case 1b: Node to be removed is the root and have a red son"
            self.tree_set_int.add_all([10, 12])
            self.tree_set_int.remove(10)
            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_Case_2_b_int(self):
            """Test Case 2: Node to be removed is red"""
            self.tree_set_int.add_all([10, 5])
            self.tree_set_int.remove(5)
            tree_color = self.tree_set_int._TreeSet__array_color()
            real_colors = [RedBlackTree._BLACK]
            self.assertEqual(tree_color, real_colors)

        def test_case_5_remove_int(self):
            """Test Case 5: The sibling is red, and both the parent and the sibling's children are black."""
            self.tree_set_int.add_all([10, 3, 13, 16, 20, 12, 2, 5])
            self.tree_set_int.remove(3)

            tree_colors = self.tree_set_int._TreeSet__array_color()
            real_colors = [RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._BLACK, RedBlackTree._RED,
                        RedBlackTree._BLACK,RedBlackTree._RED,RedBlackTree._BLACK]

            self.assertEqual(tree_colors, real_colors)

        def test_case_6_remove_int(self):
            """Test Case 6: The sibling is black, and both nephew are also black but the parent is red."""
            self.tree_set_int.add_all([10, 5, 17, 3, 7, 15, 25])
            self.tree_set_int._RedBlackTree__root.color=RedBlackTree._RED
            self.tree_set_int._RedBlackTree__root.left.color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.right.color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.right.right.color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.right.left.color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.left.left.color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.left.right.color=RedBlackTree._BLACK
            self.tree_set_int.remove(5)
            self.assertEqual(self.tree_set_int._RedBlackTree__root.color, RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_int._RedBlackTree__root.right.color, RedBlackTree._RED)

        def test_case_7_remove_int(self):
            """Test Case 7: The sibling is black, and furthest nephew is red."""
            self.tree_set_int.add_all([10, 5, 19, 3, 7, 15, 25])
            for node in self.tree_set_int:
                self.tree_set_int._RedBlackTree__contains(node).color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.color=RedBlackTree._RED
            self.tree_set_int._RedBlackTree__root.left.color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.right.color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.right.right.color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.right.right.color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.right.right.color=RedBlackTree._RED
            self.tree_set_int._RedBlackTree__root.right.left.color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.left.left.color=RedBlackTree._BLACK
            self.tree_set_int._RedBlackTree__root.left.right.color=RedBlackTree._BLACK
            self.tree_set_int.remove(5)
            self.assertEqual(self.tree_set_int._RedBlackTree__root.color, RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_int._RedBlackTree__root.right.color, RedBlackTree._BLACK)

        #--------------------TESTS PERSON------------------
            
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

        def test_remove_leaf_node_Person(self):
            """Tests removing a leaf node."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)

            self.assertTrue(self.tree_set_P.remove(self.person_test))
            self.assertEqual(self.tree_set_P.size(), 1)
            self.assertFalse(self.person_test in self.tree_set_P)
            self.assertTrue(self.person_test2 in self.tree_set_P)

        def test_remove_non_existent_element_Person(self):
            """Tests removing a non-existent element."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.assertFalse(self.tree_set_P.remove(self.person_test3))
            self.assertEqual(self.tree_set_P.size(), 2)
            self.assertTrue(self.tree_set_P.contains(self.person_test2))
            self.assertTrue(self.tree_set_P.contains(self.person_test))
            self.assertFalse(self.tree_set_P.contains(self.person_test3))   

        def test_clear_Person(self):
            """Tests clearing the TreeSet from all its inserted elements."""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3, self.person_test4, self.person_test5])
            self.tree_set_P.clear()
            self.assertEqual(self.tree_set_P.size(), 0)

        def test_clone_multiple_elements_Person(self):
            """Tests cloning  multiples elements TreeSet."""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3])
            cloned_tree_set_P = self.tree_set_P.clone()
            self.assertEqual(self.tree_set_P.size(), cloned_tree_set_P.size())
            self.assertEqual(self.tree_set_P, cloned_tree_set_P)

        def test_is_empty_Person(self):
            """Test the is_empty method for different scenarios"""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3])
            self.assertFalse(self.tree_set_P.is_empty())
            self.tree_set_P.remove(self.person_test)
            self.assertFalse(self.tree_set_P.is_empty())

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
            self.assertEqual(self.tree_set_P.poll_first(), self.person_test)
            self.assertEqual(self.tree_set_P.size(), 2)
            self.assertEqual(list(self.tree_set_P), [self.person_test3, self.person_test4])

        def test_poll_last_non_empty_set_Person(self):
            """Test poll_last method on a non-empty set."""
            self.tree_set_P.add_all([self.person_test2, self.person_test3, self.person_test4])
            self.assertEqual(self.tree_set_P.poll_last(), self.person_test4)
            self.assertEqual(self.tree_set_P.size(), 2)
            self.assertEqual(list(self.tree_set_P), [self.person_test2, self.person_test3])

        def test_iterator_multiple_elements_Person(self):
            """Test iterator  method for multiple elements."""
            self.tree_set_P.add_all([self.person_test, self.person_test2, self.person_test3])
            elements = [elem for elem in self.tree_set_P.iterator()]
            self.assertListEqual(elements, [self.person_test, self.person_test2, self.person_test3])

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
            self.assertEqual(self.tree_set_P._TreeSet__get_color(self.person_test), RedBlackTree._BLACK)

        def test_right_child_red_Person(self):
            """Test right child of root in the tree red."""
            self.tree_set_P.add(self.person_test)
            self.tree_set_P.add(self.person_test2)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(self.person_test2), RedBlackTree._RED)

        def test_left_child_red_Person(self):
            """Test left child of root in the tree red."""
            self.tree_set_P.add(self.person_test2)
            self.tree_set_P.add(self.person_test)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(self.person_test), RedBlackTree._RED)

        def test_root_recolor_Person(self):
            """Test recolor of the root when in is changed."""
            self.tree_set_P.add(self.person_test)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(self.person_test), RedBlackTree._BLACK)
            self.tree_set_P.add(self.person_test2)
            self.tree_set_P.add(self.person_test3)
            self.assertEqual(self.tree_set_P._TreeSet__get_color(self.person_test), RedBlackTree._RED)

        #---------------TESTS NO COMPARABLE PERSON------------------

        def test_Create_Tree_Person_NoComparable(self):
            """Tests removing a node with a single child."""
            with self.assertRaises(NonComparableObjectError):
                        self.tree_set_P2 = TreeSet(Person_NoComparable)            


        #---------------TESTS HALF COMPARABLE PERSON------------------

        def test_remove_node_with_single_child_Person_HalfComparable(self):
            """Tests removing a node with a single child."""
            self.tree_set_P3.add(self.person_test_HC)
            self.tree_set_P3.add(self.person_test2_HC)
            self.tree_set_P3.add(self.person_test3_HC)
            self.assertTrue(self.tree_set_P3.remove(self.person_test2_HC))
            self.assertEqual(self.tree_set_P3.size(), 2)

        def test_remove_node_with_two_children_Person_HalfComparable(self):
            """Tests removing a node with two children (replaces with successor)."""
            self.tree_set_P3.add(self.person_test_HC)
            self.tree_set_P3.add(self.person_test2_HC)
            self.tree_set_P3.add(self.person_test3_HC)
            self.assertTrue(self.tree_set_P3.remove(self.person_test2_HC))
            self.assertEqual(self.tree_set_P3.size(), 2)

        def test_remove_root_node_Person_HalfComparable(self):
            """Tests removing the root node ."""
            self.tree_set_P3.add(self.person_test_HC)
            self.tree_set_P3.add(self.person_test2_HC)
            self.tree_set_P3.add(self.person_test3_HC)
            self.assertTrue(self.tree_set_P3.remove(self.person_test2_HC))
            self.assertEqual(self.tree_set_P3.size(), 2)

        def test_clear_Person_HalfComparable(self):
            """Tests clearing the TreeSet from all its inserted elements."""
            self.tree_set_P3.add_all([self.person_test_HC, self.person_test2_HC, self.person_test3_HC])
            self.tree_set_P3.clear()
            self.assertEqual(self.tree_set_P3.size(), 0)

        #------------------------TESTS STR------------------

        def test_remove_node_with_single_child_str(self):
            """Tests removing a node with a single child."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("D")
            self.tree_set_str.add("A")

            self.assertTrue(self.tree_set_str.remove("B"))
            self.assertEqual(self.tree_set_str.size(), 2)
            self.assertFalse("B" in self.tree_set_str)
            self.assertTrue("A" in self.tree_set_str)
            self.assertTrue("D" in self.tree_set_str)

        def test_remove_node_with_two_children_str(self):
            """Tests removing a node with two children (replaces with successor)."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("A")
            self.tree_set_str.add("D")
            self.tree_set_str.add("C")

            self.assertTrue(self.tree_set_str.remove("B"))
            self.assertEqual(self.tree_set_str.size(), 3)
            self.assertFalse("B" in self.tree_set_str)
            self.assertTrue("A" in self.tree_set_str)
            self.assertTrue("C" in self.tree_set_str)
            self.assertTrue("D" in self.tree_set_str)

        def test_remove_root_node_str(self):
            """Tests removing the root node ."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("A")
            self.tree_set_str.add("D")

            self.assertTrue(self.tree_set_str.remove("B"))
            self.assertEqual(self.tree_set_str.size(), 2)
            self.assertFalse("B" in self.tree_set_str)
            self.assertTrue("A" in self.tree_set_str)
            self.assertTrue("D" in self.tree_set_str)

        def test_remove_leaf_node_str(self):
            """Tests removing a leaf node."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("D")
            self.assertTrue(self.tree_set_str.remove("B"))
            self.assertEqual(self.tree_set_str.size(), 1)
            self.assertFalse("B" in self.tree_set_str)
            self.assertTrue("D" in self.tree_set_str)

        def test_remove_non_existent_element_str(self):
            """Tests removing a non-existent element."""
            self.tree_set_str.add("C")
            self.tree_set_str.add("A")
            self.assertFalse(self.tree_set_str.remove("B"))
            self.assertEqual(self.tree_set_str.size(), 2)
            self.assertTrue(self.tree_set_str.contains("A"))
            self.assertTrue(self.tree_set_str.contains("C"))
            self.assertFalse(self.tree_set_str.contains("B"))        

        def test_clear_str(self):
            """Tests clearing the TreeSet from all its inserted elements."""
            self.tree_set_str.add_all(["A", "B", "C", "D", "E"])
            self.tree_set_str.clear()
            self.assertEqual(self.tree_set_str.size(), 0)

        def test_clone_multiple_elements_str(self):
            """Tests cloning  multiples elements TreeSet."""
            self.tree_set_str.add_all(["E", "M", "P"])
            cloned_tree_set_str = self.tree_set_str.clone()
            self.assertEqual(self.tree_set_str.size(), cloned_tree_set_str.size())
            self.assertEqual(self.tree_set_str, cloned_tree_set_str)

        def test_contains_multiple_elements_str(self):
            """Tests contains method on a TreeSet with multiple elements."""
            self.tree_set_str.add_all(["A", "B", "C", "D", "E"])
            self.assertTrue(self.tree_set_str.contains("A"))
            self.assertTrue(self.tree_set_str.contains("C"))
            self.assertFalse(self.tree_set_str.contains("G"))

        

        def test_ceiling_elements_greater_equal_str(self):
            """Test ceiling method when set contains elements greater than or equal to the given value."""
            self.tree_set_str.add_all(["A", "B", "G", "O"])
            self.assertEqual(self.tree_set_str.ceiling("A"), "A")
            self.assertEqual(self.tree_set_str.ceiling("C"), "G")

        def test_ceiling_elements_only_greater_str(self):
            """Test ceiling method when set contains only elements greater than the given value."""
            self.tree_set_str.add_all(["C", "D", "Z"])
            self.assertEqual(self.tree_set_str.ceiling("A"), "C")

        def test_ceiling_elements_only_smaller_str(self):
            """Test ceiling method when set contains only elements smaller than the given value."""
            self.tree_set_str.add_all(["A", "B", "C"])
            self.assertEqual(self.tree_set_str.ceiling("X"), None)


        def test_floor_smaller_than_min_str(self):
            """Test floor method when the value is smaller than the minimum value in the set."""
            self.tree_set_str.add("C")
            self.assertEqual(self.tree_set_str.floor("A"), None)

        def test_floor_equal_to_value_in_set_str(self):
            """Test floor method when the value is equal to a value in the set."""
            self.tree_set_str.add("A")
            self.tree_set_str.add("D")
            self.assertEqual(self.tree_set_str.floor("A"), "A")

        def test_floor_greater_than_max_str(self):
            """Test floor method when the value is greater than the maximum value in the set."""
            self.tree_set_str.add("A")
            self.tree_set_str.add("C")
            self.assertEqual(self.tree_set_str.floor("G"), "C")

        def test_floor_between_values_str(self):
            """Test floor method when the value is between two values in the set."""
            self.tree_set_str.add("A")
            self.tree_set_str.add("B")
            self.tree_set_str.add("N")
            self.assertEqual(self.tree_set_str.floor("D"), "B")

        def test_poll_first_non_empty_set_str(self):
            """Test poll_first method on a non-empty set."""
            self.tree_set_str.add_all(["A", "B", "C"])
            self.assertEqual(self.tree_set_str.poll_first(), "A")
            self.assertEqual(self.tree_set_str.size(), 2)
            self.assertEqual(list(self.tree_set_str), ["B", "C"])

        def test_poll_last_non_empty_set_str(self):
            """Test poll_last method on a non-empty set."""
            self.tree_set_str.add_all(["A", "C", "D"])
            self.assertEqual(self.tree_set_str.poll_last(), "D")
            self.assertEqual(self.tree_set_str.size(), 2)
            self.assertEqual(list(self.tree_set_str), ["A", "C"])

        def test_iterator_multiple_elements_str(self):
            """Test iterator  method for multiple elements."""
            self.tree_set_str.add_all(["A", "B", "C"])
            elements = [elem for elem in self.tree_set_str.iterator()]
            self.assertListEqual(elements, ["A", "B", "C"])

        def test_descending_iterator_multiples_elements_str(self):
            """Test descending_iterator method with multiple elements."""
            self.tree_set_str.add_all(["N", "M", "Ñ"])
            elements = [elem for elem in self.tree_set_str.descending_iterator()]
            self.assertListEqual(elements, ["Ñ", "N", "M"])

        def test_lower_smaller_than_min_str(self):
            """Test lower method when the value is smaller than the minimum value in the set."""
            self.tree_set_str.add("C")
            self.assertIsNone(self.tree_set_str.lower("B"))

        def test_lower_equal_to_value_in_set_str(self):
            """Test lower method when the value is equal to a value in the set."""
            self.tree_set_str.add_all(["A", "C"])
            self.assertEqual(self.tree_set_str.lower("A"), None)

        def test_lower_greater_than_max_str(self):
            """Test lower method when the value is greater than the maximum value in the set."""
            self.tree_set_str.add("A")
            self.tree_set_str.add("B")
            self.assertEqual(self.tree_set_str.lower("D"), "B")

        def test_lower_between_values_str(self):
            """Test lower method when the value is between two values in the set."""
            self.tree_set_str.add("A")
            self.tree_set_str.add("B")
            self.tree_set_str.add("C")
            self.assertEqual(self.tree_set_str.lower("L"), "C")

        

        def test_higher_greater_than_max_str(self):
            """Test higher method when the value is greater than the maximum value in the set."""
            self.tree_set_str.add_all(["A", "C", "R"])
            self.assertIsNone(self.tree_set_str.higher("X"))

        def test_higher_elements_greater_than_value_str(self):
            """Test higher method when set contains elements greater than the given value."""
            self.tree_set_str.add_all(["A", "B", "Z"])
            self.assertEqual(self.tree_set_str.higher("E"), "Z")

        def test_higher_elements_only_smaller_str(self):
            """Test higher method when set contains only elements smaller than the given value."""
            self.tree_set_str.add_all(["A", "N", "Ñ"])
            self.assertEqual(self.tree_set_str.higher("B"), "N")

        def test_first_element_black_str(self):
            """Test first node in the tree black."""
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str._TreeSet__get_color("A"), RedBlackTree._BLACK)

        def test_right_child_red_str(self):
            """Test right child of root in the tree red."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("C")
            self.assertEqual(self.tree_set_str._TreeSet__get_color("C"), RedBlackTree._RED)

        def test_left_child_red_str(self):
            """Test left child of root in the tree red."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str._TreeSet__get_color("A"), RedBlackTree._RED)

        def test_root_recolor_str(self):
            """Test recolor of the root when in is changed."""
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str._TreeSet__get_color("A"), RedBlackTree._BLACK)
            self.tree_set_str.add("B")
            self.tree_set_str.add("C")
            self.assertEqual(self.tree_set_str._TreeSet__get_color("A"), RedBlackTree._RED)

        def test_left_rotation_recolor_str(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set_str.add_all(["A","B","C","D","E","F","G"])
            self.assertEqual(self.tree_set_str._TreeSet__get_color("A"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("B"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("C"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("D"), RedBlackTree._RED)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("E"), RedBlackTree._RED)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("F"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("G"), RedBlackTree._RED)
            self.tree_set_str.add("H")
            self.assertEqual(self.tree_set_str._TreeSet__get_color("A"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("B"), RedBlackTree._RED)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("C"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("D"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("E"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("F"), RedBlackTree._RED)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("G"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("H"), RedBlackTree._RED)

        def test_right_rotation_recolor_str(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set_str.add_all(["H","G","F","E","D","C","B"])
            self.assertEqual(self.tree_set_str._TreeSet__get_color("B"), RedBlackTree._RED)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("C"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("D"), RedBlackTree._RED)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("E"), RedBlackTree._RED)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("F"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("G"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("H"), RedBlackTree._BLACK)
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str._TreeSet__get_color("A"), RedBlackTree._RED)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("B"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("C"), RedBlackTree._RED)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("D"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("E"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("F"), RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("G"), RedBlackTree._RED)
            self.assertEqual(self.tree_set_str._TreeSet__get_color("H"), RedBlackTree._BLACK)

        def test_case_4_1_str(self):
            """Test Case 4: Uncle is red and the violator node is in external position."""

            self.tree_set_str.add_all(["J", "E", "O", "C", "G"])
            self.tree_set_str.add("B")
            tree_colors = self.tree_set_str._TreeSet__array_color()
            real_colors = [RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._BLACK,
                           RedBlackTree._BLACK, RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_case_4_2_str(self):
            """Test Case 4: Uncle is red and the violator node is in internal position."""

            self.tree_set_str.add_all(["J", "E", "O", "C", "G"])
            self.tree_set_str.add("D")
            tree_colors = self.tree_set_str._TreeSet__array_color()
            real_colors = [RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._RED, RedBlackTree._BLACK,
                           RedBlackTree._BLACK, RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_Case_5_str(self):
            """Test Case 5: Uncle is black and the violator node is in external position."""
            self.tree_set_str.add_all(["J", "E", "O", "C"])
            self.tree_set_str.add("B")
            tree_colors = self.tree_set_str._TreeSet__array_color()
            real_colors = [RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._BLACK,
                           RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_case_6_str(self):
            """Test Case 6: Uncle is black and the violator node is in internal position."""
            self.tree_set_str.add_all(["J", "E", "O", "F"])
            self.tree_set_str.add("G")
            tree_colors = self.tree_set_str._TreeSet__array_color()
            real_colors = [RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._RED,
                           RedBlackTree._BLACK, RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_case_1_b_remove_str(self):
            "Test Case 1b: Node to be removed is the root and have a red son"
            self.tree_set_str.add_all(["J", "L"])
            self.tree_set_str.remove("J")
            tree_colors = self.tree_set_str._TreeSet__array_color()
            real_colors = [RedBlackTree._BLACK]
            self.assertEqual(tree_colors, real_colors)

        def test_Case_2_b_remove_str(self):
            """Test Case 2: Node to be removed is red"""
            self.tree_set_str.add_all(["J", "E"])
            self.tree_set_str.remove("E")
            tree_color = self.tree_set_str._TreeSet__array_color()
            real_colors = [RedBlackTree._BLACK]
            self.assertEqual(tree_color, real_colors)

        def test_case_5_remove_str(self):
            """Test Case 5: The sibling is red, and both the parent and the sibling's children are black."""
            self.tree_set_str.add_all(["J", "C", "M", "P", "T", "L", "B", "E"])
            self.tree_set_str.remove("C")

            tree_colors = self.tree_set_str._TreeSet__array_color()
            real_colors = [RedBlackTree._RED, RedBlackTree._BLACK, RedBlackTree._BLACK, RedBlackTree._RED,
                           RedBlackTree._BLACK, RedBlackTree._RED, RedBlackTree._BLACK]

            self.assertEqual(tree_colors, real_colors)

        def test_case_6_remove_str(self):
            """Test Case 6: The sibling is black, and both nephew are also black but the parent is red."""
            self.tree_set_str.add_all(["J", "E", "Q", "C", "G", "O", "Y"])
            self.tree_set_str._RedBlackTree__root.color = RedBlackTree._RED
            self.tree_set_str._RedBlackTree__root.left.color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.right.color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.right.right.color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.right.left.color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.left.left.color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.left.right.color = RedBlackTree._BLACK
            self.tree_set_str.remove("E")
            self.assertEqual(self.tree_set_str._RedBlackTree__root.color, RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._RedBlackTree__root.right.color, RedBlackTree._RED)

        def test_case_7_remove_str(self):
            """Test Case 7: The sibling is black, and furthest nephew is red."""
            self.tree_set_str.add_all(["J", "E", "S", "C", "G", "O", "Y"])
            for node in self.tree_set_str:
                self.tree_set_str._RedBlackTree__contains(node).color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.color = RedBlackTree._RED
            self.tree_set_str._RedBlackTree__root.left.color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.right.color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.right.right.color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.right.right.color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.right.right.color = RedBlackTree._RED
            self.tree_set_str._RedBlackTree__root.right.left.color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.left.left.color = RedBlackTree._BLACK
            self.tree_set_str._RedBlackTree__root.left.right.color = RedBlackTree._BLACK
            self.tree_set_str.remove("E")
            self.assertEqual(self.tree_set_str._RedBlackTree__root.color, RedBlackTree._BLACK)
            self.assertEqual(self.tree_set_str._RedBlackTree__root.right.color, RedBlackTree._BLACK)

if __name__ == '__main__':
    unittest.main()
