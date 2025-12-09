# tests.py
# Unit tests for PriorityQueue using Python's unittest framework
import unittest
from random import randint
from pq import PriorityQueue
from main import sort_speed


class TestPriorityQueueInt(unittest.TestCase):
    def test_priority_queue_int_fixed(self):
        sample_int_array = [23, -3, -2, 4, 11, 4, 7, 8, 0, 0, -3]
        length = len(sample_int_array)

        pq = PriorityQueue()

        for x in sample_int_array:
            pq.push(x)

        # pq.getCount() == length
        self.assertEqual(len(pq), length)

        # pq.peek() == max_element(sample_int_array)
        self.assertEqual(pq.peek(), max(sample_int_array))

        # sort in descending order
        expected = sorted(sample_int_array, reverse=True)

        # popped contents of pq should match sorted contents
        for expected_value in expected:
            popped = pq.pop()
            self.assertEqual(expected_value, popped)


class TestPriorityQueueString(unittest.TestCase):
    def test_priority_queue_string_fixed(self):
        sample_string_array = [
            "h", "a", "z", "j", "k", "b",
            "d", "r", "s", "l", "n", "m"
        ]
        length = len(sample_string_array)

        pq = PriorityQueue()

        for s in sample_string_array:
            pq.push(s)

        # pq.getCount() == length
        self.assertEqual(len(pq), length)

        # pq.peek() == max_element(sample_string_array)
        self.assertEqual(pq.peek(), max(sample_string_array))

        # sort in descending (reverse lexicographic) order
        expected = sorted(sample_string_array, reverse=True)

        # popped contents of pq should match sorted contents
        for expected_value in expected:
            popped = pq.pop()
            self.assertEqual(expected_value, popped)


class TestRandomPriorityQueueInt(unittest.TestCase):
    def test_priority_queue_int_random(self):
        length = 20
        sample_int_array = [randint(0, length) for _ in range(length)]

        pq = PriorityQueue()
        for value in sample_int_array:
            pq.push(value)

        # pq.getCount() == length
        self.assertEqual(len(pq), length)

        # pq.peek() == max_element(sample_int_array)
        self.assertEqual(pq.peek(), max(sample_int_array))

        # sort in descending order
        expected = sorted(sample_int_array, reverse=True)

        # popped contents of pq should match sorted contents
        for expected_value in expected:
            popped = pq.pop()
            self.assertEqual(expected_value, popped)


class TestPriorityQueueTiming(unittest.TestCase):
    def test_priority_queue_timing(self):
        # Here we assert that heap-based sort (pq) is faster than insertion sort
        length = 2048
        pq_time, is_time, builtin_time = sort_speed(length)

        # heap-based sort should beat insertion sort for sufficiently large n
        self.assertLess(pq_time, is_time)


if __name__ == "__main__":
    unittest.main()
