import unittest
from TreeSet import TreeSet


class TestTreeSet(unittest.TestCase):
    def test_add(self):
        tree_set = TreeSet(int)
        self.assertTrue(tree_set.is_empty())

        tree_set.add(5)
        self.assertEqual(len(tree_set), 1)
        self.assertTrue(tree_set.contains(5))

        tree_set.add(10)
        tree_set.add(3)
        self.assertEqual(len(tree_set), 3)
        self.assertTrue(tree_set.contains(10))
        self.assertTrue(tree_set.contains(3))

    def test_add_all(self):
        tree_set = TreeSet(int)
        self.assertTrue(tree_set.is_empty())

        tree_set.add_all([1, 2, 3, 4, 5])
        self.assertEqual(len(tree_set), 5)



    def test_remove(self):
        tree_set = TreeSet(int, [1, 2, 3, 4, 5])
        self.assertEqual(len(tree_set), 5)

        tree_set.remove(3)
        self.assertEqual(len(tree_set), 4)
        self.assertFalse(tree_set.contains(3))

        tree_set.remove(10)  # Trying to remove a non-existent element
        self.assertEqual(len(tree_set), 4)  # Size should remain the same

    def test_clear(self):
        tree_set = TreeSet(int, [1, 2, 3, 4, 5])
        self.assertEqual(len(tree_set), 5)

        self.assertNotEqual(tree_set.clear(), 5)
        self.assertEqual(tree_set.clear(), None)

    def test_clone(self):
        original_set = TreeSet(int, [1, 2, 3, 4, 5])
        self.assertEqual(len(original_set), 5)

        cloned_set = original_set.clone()
        print(cloned_set)
        print(original_set)
        self.assertEqual(len(original_set), len(cloned_set))
        self.assertListEqual(list(original_set), list(cloned_set))
        self.assertEqual(original_set, cloned_set)

        original_set.add(6)
        self.assertEqual(len(original_set), 6)
        self.assertEqual(len(cloned_set), 5)

        self.assertTrue(original_set, cloned_set)
    
    #def test_is_empty(self):
    #    treeSet = TreeSet(int, [1, 4, 2, 6, 8])
    #    self.assertEqual(len(treeSet), 5)
    #    print(treeSet.is_empty())
    #    self.assertTrue(treeSet.is_empty())


    def test_ceiling(self):
        tree_set = TreeSet(int, [1, 3, 5, 7, 9])
        self.assertEqual(tree_set.ceiling(4), 5)
        self.assertEqual(tree_set.ceiling(10), None)



if __name__ == '__main__':
    unittest.main()