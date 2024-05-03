import unittest


class User:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

class TestOtherItemsTreeSet(unittest.TestCase):
    def test_add(self):
        tree = TreeSet()


if __name__ == '__main__':
    unittest.main()
