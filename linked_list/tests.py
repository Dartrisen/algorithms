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

    def test_set(self):
        self.mock.append(1)
        self.mock.append(2)
        self.mock.append(3)
        self.assertTrue(self.mock.set(0, 4))
        self.assertEqual(self.mock.get(0).value, 4)
        self.assertTrue(self.mock.set(1, 5))
        self.assertEqual(self.mock.get(1).value, 5)
        self.assertTrue(self.mock.set(2, 6))
        self.assertEqual(self.mock.get(2).value, 6)
        self.assertFalse(self.mock.set(3, 7))
        self.assertFalse(self.mock.set(-1, 8))

    def test_insert(self):
        """Test it."""
        self.assertTrue(self.mock.insert(0, 0))
        self.assertEqual(self.mock.get(0).value, 0)

    def test_insert_false(self):
        """Test it."""
        self.assertFalse(self.mock.insert(-1, -1))

    def test_remove(self):
        """Test it."""
        self.mock.append(1)
        self.mock.append(2)
        self.mock.append(3)
        self.assertEqual(self.mock.remove(0).value, 1)
        self.assertEqual(self.mock.length, 2)
        self.assertEqual(self.mock.remove(1).value, 3)

    def test_remove_invalid_index(self):
        """Test it."""
        self.assertIsNone(self.mock.remove(-1))
        self.assertIsNone(self.mock.remove(3))

    def test_reverse(self):
        """Test it."""
        self.mock.append(1)
        self.mock.append(2)
        self.mock.append(3)
        self.mock.reverse()
        self.assertEqual(self.mock.get(0).value, 3)
        self.assertEqual(self.mock.get(1).value, 2)
        self.assertEqual(self.mock.get(2).value, 1)


if __name__ == '__main__':
    unittest.main()
