"""Test Red-Black Tree implementation module"""
import unittest
from tree_set import RedBlackTree as RBTree


class TestRBTree(unittest.TestCase):
    """Test Red-Black Tree implementation"""

    def setUp(self):
        """Set up empty, one item and many items trees"""
        self.empty_tree = RBTree(int)

        self.one_item_tree = RBTree(int)
        self.one_item_tree.add(1)

        self.many_items_tree = RBTree(int)

        for num in range(10):
            self.many_items_tree.add(num)

    def test_empty_size(self):
        """Test size of empty tree"""
        self.assertEqual(self.empty_tree.size(), 0, "Empty tree size must be 0")

    def test_empty_is_empty(self):
        """Test if empty tree is empty"""
        self.assertTrue(self.empty_tree.is_empty(), "Empty tree must be empty")

    def test_empty_clear(self):
        """Test clear of empty tree"""
        self.empty_tree.clear()
        self.assertEqual(self.empty_tree.size(), 0,
                         "Empty tree size must be 0 after clear")
        self.assertTrue(self.empty_tree.is_empty(),
                        "Empty tree must be empty after clear")

    def test_empty_contains(self):
        """Test if empty tree contains value"""
        self.assertFalse(1 in self.empty_tree,
                         "Empty tree must not contain any value")

    def test_empty_remove(self):
        ""
        self.assertFalse(self.empty_tree.remove(1),
                         "Empty tree must not remove any value")

    def test_empty_add(self):
        """Test adding value to empty tree"""
        self.empty_tree.add(1)
        self.assertEqual(self.empty_tree.size(), 1,
                         "Empty tree size must be 1 after adding one item")
        self.assertTrue(1 in self.empty_tree,
                        "Empty tree must contain added value")

    def test_empty_iter(self):
        """Test iteration over empty tree"""
        self.assertEqual(list(self.empty_tree), [],
                         "Empty tree must return empty list")

    def test_empty_reversed(self):
        """Test reversed iteration over empty tree"""
        self.assertEqual(list(reversed(self.empty_tree)), [],
                         "Empty tree must return empty list")

    def test_empty_equal(self):
        """Test equality of empty trees"""
        other = RBTree(int)
        self.assertEqual(self.empty_tree, other, "Empty trees must be equal")

    def test_one_item_size(self):
        """Test size of one item tree"""
        self.assertEqual(self.one_item_tree.size(), 1,
                         "One item tree size must be 1")

    def test_one_item_is_empty(self):
        """Test if one item tree is empty"""
        self.assertFalse(self.one_item_tree.is_empty(),
                         "One item tree must not be empty")

    def test_one_item_clear(self):
        """Test clear of one item tree"""
        self.one_item_tree.clear()
        self.assertEqual(self.one_item_tree.size(), 0,
                         "One item tree size must be 0 after clear")
        self.assertTrue(self.one_item_tree.is_empty(),
                        "One item tree must be empty after clear")

    def test_one_item_contains(self):
        """Test if one item tree contains value"""
        self.assertTrue(1 in self.one_item_tree,
                        "One item tree must contain added value")

    def test_one_item_remove(self):
        """Test removing value from one item tree"""
        self.assertTrue(self.one_item_tree.remove(1),
                        "One item tree must remove added value")
        self.assertFalse(1 in self.one_item_tree,
                         "One item tree must not contain removed value")

    def test_one_item_add(self):
        """Test adding value to one item tree"""
        self.one_item_tree.add(1)
        self.assertEqual(self.one_item_tree.size(), 1,
                         "One item tree size must be 1 after adding one item")
        self.assertTrue(1 in self.one_item_tree,
                        "One item tree must contain added value")

    def test_one_item_iter(self):
        """Test iteration over one item tree"""
        self.assertEqual(list(self.one_item_tree), [1],
                         "One item tree must return list with one item")

    def test_one_item_reversed(self):
        """Test reversed iteration over one item tree"""
        self.assertEqual(list(reversed(self.one_item_tree)), [1],
                         "One item tree must return list with one item")

    def test_one_item_equal(self):
        """Test equality of one item trees"""
        other = RBTree(int)
        other.add(1)
        self.assertEqual(self.one_item_tree, other,
                         "One item trees must be equal")

    def test_many_items_size(self):
        """Test size of many items tree"""
        self.assertEqual(self.many_items_tree.size(), 10,
                         "Many items tree size must be 10")

    def test_many_items_is_empty(self):
        """Test if many items tree is empty"""
        self.assertFalse(self.many_items_tree.is_empty(),
                         "Many items tree must not be empty")

    def test_many_items_clear(self):
        """Test clear of many items tree"""
        self.many_items_tree.clear()
        self.assertEqual(self.many_items_tree.size(), 0,
                         "Many items tree size must be 0 after clear")
        self.assertTrue(self.many_items_tree.is_empty(),
                        "Many items tree must be empty after clear")

    def test_many_items_contains(self):
        """Test if many items tree contains values"""
        for num in range(10):
            self.assertTrue(num in self.many_items_tree,
                            "Many items tree must contain added values")

    def test_many_items_remove(self):
        """Test removing values from many items tree"""
        for num in range(10):
            self.assertTrue(self.many_items_tree.remove(num),
                            "Many items tree must remove added values")
            self.assertFalse(num in self.many_items_tree,
                             "Many items tree must not contain removed values")

    def test_many_items_add(self):
        """Test adding values to many items tree"""
        for num in range(10):
            self.many_items_tree.add(num)
            self.assertEqual(self.many_items_tree.size(), 10,
                             "Many items tree size must be 10 after adding 10 items")
            self.assertTrue(num in self.many_items_tree,
                            "Many items tree must contain added values")

    def test_many_items_iter(self):
        """Test iteration over many items tree"""
        self.assertEqual(list(self.many_items_tree), list(range(10)),
                         "Many items tree must return list with 10 items")

    def test_many_items_reversed(self):
        """Test reversed iteration over many items tree"""
        self.assertEqual(list(reversed(self.many_items_tree)),
                         list(reversed(range(10))),
                         "Many items tree must return list with 10 items in reversed order")

    def test_many_items_equal(self):
        """Test equality of many items trees"""
        other = RBTree(int)
        for num in range(10):
            other.add(num)
        self.assertEqual(self.many_items_tree, other,
                         "Many items trees must be equal")


if __name__ == '__main__':
    unittest.main()
