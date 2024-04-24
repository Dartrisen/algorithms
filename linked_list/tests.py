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
        self.assertIsNone(self.mock.head)
        self.assertIsNone(self.mock.tail)
        self.assertEqual(self.mock.length, 0)

    def test_pop_first(self):
        """Test it."""
        self.mock.append(4)
        self.mock.append(6)
        self.mock.append(8)
        self.assertEqual(self.mock.pop_first().value, 4)
        self.assertEqual(self.mock.length, 2)
        self.assertEqual(self.mock.head.value, 6)

    def test_pop_first_empty(self):
        """Test it."""
        self.assertIsNone(self.mock.pop_first())
        self.assertIsNone(self.mock.head)
        self.assertIsNone(self.mock.tail)
        self.assertEqual(self.mock.length, 0)

    def test_prepend(self):
        """Test it."""
        self.mock.prepend(1)
        self.mock.prepend(2)
        self.assertEqual(self.mock.head.value, 2)
        self.assertEqual(self.mock.head.next.value, 1)
        self.assertEqual(self.mock.tail.value, 1)
        self.assertEqual(self.mock.length, 2)

    def test_get(self):
        self.mock.append(1)
        self.mock.append(2)
        self.mock.append(3)
        self.assertEqual(self.mock.get(0).value, 1)
        self.assertEqual(self.mock.get(1).value, 2)
        self.assertEqual(self.mock.get(2).value, 3)

    def test_get_empty(self):
        self.assertIsNone(self.mock.get(3))
        self.assertIsNone(self.mock.get(-1))

    def test_insert(self):
        self.assertRaises(NotImplementedError)


if __name__ == '__main__':
    unittest.main()
