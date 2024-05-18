"""Implementation test class for the SimpleQueue class."""
import unittest
from data_utils import SimpleQueue


class TestSimpleQueue(unittest.TestCase):
    """Implements tests for the SimpleQueue class."""
    def setUp(self) -> None:
        """Creates the SimpleQueue instances for the tests."""
        self.empty_queue = SimpleQueue()
        self.one_queue = SimpleQueue(1)
        self.many_queue = SimpleQueue([num for num in range(10)])

    def test_empty_len(self):
        """Tests the length of the empty queue."""
        self.assertEqual(len(self.empty_queue), 0, "Queue must be empty")

    def test_empty_enqueue(self):
        """Tests the enqueue method with an empty queue."""
        self.empty_queue.enqueue(1)
        self.assertEqual(len(self.empty_queue), 1,
                         "Queue must have one element")
        self.assertEqual(self.empty_queue.peek(), 1,
                         "Wrong element at the top of the queue")

    def test_empty_dequeue(self):
        """Tests the dequeue method with an empty queue."""
        self.empty_queue.enqueue(1)
        self.assertEqual(self.empty_queue.dequeue(), 1,
                         "Wrong element dequeued")
        self.assertEqual(len(self.empty_queue), 0, "Queue must be empty")

    def test_empty_is_empty(self):
        """Tests the is_empty method with an empty queue."""
        self.assertTrue(self.empty_queue.is_empty(), "Queue must be empty")
        self.empty_queue.enqueue(1)
        self.assertFalse(self.empty_queue.is_empty(), "Queue must not be empty")

    def test_empty_iter(self):
        """Tests the iterator of the empty queue."""
        self.assertEqual([], [item for item in self.empty_queue],
                         "Queue must be empty")

    def test_empty_str(self):
        """Tests the string representation of the empty queue."""
        self.assertEqual(str(self.empty_queue), "SimpleQueue([])",
                         "Wrong string representation of the queue")

    def test_one_len(self):
        """Tests the length of the queue with one element."""
        self.assertEqual(len(self.one_queue), 1, "Queue must have one element")

    def test_one_enqueue(self):
        """Tests the enqueue method with a queue with one element."""
        self.one_queue.enqueue(2)
        self.assertEqual(len(self.one_queue), 2, "Queue must have two elements")
        self.assertEqual(self.one_queue.peek(), 1,
                         "Wrong element at the top of the queue")

    def test_one_dequeue(self):
        """Tests the dequeue method with a queue with one element."""
        self.assertEqual(self.one_queue.dequeue(), 1, "Wrong element dequeued")
        self.assertEqual(len(self.one_queue), 0, "Queue must be empty")

    def test_one_is_empty(self):
        """Tests the is_empty method with a queue with one element."""
        self.assertFalse(self.one_queue.is_empty(), "Queue must not be empty")
        self.one_queue.dequeue()
        self.assertTrue(self.one_queue.is_empty(), "Queue must be empty")

    def test_one_iter(self):
        """Tests the iterator of the queue with one element."""
        self.assertEqual([1], [item for item in self.one_queue],
                         "Queue must have one element")

    def test_one_str(self):
        """Tests the string representation of the queue with one element."""
        self.assertEqual(str(self.one_queue), "SimpleQueue([1])",
                         "Wrong string representation of the queue")

    def test_many_len(self):
        """Tests the length of the queue with many elements."""
        self.assertEqual(len(self.many_queue), 10,
                         "Queue must have 10 elements")

    def test_many_enqueue(self):
        """Tests the enqueue method with a queue with many elements."""
        self.many_queue.enqueue(10)
        self.assertEqual(len(self.many_queue), 11,
                         "Queue must have 11 elements")
        self.assertEqual(self.many_queue.peek(), 0,
                         "Wrong element at the top of the queue")

    def test_many_dequeue(self):
        """Tests the dequeue method with a queue with many elements."""
        self.assertEqual(self.many_queue.dequeue(), 0, "Wrong element dequeued")
        self.assertEqual(len(self.many_queue), 9, "Queue must have 9 elements")

    def test_many_is_empty(self):
        """Tests the is_empty method with a queue with many elements."""
        self.assertFalse(self.many_queue.is_empty(), "Queue must not be empty")

        for _ in range(10):
            self.many_queue.dequeue()

        self.assertTrue(self.many_queue.is_empty(), "Queue must be empty")

    def test_many_iter(self):
        """Tests the iterator of the queue with many elements."""
        self.assertEqual([num for num in range(10)],
                         [item for item in self.many_queue],
                         "Queue must have 10 elements")

    def test_many_str(self):
        """Tests the string representation of the queue with many elements."""
        self.assertEqual(str(self.many_queue),
                         "SimpleQueue([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])",
                         "Wrong string representation of the queue")


if __name__ == '__main__':
    unittest.main()
