
import unittest

from TreeSet import *


class TestInt(unittest.TestCase):
        def setUp(self):
            self.tree_set_str = TreeSet(str)

        def test_add_single_element(self):
            """Tests adding a single element to an empty TreeSet."""
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str.size(), 1)
            self.assertTrue("A" in self.tree_set_str)

        def test_add_all_empty_sequence(self):
            """Tests adding from an empty sequence ."""
            self.tree_set_str.add_all([])
            self.assertEqual(self.tree_set_str.size(), 0)

        def test_add_all_multiple_elements(self):
            """Tests adding from a sequence with multiple elements ."""
            values = ["C", "A", "F", "G", "I", "B"]
            original_size = self.tree_set_str.size()  # Track initial size
            self.tree_set_str.add_all(values)

            expected_list = sorted(values)
            self.assertEqual(self.tree_set_str.size(), len(expected_list) + original_size)  # Consider initial size
            self.assertListEqual(list(self.tree_set_str), expected_list)

        def test_add_all_duplicates(self):
            """Tests adding from a sequence with duplicates."""
            values = ["C", "C", "F", "F", "I", "B"]
            original_size = self.tree_set_str.size()  # Track initial size
            self.tree_set_str.add_all(values)

            expected_list = sorted(set(values))

        def test_remove_from_empty_set(self):
            """Tests removing from an empty TreeSet."""
            self.assertFalse(self.tree_set_str.remove("A"))
            self.assertEqual(self.tree_set_str.size(), 0)

        def test_remove_non_existent_element(self):
            """Tests removing a non-existent element."""
            self.tree_set_str.add("C")
            self.tree_set_str.add("A")

            self.assertFalse(self.tree_set_str.remove("B"))
            self.assertEqual(self.tree_set_str.size(), 2)
            self.assertTrue("C" in self.tree_set_str)
            self.assertTrue("A" in self.tree_set_str)

        def test_remove_leaf_node(self):
            """Tests removing a leaf node."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("D")

            self.assertTrue(self.tree_set_str.remove("B"))
            self.assertEqual(self.tree_set_str.size(), 1)
            self.assertFalse("B" in self.tree_set_str)
            self.assertTrue("D" in self.tree_set_str)

        def test_remove_node_with_single_child(self):
            """Tests removing a node with a single child."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("D")
            self.tree_set_str.add("A")

            self.assertTrue(self.tree_set_str.remove("B"))
            self.assertEqual(self.tree_set_str.size(), 2)
            self.assertFalse("B" in self.tree_set_str)
            self.assertTrue("A" in self.tree_set_str)
            self.assertTrue("D" in self.tree_set_str)

        def test_remove_node_with_two_children(self):
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

        def test_remove_root_node(self):
            """Tests removing the root node ."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("A")
            self.tree_set_str.add("D")

            self.assertTrue(self.tree_set_str.remove("B"))
            self.assertEqual(self.tree_set_str.size(), 2)
            self.assertFalse("B" in self.tree_set_str)
            self.assertTrue("A" in self.tree_set_str)
            self.assertTrue("D" in self.tree_set_str)

        def test_first_element_black(self):
            """Test first node in the tree black."""
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str.__get_color__("A"), TreeNode.Color.BLACK)

        def test_right_child_red(self):
            """Test right child of root in the tree red."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("C")
            self.assertEqual(self.tree_set_str.__get_color__("C"), TreeNode.Color.RED)

        def test_left_child_red(self):
            """Test left child of root in the tree red."""
            self.tree_set_str.add("B")
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str.__get_color__("A"), TreeNode.Color.RED)

        def test_root_recolor(self):
            """Test recolor of the root when in is changed."""
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str.__get_color__("A"), TreeNode.Color.BLACK)
            self.tree_set_str.add("B")
            self.tree_set_str.add("C")
            self.assertEqual(self.tree_set_str.__get_color__("A"), TreeNode.Color.RED)

        def test_left_rotation_recolor(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set_str.add_all(["A","B","C","D","E","F","G"])
            self.assertEqual(self.tree_set_str.__get_color__("A"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("B"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("C"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("D"), TreeNode.Color.RED)
            self.assertEqual(self.tree_set_str.__get_color__("E"), TreeNode.Color.RED)
            self.assertEqual(self.tree_set_str.__get_color__("F"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("G"), TreeNode.Color.RED)
            self.tree_set_str.add("H")
            self.assertEqual(self.tree_set_str.__get_color__("A"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("B"), TreeNode.Color.RED)
            self.assertEqual(self.tree_set_str.__get_color__("C"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("D"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("E"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("F"), TreeNode.Color.RED)
            self.assertEqual(self.tree_set_str.__get_color__("G"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("H"), TreeNode.Color.RED)

        def test_right_rotation_recolor(self):
            """Test nodes recolors and propagations when a new node is inserted."""
            self.tree_set_str.add_all(["H","G","F","E","D","C","B"])
            self.assertEqual(self.tree_set_str.__get_color__("B"), TreeNode.Color.RED)
            self.assertEqual(self.tree_set_str.__get_color__("C"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("D"), TreeNode.Color.RED)
            self.assertEqual(self.tree_set_str.__get_color__("E"), TreeNode.Color.RED)
            self.assertEqual(self.tree_set_str.__get_color__("F"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("G"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("H"), TreeNode.Color.BLACK)
            self.tree_set_str.add("A")
            self.assertEqual(self.tree_set_str.__get_color__("A"), TreeNode.Color.RED)
            self.assertEqual(self.tree_set_str.__get_color__("B"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("C"), TreeNode.Color.RED)
            self.assertEqual(self.tree_set_str.__get_color__("D"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("E"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("F"), TreeNode.Color.BLACK)
            self.assertEqual(self.tree_set_str.__get_color__("G"), TreeNode.Color.RED)
            self.assertEqual(self.tree_set_str.__get_color__("H"), TreeNode.Color.BLACK)


if __name__ == '__main__':
    unittest.main()
