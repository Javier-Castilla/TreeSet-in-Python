import unittest

def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromName("tests.test_empty_treeset"))
    suite.addTest(loader.loadTestsFromName("tests.test_many_items_treeset"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())