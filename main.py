import unittest
from TreeSet import *

def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromName("tests.test_empty_treeset"))
    suite.addTest(loader.loadTestsFromName("tests.test_many_items_treeset"))
    return suite

def is_odd(f):
    def wrapper(args):
        if args % 2 == 0:
            return f(args)
        else:
            return args

    return wrapper

@is_odd
def next_power(num):
    return num << 1


if __name__ == "__main__":
    """runner = unittest.TextTestRunner()
    runner.run(suite())"""
    t = TreeSet(int)
    print(t.__lt__)
