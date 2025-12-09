import unittest
from dynamic_array import DynamicArray
from linked_list import LinkedList

class TestDynamicArray(unittest.TestCase):

    def test_initialization(self):
        da = DynamicArray()
        self.assertEqual(len(da), 0)
        self.assertRaises(IndexError, lambda: da[0])

    def test_append_and_len(self):
        da = DynamicArray()
        for i in range(15):
            da.append(i)
            self.assertEqual(len(da), i + 1)
            self.assertEqual(da[i], i)

    def test_getitem_setitem(self):
        da = DynamicArray([1, 2, 3])
        self.assertEqual(da[0], 1)
        self.assertEqual(da[1], 2)
        self.assertEqual(da[2], 3)
        da[1] = 20
        self.assertEqual(da[1], 20)
        self.assertRaises(IndexError, lambda: da[3])
        self.assertRaises(IndexError, lambda: da[-4])

    def test_delitem(self):
        da = DynamicArray([1, 2, 3, 4])
        del da[1]
        self.assertEqual(len(da), 3)
        self.assertEqual(da[0], 1)
        self.assertEqual(da[1], 3)
        self.assertEqual(da[2], 4)
        del da[0]
        self.assertEqual(len(da), 2)
        self.assertEqual(da[0], 3)
        self.assertEqual(da[1], 4)
        del da[1]
        self.assertEqual(len(da), 1)
        self.assertEqual(da[0], 3)
        self.assertRaises(IndexError, lambda: print(da[1]))

    def test_insert(self):
        da = DynamicArray([1, 2, 3])
        da.insert(1, 10)
        self.assertEqual(len(da), 4)
        self.assertEqual(da[0], 1)
        self.assertEqual(da[1], 10)
        self.assertEqual(da[2], 2)
        self.assertEqual(da[3], 3)
        da.insert(0, 0)
        self.assertEqual(len(da), 5)
        self.assertEqual(da[0], 0)
        self.assertEqual(da[1], 1)
        da.insert(5, 20)

    def test_search(self):
        da = DynamicArray([1, 2, 3, 4, 5])
        self.assertIn(3, da)
        self.assertNotIn(6, da)

class TestLinkedList(unittest.TestCase):

    def test_initialization(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)
        self.assertRaises(IndexError, lambda: ll[0])

    def test_append_and_len(self):
        ll = LinkedList()
        for i in range(10):
            ll.append(i)
            self.assertEqual(len(ll), i + 1)
            self.assertEqual(ll[i], i)

    def test_getitem_setitem(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(ll[0], 1)
        self.assertEqual(ll[1], 2)
        self.assertEqual(ll[2], 3)
        ll[1] = 20
        self.assertEqual(ll[1], 20)
        self.assertRaises(IndexError, lambda: ll[3])
        self.assertRaises(IndexError, lambda: ll[-4])

    def test_delitem(self):
        ll = LinkedList([1, 2, 3, 4])
        del ll[1]
        self.assertEqual(len(ll), 3)
        self.assertEqual(ll[0], 1)
        self.assertEqual(ll[1], 3)
        self.assertEqual(ll[2], 4)
        del ll[0]
        self.assertEqual(len(ll), 2)
        self.assertEqual(ll[0], 3)
        self.assertEqual(ll[1], 4)
        del ll[1]
        self.assertEqual(len(ll), 1)
        self.assertEqual(ll[0], 3)
        self.assertRaises(IndexError, lambda: print(ll[1]))

    def test_insert(self):
        ll = LinkedList([1, 2, 3])
        ll.insert(1, 10)
        self.assertEqual(len(ll), 4)
        self.assertEqual(ll[0], 1)
        self.assertEqual(ll[1], 10)
        self.assertEqual(ll[2], 2)
        self.assertEqual(ll[3], 3)
        ll.insert(0, 0)
        self.assertEqual(len(ll), 5)
        self.assertEqual(ll[0], 0)
        self.assertEqual(ll[1], 1)
        ll.insert(5, 20)

    def test_search(self):
        ll = LinkedList([1, 2, 3, 4, 5])
        self.assertIn(3, ll)
        self.assertNotIn(6, ll)

if __name__ == '__main__':
    unittest.main()