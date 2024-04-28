import unittest
from TreeSet import *

class TestManyItemsTreeSet(unittest.TestCase):
    def setUp(self) -> None:
        self.tree_type = int
        self.items = set([randint(0, 100) for _ in range(10)])
        self.tree = TreeSet(self.tree_type, self.items)
        self.ordered_items = [item for item in self.tree.iterator()]

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
            print(index, item)
            self.assertEqual(self.tree.higher(item), self.ordered_items[index + 1], "Wrong higher value")

    def test_lower(self):
        for index, item in enumerate(self.ordered_items[1:]):
            print(index, item)
            self.assertEqual(self.tree.higher(item), self.ordered_items[index - 1], "Wrong lower value")

    def test_ceiling(self):
        for index, item in enumerate(self.ordered_items[1:]):
            print(index, item)
            self.assertEqual(self.tree.ceiling(item), self.ordered_items[index], "Wrong ceiling value")

    def test_floor(self):
        for index, item in enumerate(self.ordered_items[1:]):
            print(index, item)
            self.assertEqual(self.tree.floor(item), self.ordered_items[index], "Wrong ceiling value")

    def test_first(self):
        self.assertEqual(self.tree.first(), min(self.items), "Wrong TreeSet first value")

    def test_last(self):
        self.assertEqual(self.tree.last(), max(self.items), "Wrong TreeSet last value")

    def test_poll_first(self):
        items_len = self.tree.size()
        for index in range(items_len):
            self.assertEqual(self.tree.poll_first(), self.ordered_items[index], "Wrong deleted first value from TreeSet")

        self.assertEqual(self.tree.size(), 0, "TreeSet size must be 0 after deleting all items")

    def test_poll_last(self):
        items_len = self.tree.size()

        for index in range(self.tree.size()):
            self.assertEqual(self.tree.poll_first(), self.ordered_items[items_len - index], "Wrong deleted last value from TreeSet")

        self.assertEqual(self.tree.size(), 0, "TreeSet size must be 0 after deleting all items")

if __name__ == '__main__':
    unittest.main()
