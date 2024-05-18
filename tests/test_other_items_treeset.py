import random
import unittest
from TreeSet import TreeSet
from tests.tests_classes import *


class TestOtherItemsTreeSet(unittest.TestCase):
    def setUp(self) -> None:
        self.tree_person = TreeSet(Person)
        self.tree_worker = TreeSet(Worker)
        self.tree_professor = TreeSet(Professor)

    def test_tree_with_person(self):
        tree = TreeSet(Person)
        ids = {random.randint(10, 40) for _ in range(10)}
        ids = sorted(list(ids))
        items = [Person(f"Person{identifier}", identifier) for identifier in ids]

        for item in items:
            self.assertTrue(tree.add(item),
                            "Wrong value after inserting new element")

        self.assertEqual(tree.size(), len(ids), "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")
        self.assertEqual(tree.higher(items[0]), items[1], "Wrong higher value")
        self.assertEqual(tree.lower(items[-1]), items[-2], "Wrong lower value")
        self.assertEqual(tree.ceiling(items[0]), items[0], "Wrong ceiling value")
        self.assertEqual(tree.floor(items[-1]), items[-1], "Wrong floor value")
        self.assertEqual(tree.first(), items[0], "Wrong first value")
        self.assertEqual(tree.last(), items[-1], "Wrong last value")

        self.assertEqual([person for person in tree.iterator()], items, "Wrong iterator values")
        self.assertEqual([person for person in tree.descending_iterator()], items[::-1], "Wrong descending iterator values")

        for person in items:
            self.assertTrue(tree.contains(person), "Tree must contain the element")

        tree_clone = tree.clone()
        self.assertEqual(tree, tree_clone, "Tree and clone must be equal")

        for index in range(len(items)):
            self.assertEqual(tree.poll_first(), items[index], "Wrong poll first value")

        for index in range(1, len(items) + 1):
            print(tree_clone)
            self.assertEqual(tree_clone.poll_last(), items[-index], "Wrong poll last value")

    def test_add2(self):
        tree = TreeSet(Professor)
        items = [Professor(f"Professor{num}", num) for num in range(10)]

        for item in items:
            self.assertTrue(tree.add(item),
                            "Wrong value after inserting new value")

        self.assertEqual(tree.size(), 10, "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")

    def test_add3(self):
        tree = TreeSet(Worker)

        items = [Professor(f"Professor{num}", num) for num in range(10)]

        for item in items:
            self.assertTrue(tree.add(item),
                            "Wrong value after inserting new value")

        self.assertEqual(tree.size(), 10, "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")

    def test_empty_tree(self):
        tree = TreeSet(Person)
        self.assertTrue(tree.is_empty(), "Tree should be empty")

    def test_add_and_check_empty(self):
        tree = TreeSet(Person)
        tree.add(Person("Person1", 10))
        self.assertFalse(tree.is_empty(), "Tree should not be empty")

    def test_add_and_remove_check_empty(self):
        tree = TreeSet(Person)
        person = Person("Person1", 10)
        tree.add(person)
        tree.remove(person)
        self.assertTrue(tree.is_empty(),
                        "Tree should be empty after removing the element")

    def test_tree_size(self):
        tree = TreeSet(Person)
        items = [Person(f"Person{num}", num * 10) for num in range(10)]
        for item in items:
            tree.add(item)
        self.assertEqual(tree.size(), 10, "Tree size should be 10")

    def test_contains(self):
        tree = TreeSet(Person)
        person = Person("Person1", 10)
        tree.add(person)
        self.assertTrue(tree.contains(person),
                        "Tree should contain the added element")

    def test_not_contains(self):
        tree = TreeSet(Person)
        person1 = Person("Person1", 10)
        person2 = Person("Person2", 20)
        tree.add(person1)
        self.assertFalse(tree.contains(person2),
                         "Tree should not contain an element that was not added")

    def test_first_last(self):
        tree = TreeSet(Person)
        items = [Person(f"Person{num}", num * 10) for num in range(10)]
        for item in items:
            tree.add(item)
        self.assertEqual(tree.first(), items[0],
                         "First element should be Person0")
        self.assertEqual(tree.last(), items[-1],
                         "Last element should be Person9")

    def test_poll_first_last(self):
        tree = TreeSet(Person)
        items = [Person(f"Person{num}", num * 10) for num in range(10)]
        for item in items:
            tree.add(item)
        self.assertEqual(tree.poll_first(), items[0],
                         "Poll first should return Person0")
        self.assertEqual(tree.poll_last(), items[-1],
                         "Poll last should return Person9")


if __name__ == '__main__':
    unittest.main()
