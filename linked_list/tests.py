import unittest
from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.mock = LinkedList(4)
        self.mock.make_empty()

    def test_append(self):
        """Test it."""
        self.mock.append(4)
        self.mock.append(6)
        self.assertEqual(self.mock.head.value, 4)
        self.assertEqual(self.mock.tail.value, 6)
        self.assertEqual(self.mock.length, 2)

    def test_append_empty(self):
        """Test it."""
        self.assertIsNone(self.mock.head)
        self.assertIsNone(self.mock.tail)
        self.assertEqual(self.mock.length, 0)

    def test_pop(self):
        """Test it."""
        self.mock.append(4)
        self.mock.append(6)
        self.mock.append(8)
        pop = self.mock.pop()
        self.assertEqual(pop.value, 8)
        self.assertEqual(self.mock.head.value, 4)
        self.assertEqual(self.mock.tail.value, 6)
        self.assertEqual(self.mock.length, 2)

    def test_pop_empty(self):
        """Test it."""
        self.assertIsNone(self.mock.pop())
        self.assertEqual(self.mock.length, 0)

    def test_prepend(self):
        """Test it."""
        self.mock.prepend(1)
        self.mock.prepend(2)
        self.assertEqual(self.mock.head.value, 2)
        self.assertEqual(self.mock.head.next.value, 1)
        self.assertEqual(self.mock.tail.value, 1)
        self.assertEqual(self.mock.length, 2)


if __name__ == '__main__':
    unittest.main()
