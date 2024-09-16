"""Implementation of the test class for the SimpleStack class."""
import unittest
from data_utils import SimpleStack


class TestSimpleStack(unittest.TestCase):
    """Test class for the SimpleStack class."""

    def setUp(self) -> None:
        """Set up the test class."""
        self.empty_stack = SimpleStack()
        self.one_stack = SimpleStack(1)
        self.many_stack = SimpleStack([num for num in range(10)])

    def test_empty_len(self):
        """Test the length of the stack."""
        self.assertEqual(len(self.empty_stack), 0, "Stack must be empty")

    def test_empty_push(self):
        """Test the push method of the stack."""
        self.empty_stack.push(1)
        self.assertEqual(len(self.empty_stack), 1,
                         "Stack must have one element")
        self.assertEqual(self.empty_stack.peek(), 1,
                         "Wrong element at the top of the stack")

    def test_empty_pull(self):
        """Test the pull method of the stack."""
        self.empty_stack.push(1)
        self.assertEqual(self.empty_stack.pull(), 1,
                         "Wrong element pulled")
        self.assertEqual(len(self.empty_stack), 0, "Stack must be empty")

    def test_empty_is_empty(self):
        """Test the is_empty method of the stack."""
        self.assertTrue(self.empty_stack.is_empty(), "Stack must be empty")
        self.empty_stack.push(1)
        self.assertFalse(self.empty_stack.is_empty(), "Stack must not be empty")

    def test_empty_iter(self):
        """Test the iterator of the stack."""
        self.assertEqual([], [item for item in self.empty_stack],
                         "Stack must be empty")

    def test_empty_str(self):
        """Test the string representation of the stack."""
        self.assertEqual(str(self.empty_stack), "SimpleStack([])",
                         "Wrong string representation of the stack")

    def test_one_len(self):
        """Test the length of the stack."""
        self.assertEqual(len(self.one_stack), 1, "Stack must have one element")

    def test_one_push(self):
        """Test the push method of the stack."""
        self.one_stack.push(2)
        self.assertEqual(len(self.one_stack), 2, "Stack must have two elements")
        self.assertEqual(self.one_stack.peek(), 2,
                         "Wrong element at the top of the stack")

    def test_one_pull(self):
        """Test the pull method of the stack."""
        self.assertEqual(self.one_stack.pull(), 1, "Wrong element pullped")
        self.assertEqual(len(self.one_stack), 0, "Stack must be empty")

    def test_one_is_empty(self):
        """Test the is_empty method of the stack."""
        self.assertFalse(self.one_stack.is_empty(), "Stack must not be empty")
        self.one_stack.pull()
        self.assertTrue(self.one_stack.is_empty(), "Stack must be empty")

    def test_one_iter(self):
        """Test the iterator of the stack."""
        self.assertEqual([1], [item for item in self.one_stack],
                         "Stack must have one element")

    def test_one_str(self):
        """Test the string representation of the stack."""
        self.assertEqual(str(self.one_stack), "SimpleStack([1])",
                         "Wrong string representation of the stack")

    def test_many_len(self):
        """Test the length of the stack."""
        self.assertEqual(len(self.many_stack), 10, "Stack must have 10 elements")

    def test_many_push(self):
        """Test the push method of the stack."""
        self.many_stack.push(10)
        self.assertEqual(len(self.many_stack), 11, "Stack must have 11 elements")
        self.assertEqual(self.many_stack.peek(), 10,
                         "Wrong element at the top of the stack")

    def test_many_pull(self):
        """Test the pull method of the stack."""
        self.assertEqual(self.many_stack.pull(), 9, "Wrong element pullped")
        self.assertEqual(len(self.many_stack), 9, "Stack must have 9 elements")

    def test_many_is_empty(self):
        """Test the is_empty method of the stack."""
        self.assertFalse(self.many_stack.is_empty(), "Stack must not be empty")

        for _ in range(10):
            self.many_stack.pull()

        self.assertTrue(self.many_stack.is_empty(), "Stack must be empty")

    def test_many_iter(self):
        """Test the iterator of the stack."""
        self.assertEqual(list(range(10))[::-1], [item for item in self.many_stack],
                         "Stack must have 10 elements")

    def test_many_str(self):
        """Test the string representation of the stack."""
        self.assertEqual(str(self.many_stack), "SimpleStack([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])",
                         "Wrong string representation of the stack")


if __name__ == '__main__':
    unittest.main()
