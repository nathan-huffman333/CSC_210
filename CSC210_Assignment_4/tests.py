import unittest
from random import randint
from simple_sorts import bubble_sort, selection_sort, insertion_sort
from time import perf_counter_ns

class TestSimpleSorts(unittest.TestCase):
    def test_bubble_sort_simple(self):
        lst = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(lst)
        self.assertEqual(lst, [11, 12, 22, 25, 34, 64, 90])

    def test_selection_sort_simple(self):
        lst = [64, 34, 25, 12, 22, 11, 90]
        selection_sort(lst)
        self.assertEqual(lst, [11, 12, 22, 25, 34, 64, 90])

    def test_insertion_sort_simple(self):
        lst = [64, 34, 25, 12, 22, 11, 90]
        insertion_sort(lst)
        self.assertEqual(lst, [11, 12, 22, 25, 34, 64, 90])

    def test_large_random_array_bubble_sort(self):
        lst = [randint(0, 10000) for _ in range(1000)]
        sorted_lst = sorted(lst)
        bubble_sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_large_random_array_selection_sort(self):
        lst = [randint(0, 10000) for _ in range(1000)]
        sorted_lst = sorted(lst)
        selection_sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_large_random_array_insertion_sort(self):
        lst = [randint(0, 10000) for _ in range(1000)]
        sorted_lst = sorted(lst)
        insertion_sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_bubble_sort_strings(self):
        lst = ["banana", "apple", "orange", "kiwi"]
        bubble_sort(lst)
        self.assertEqual(lst, ["apple", "banana", "kiwi", "orange"])

    def test_selection_sort_strings(self):
        lst = ["banana", "apple", "orange", "kiwi"]
        selection_sort(lst)
        self.assertEqual(lst, ["apple", "banana", "kiwi", "orange"])

    def test_insertion_sort_strings(self):
        lst = ["banana", "apple", "orange", "kiwi"]
        insertion_sort(lst)
        self.assertEqual(lst, ["apple", "banana", "kiwi", "orange"])

    def test_buble_sort_slower_than_selection_sort(self):
        lst1 = [randint(0, 10000) for _ in range(10000)]
        lst2 = lst1.copy()
        start_time = perf_counter_ns()
        bubble_sort(lst1)
        bubble_time = perf_counter_ns() - start_time
        start_time = perf_counter_ns()
        selection_sort(lst2)
        selection_time = perf_counter_ns() - start_time
        self.assertGreater(bubble_time, selection_time)
        self.assertEqual(lst1, lst2)

if __name__ == '__main__':
    unittest.main()