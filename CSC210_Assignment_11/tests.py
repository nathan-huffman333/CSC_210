# tests.py
# Unit tests for bst.py and search_speed
import unittest
import random
from bst import BST
from main import search_speed


class TestBSTInt(unittest.TestCase):
    def test_bst_int(self):
        length = 11
        sample_int_array1 = [23, -3, -2, 4, 11, 4, 7, 8, 0, 0, -3]

        bst = BST()
        for value in sample_int_array1:
            bst.insert(value)

        # bst.getCount() == length
        self.assertEqual(len(bst), length)

        # min / max
        self.assertEqual(bst.minimum(), min(sample_int_array1))
        self.assertEqual(bst.maximum(), max(sample_int_array1))

        # contains
        for value in sample_int_array1:
            self.assertIn(value, bst)

        # inOrderWalk vs sorted array
        ordered = bst.in_order_walk()
        sample_sorted = sorted(sample_int_array1)

        # element-wise equality
        self.assertEqual(ordered, sample_sorted)


class TestBSTString(unittest.TestCase):
    def test_bst_string(self):
        length = 12
        sample_string_array1 = [
            "h", "a", "z", "j", "k", "b",
            "d", "r", "s", "l", "n", "m"
        ]

        bst = BST()
        for value in sample_string_array1:
            bst.insert(value)

        # getCount == length
        self.assertEqual(len(bst), length)

        # min / max
        self.assertEqual(bst.minimum(), min(sample_string_array1))
        self.assertEqual(bst.maximum(), max(sample_string_array1))

        # contains
        for value in sample_string_array1:
            self.assertIn(value, bst)

        # inOrderWalk vs sorted array
        ordered = bst.in_order_walk()
        sample_sorted = sorted(sample_string_array1)

        self.assertEqual(ordered, sample_sorted)


class TestBSTRandomInt(unittest.TestCase):
    def test_random_bst_int(self):
        length = 20
        # random ints in [0, length]
        sample_int_array1 = [random.randint(0, length) for _ in range(length)]

        bst = BST()
        for value in sample_int_array1:
            bst.insert(value)

        # getCount == length
        self.assertEqual(len(bst), length)

        # min / max
        self.assertEqual(bst.minimum(), min(sample_int_array1))
        self.assertEqual(bst.maximum(), max(sample_int_array1))

        # contains
        for value in sample_int_array1:
            self.assertIn(value, bst)

        # inOrderWalk vs sorted array
        ordered = bst.in_order_walk()
        sample_sorted = sorted(sample_int_array1)

        self.assertEqual(ordered, sample_sorted)


class TestBSTTiming(unittest.TestCase):
    def test_bst_timing(self):
        length = 2048
        bst_time, list_time = search_speed(length)

        # Both should be non-negative
        self.assertGreaterEqual(bst_time, 0)
        self.assertGreaterEqual(list_time, 0)

        # BST should be faster than list
        self.assertLess(bst_time, list_time)


if __name__ == "__main__":
    unittest.main()
