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

        clone_set = original_set.clone()
        self.assertEqual(len(original_set), len(clone_set))
        self.assertEqual(list(original_set), list(clone_set))

        original_set.add(6)
        self.assertNotEqual(len(original_set), len(clone_set))
        self.assertNotEqual(list(original_set), list(clone_set))


    
    def test_is_empty(self):
        treeSet_lleno = TreeSet(int, [1, 4, 2, 6, 8])
        self.assertEqual(len(treeSet_lleno), 5)
        self.assertFalse(treeSet_lleno.is_empty())

        treeSet_vacio = TreeSet(int, [])
        print(treeSet_vacio)
        self.assertTrue(treeSet_vacio.is_empty())

    def test_contains(self):
        tree_set = TreeSet(int, [1,2,3,4,5])
        self.assertTrue(tree_set.contains(1))
        self.assertTrue(tree_set.contains(5))
        self.assertFalse(tree_set.contains(0))
        self.assertFalse(tree_set.contains(9))

    def test_ceiling(self):
        tree_set = TreeSet(int, [1, 3, 5, 7, 9])
        self.assertEqual(tree_set.ceiling(4), 5)
        self.assertEqual(tree_set.ceiling(10), None)
        self.assertNotEqual(tree_set.ceiling(2), 1)
        self.assertNotEqual(tree_set.ceiling(10), 9)


    def test_floor(self):
        tree_set = TreeSet(int, [1, 3, 5, 7, 9])
        self.assertEqual(tree_set.floor(0), None)
        self.assertEqual(tree_set.floor(10), 9)
        self.assertNotEqual(tree_set.floor(4), 5)
        self.assertNotEqual(tree_set.floor(10), None)

    def test_first(self):
        tree_set = TreeSet(int, [1, 2, 3, 4, 5])
        self.assertEqual(tree_set.first(), 1)
        self.assertNotEqual(tree_set.first(), 9)
        self.assertNotEqual(tree_set.first(), 0)


    def test_last(self):
        tree_set = TreeSet(int, [1, 3, 5, 7, 9])
        self.assertEqual(tree_set.last(), 9)
        self.assertNotEqual(tree_set.last(), 10)

    def test_pollfirst(self):
        tree_set = TreeSet(int, [1, 3, 4, 5, 9])
        self.assertEqual(tree_set.pollFirst(), 1)
        self.assertEqual(tree_set.pollFirst(), 3)

        tree_set_2 = TreeSet(int, [])
        self.assertEqual(tree_set_2.pollFirst(), None)
    
    def test_polllast(self):
        tree_set = TreeSet(int, [1, 2, 3, 4, 5])
        self.assertEqual(tree_set.pollLast(), 5)
        self.assertEqual(tree_set.pollLast(), 4)

        tree_set_2 = TreeSet(int, [])
        self.assertEqual(tree_set_2.pollLast(), None)


    def test_iterator(self):
        original_set = TreeSet(int, [4, 2, 6, 1, 3, 5, 7])
        expected_asc_order = [1, 2, 3, 4, 5, 6, 7]
        actual_asc_order = list(original_set.iterator())
        self.assertEqual(actual_asc_order, expected_asc_order)

    def test_descending_iterator(self):
        original_set = TreeSet(int, [4, 2, 6, 1, 3, 5, 7])
        expected_desc_order = [7, 6, 5, 4, 3, 2, 1]
        actual_desc_order = list(original_set.descending_iterator())
        self.assertEqual(actual_desc_order, expected_desc_order)

    def test_lower(self):
        tree_set = TreeSet(int, [1, 3, 5, 7, 9])
        self.assertEqual(tree_set.lower(8), 7)
        self.assertEqual(tree_set.lower(4), 3)
        self.assertNotEqual(tree_set.lower(2), 3)
        self.assertEqual(tree_set.lower(0), None)

    def test_higher(self):
        tree_set = TreeSet(int, [1, 3, 5, 7, 9])
        self.assertEqual(tree_set.higher(8), 9)
        self.assertEqual(tree_set.higher(4), 5)
        self.assertNotEqual(tree_set.higher(2), 1)
        self.assertEqual(tree_set.higher(10), None)






if __name__ == '__main__':
    unittest.main()