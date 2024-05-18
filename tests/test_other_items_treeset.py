import random
import unittest
from TreeSet import TreeSet
from tests.tests_classes import *
from treeset_exceptions import NonComparableObjectError


class TestOtherItemsTreeSet(unittest.TestCase):
    def test_tree_with_person(self):
        """
        Test the TreeSet with Person objects and Worker objects,
        that extends Person. Missing __gt__ comparator.
        """
        tree = TreeSet(Person)
        ids = {random.randint(10, 40) for _ in range(10)}
        ids = sorted(list(ids))
        items = [
            Person(f"Person{identifier}", identifier) if index % 2 == 0 else
            Worker(f"Worker{identifier}", identifier, f"job{identifier}")
            for index, identifier in enumerate(ids)
        ]

        for item in items:
            self.assertTrue(tree.add(item),
                            "Wrong value after inserting new element")

        self.assertEqual(tree.size(), len(ids), "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")

        for index in range(len(items) - 1):
            self.assertEqual(
                tree.higher(items[index]), items[index + 1],
                "Wrong higher value"
            )
            self.assertEqual(
                tree.lower(items[index + 1]), items[index],
                "Wrong lower value"
            )
            self.assertEqual(
                tree.ceiling(items[index]), items[index],
                "Wrong ceiling value"
            )
            self.assertEqual(
                tree.floor(items[index]), items[index],
                "Wrong floor value"
            )

        self.assertEqual(tree.last(), items[-1], "Wrong last value")

        self.assertEqual(
            [person for person in tree.iterator()], items,
            "Wrong iterator values"
        )
        self.assertEqual(
            [person for person in tree.descending_iterator()], items[::-1],
            "Wrong descending iterator values"
        )

        for person in items:
            self.assertTrue(
                tree.contains(person),
                "Tree must contain the element"
            )

        tree_clone = tree.clone()
        self.assertEqual(tree, tree_clone,
                         "Tree and clone must be equal")

        for index in range(len(items)):
            self.assertEqual(
                tree.poll_first(), items[index],
                "Wrong poll first value"
            )
            self.assertEqual(
                tree_clone.poll_last(), items[-(index + 1)],
                "Wrong poll last value"
            )

    def test_tree_with_professor(self):
        """
        Test the TreeSet with Professor objects. Missing __lt__ comparator.
        """
        tree = TreeSet(Professor)
        ids = {random.randint(10, 40) for _ in range(10)}
        ids = sorted(list(ids))
        items = [
            Professor(f"Professor{identifier}", f"subject{identifier}")
            for identifier in ids
        ]

        for item in items:
            self.assertTrue(tree.add(item),
                            "Wrong value after inserting new element")

        self.assertEqual(tree.size(), len(ids), "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")

        for index in range(len(items) - 1):
            self.assertEqual(
                tree.higher(items[index]), items[index + 1],
                "Wrong higher value"
            )
            self.assertEqual(
                tree.lower(items[index + 1]), items[index],
                "Wrong lower value"
            )
            self.assertEqual(
                tree.ceiling(items[index]), items[index],
                "Wrong ceiling value"
            )
            self.assertEqual(
                tree.floor(items[index]), items[index],
                "Wrong floor value"
            )

        self.assertEqual(tree.last(), items[-1], "Wrong last value")

        self.assertEqual(
            [professor for professor in tree.iterator()], items,
            "Wrong iterator values"
        )
        self.assertEqual(
            [professor for professor in tree.descending_iterator()], items[::-1],
            "Wrong descending iterator values"
        )

        for professor in items:
            self.assertTrue(
                tree.contains(professor),
                "Tree must contain the element"
            )

        tree_clone = tree.clone()
        self.assertEqual(tree, tree_clone,
                         "Tree and clone must be equal")

        for index in range(len(items)):
            self.assertEqual(
                tree.poll_first(), items[index],
                "Wrong poll first value"
            )
            self.assertEqual(
                tree_clone.poll_last(), items[-(index + 1)],
                "Wrong poll last value"
            )

    def test_tree_with_student(self):
        """
        Test the TreeSet with Student objects. Missing __eq__ comparator.
        """
        with self.assertRaises(NonComparableObjectError):
            TreeSet(Student)

if __name__ == '__main__':
    unittest.main()
