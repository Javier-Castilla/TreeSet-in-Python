import unittest


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTest(loader.loadTestsFromName("tests.test_empty_tree_set"))
    suite.addTest(loader.loadTestsFromName("tests.test_many_items_tree_set"))
    suite.addTest(loader.loadTestsFromName("tests.test_other_items_tree_set"))
    suite.addTest(loader.loadTestsFromName("tests.test_simple_stack"))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

    # Uncomment the next lines and execute the program to see the GUI
    # app = GUI()
    # app.mainloop()
