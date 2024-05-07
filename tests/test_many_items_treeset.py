import unittest
from TreeSet import *


class TestManyItemsTreeSet(unittest.TestCase):
    def setUp(self) -> None:
        self.tree_type = int
        self.items = set([randint(0, 100) for _ in range(10)])
        self.tree = TreeSet(self.tree_type, self.items)
        self.ordered_items = sorted(list(self.items))

    def test_size(self):
        self.assertEqual(self.tree.size(), len(self.items), "TreeSet must be 10")

    def test_remove(self):
        for num in self.items:
            self.assertTrue(self.tree.remove(num), "Wrong value after deleting")

        self.assertEqual(self.tree.size(), 0, "TreeSet size must be 0 after deleting all items")
        self.assertTrue(self.tree.is_empty(), "TreeSet must be empty after deleting all items")

    def test_clear(self):
        self.tree.clear()
        self.assertEqual(self.tree.size(), 0, "TreeSet size must be 0 after deleting all items")
        self.assertTrue(self.tree.is_empty(), "TreeSet must be empty after deleting all items")

    def test_higher(self):
        for index, item in enumerate(self.ordered_items[:-1]):
            self.assertEqual(self.tree.higher(item), self.ordered_items[index + 1], "Wrong higher value")

    def test_lower(self):
        for index, item in enumerate(self.ordered_items[1:]):
            self.assertEqual(self.tree.lower(item), self.ordered_items[index], "Wrong lower value")

    def test_ceiling(self):
        for index, item in enumerate(self.ordered_items):
            self.assertEqual(self.tree.ceiling(item), self.ordered_items[index], "Wrong ceiling value")

    def test_floor(self):
        for index, item in enumerate(self.ordered_items):
            self.assertEqual(self.tree.floor(item), self.ordered_items[index], "Wrong ceiling value")

    def test_first(self):
        self.assertEqual(self.tree.first(), min(self.items), "Wrong TreeSet first value")

    def test_last(self):
        self.assertEqual(self.tree.last(), max(self.items), "Wrong TreeSet last value")

    def test_poll_first(self):
        items_len = self.tree.size()

        for index in range(items_len):
            self.assertEqual(self.tree.poll_first(), self.ordered_items[index],
                             "Wrong deleted first value from TreeSet")

        self.assertEqual(self.tree.size(), 0, "TreeSet size must be 0 after deleting all items")

    def test_poll_last(self):
        items_len = self.tree.size()

        for index in range(items_len - 1, -1, -1):
            self.assertEqual(
                self.tree.poll_last(), self.ordered_items[index], "Wrong deleted last value from TreeSet"
            )

        self.assertEqual(self.tree.size(), 0, "TreeSet size must be 0 after deleting all items")

    def test_iterator(self):
        for index, item in enumerate(self.tree.iterator()):
            self.assertEqual(item, self.ordered_items[index], "Wrong value when using TreeSet iteration")

    def test_descending_iterator(self):
        for index, item in enumerate(self.tree.descending_iterator()):
            self.assertEqual(
                item, self.ordered_items[len(self.ordered_items) - 1 - index],
                "Wrong value when using TreeSet descending iterator"
            )

    def test_clone(self):
        cloned_tree = self.tree.clone()
        self.assertEqual(self.tree, cloned_tree, "Cloned tree is not equal to base tree")
        self.assertEqual(self.tree.size(), cloned_tree.size())
        self.assertFalse(cloned_tree.is_empty())


if __name__ == '__main__':
    unittest.main()
