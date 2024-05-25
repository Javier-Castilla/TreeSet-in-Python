"""Implementation of the test class for a TreeSet with items different from
int, float and str module."""
import random
import unittest
from tree_set import TreeSet
from tests.tests_classes import *
from tree_set_exceptions import ClassCastException


class TestOtherItemsTreeSet(unittest.TestCase):
    """Test the TreeSet with other items."""

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

        tree.clear()
        tree.add_all(items)

        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after clear and using add_all"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after clear and using add_all"
        )

        tree = TreeSet(Person, items)
        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after using constructor with collection"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after using constructor with collection"
        )

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

        tree.clear()
        tree.add_all(items)

        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after clear and using add_all"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after clear and using add_all"
        )

        tree = TreeSet(Professor, items)
        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after using constructor with collection"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after using constructor with collection"
        )

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
            [professor for professor in tree.descending_iterator()],
            items[::-1],
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
        tree = TreeSet(Student)
        with self.assertRaises(ClassCastException):
            tree.add(Student("Student1", 1))

    def test_tree_with_lazy_worker(self):
        """
        Test the TreeSet with LazyWorker objects. Comparators are lazy, they
        just do not do anything.
        """
        tree = TreeSet(LazyWorker)
        with self.assertRaises(ClassCastException):
            tree.add(LazyWorker("LazyWorker1", 1, "job1", 1))

    def test_tree_with_alien(self):
        """Test the TreeSet with Alien objects. Missing __le__ comparator."""
        tree = TreeSet(Alien)
        ids = {random.randint(10, 40) for _ in range(10)}
        ids = sorted(list(ids))
        items = [
            Martian(f"Martian{identifier}", identifier, "Green") if index % 2 == 0 else
            Venusian(f"Venusian{identifier}", identifier, identifier * 10)
            for index, identifier in enumerate(ids)
        ]

        for item in items:
            self.assertTrue(tree.add(item),
                            "Wrong value after inserting new element")

        self.assertEqual(tree.size(), len(ids), "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")

        tree.clear()
        tree.add_all(items)

        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after clear and using add_all"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after clear and using add_all"
        )

        tree = TreeSet(Alien, items)
        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after using constructor with collection"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after using constructor with collection"
        )

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

    def test_tree_with_list(self):
        """
        Test the TreeSet with list objects.
        """
        tree = TreeSet(list)
        items = [
            [random.randint(10, 40) for _ in range(4)] for _ in range(10)
        ]

        sorted_items = sorted(items)

        for item in items:
            self.assertTrue(tree.add(item),
                            "Wrong value after inserting new element")

        self.assertEqual(tree.size(), len(items), "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")

        tree.clear()
        tree.add_all(items)

        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after clear and using add_all"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after clear and using add_all"
        )

        tree = TreeSet(list, items)
        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after using constructor with collection"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after using constructor with collection"
        )

        for index in range(len(items) - 1):
            self.assertEqual(
                tree.higher(sorted_items[index]), sorted_items[index + 1],
                "Wrong higher value"
            )
            self.assertEqual(
                tree.lower(sorted_items[index + 1]), sorted_items[index],
                "Wrong lower value"
            )
            self.assertEqual(
                tree.ceiling(sorted_items[index]), sorted_items[index],
                "Wrong ceiling value"
            )
            self.assertEqual(
                tree.floor(sorted_items[index]), sorted_items[index],
                "Wrong floor value"
            )

        self.assertEqual(tree.last(), sorted_items[-1], "Wrong last value")

        self.assertEqual(
            [item for item in tree.iterator()], sorted_items,
            "Wrong iterator values"
        )
        self.assertEqual(
            [item for item in tree.descending_iterator()], sorted_items[::-1],
            "Wrong descending iterator values"
        )

        for item in items:
            self.assertTrue(
                tree.contains(item),
                "Tree must contain the element"
            )

        tree_clone = tree.clone()
        self.assertEqual(tree, tree_clone,
                         "Tree and clone must be equal")

        for index in range(len(sorted_items)):
            (changed_item := sorted_items[index]).pop()
            self.assertEqual(item := tree.floor(changed_item), changed_item,
                             "Wrong floor value")
            self.assertEqual(item, tree_clone.floor(changed_item),
                             "Wrong floor value")

        for index in range(len(sorted_items)):
            self.assertEqual(
                tree.poll_first(), sorted_items[index],
                "Wrong poll first value"
            )
            self.assertEqual(
                tree_clone.poll_last(), sorted_items[-(index + 1)],
                "Wrong poll last value"
            )

    def test_tree_with_set(self):
        """
        Test the TreeSet with set objects. Note that the operators '<' and '>'
        are not defined for sets, instead it checks subset relation.
        """
        tree = TreeSet(set)
        items = []
        s = set()
        old_len = 0
        for _ in range(10):
            while len(s) == old_len:
                s.add(random.randint(0, 40))

            old_len = len(s)
            items.append(set(s))

        del s

        for item in items:
            self.assertTrue(tree.add(item),
                            "Wrong value after inserting new element")

        self.assertEqual(tree.size(), len(items), "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")

        tree.clear()

        tree.add_all(items)
        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after clear and using add_all"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after clear and using add_all"
        )

        tree = TreeSet(set, items)
        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after using constructor with collection"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after using constructor with collection"
        )

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
            [item for item in tree.iterator()], items,
            "Wrong iterator values"
        )
        self.assertEqual(
            [item for item in tree.descending_iterator()], items[::-1],
            "Wrong descending iterator values"
        )

        for item in items:
            self.assertTrue(
                tree.contains(item),
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

    def test_tree_with_tuple(self):
        """Test the TreeSet with tuple objects."""
        tree = TreeSet(tuple)
        items = [
            tuple(random.randint(10, 40) for _ in range(4)) for _ in range(10)
        ]

        sorted_items = sorted(items)

        for item in items:
            self.assertTrue(tree.add(item),
                            "Wrong value after inserting new element")

        self.assertEqual(tree.size(), len(items), "Wrong tree size")
        self.assertFalse(tree.is_empty(), "Tree must not be empty")

        tree.clear()
        tree.add_all(items)

        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after clear and using add_all"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after clear and using add_all"
        )

        tree = TreeSet(tuple, items)
        self.assertEqual(
            tree.size(), len(items),
            "Wrong tree size after using constructor with collection"
        )
        self.assertFalse(
            tree.is_empty(),
            "Tree must not be empty after using constructor with collection"
        )

        for index in range(len(items) - 1):
            self.assertEqual(
                tree.higher(sorted_items[index]), sorted_items[index + 1],
                "Wrong higher value"
            )
            self.assertEqual(
                tree.lower(sorted_items[index + 1]), sorted_items[index],
                "Wrong lower value"
            )
            self.assertEqual(
                tree.ceiling(sorted_items[index]), sorted_items[index],
                "Wrong ceiling value"
            )
            self.assertEqual(
                tree.floor(sorted_items[index]), sorted_items[index],
                "Wrong floor value"
            )

        self.assertEqual(tree.last(), sorted_items[-1], "Wrong last value")

        self.assertEqual(
            [item for item in tree.iterator()], sorted_items,
            "Wrong iterator values"
        )
        self.assertEqual(
            [item for item in tree.descending_iterator()], sorted_items[::-1],
            "Wrong descending iterator values"
        )

        for item in items:
            self.assertTrue(
                tree.contains(item),
                "Tree must contain the element"
            )

        tree_clone = tree.clone()
        self.assertEqual(tree, tree_clone,
                         "Tree and clone must be equal")

        for index in range(len(sorted_items)):
            self.assertEqual(
                tree.poll_first(), sorted_items[index],
                "Wrong poll first value"
            )
            self.assertEqual(
                tree_clone.poll_last(), sorted_items[-(index + 1)],
                "Wrong poll last value"
            )

    def test_tree_with_dictionary(self):
        """Test the TreeSet with dictionary objects."""
        tree = TreeSet(dict)
        with self.assertRaises(ClassCastException):
            tree.add({1: 1, 2: 2})


if __name__ == '__main__':
    unittest.main()
