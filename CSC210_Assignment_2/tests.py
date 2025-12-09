import unittest
from search import linear_search, binary_search
from experiment import time_trial, random_int_list

class TestSearchAlgorithms(unittest.TestCase):
    def test_linear_search_found(self):
        lst = [1, 2, 3, 4, 5]
        self.assertTrue(linear_search(lst, 3))
    
    def test_linear_search_not_found(self):
        lst = [1, 2, 3, 4, 5]
        self.assertFalse(linear_search(lst, 6))

    def test_linear_search_letters(self):
        lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.assertTrue(linear_search(lst, 'c'))
        self.assertFalse(linear_search(lst, 'z'))
    
    def test_binary_search_letters(self):
        lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        self.assertTrue(binary_search(lst, 'c'))
        self.assertFalse(binary_search(lst, 'z'))
    
    def test_binary_search_found(self):
        lst = [1, 2, 3, 4, 5]
        self.assertTrue(binary_search(lst, 4))
    
    def test_binary_search_not_found(self):
        lst = [1, 2, 3, 4, 5]
        self.assertFalse(binary_search(lst, 0))

    def test_binary_search_empty_list(self):
        lst = []
        self.assertFalse(binary_search(lst, 1))

    def test_time_trial(self):
        num_trials = 100
        data_size = 1000
        min_value = 1
        max_value = 1000
        linear_time, binary_time = time_trial(num_trials, data_size, min_value, max_value)
        print(f"Linear Search Time: {linear_time} ns, Binary Search Time: {binary_time} ns" )
        self.assertIsInstance(linear_time, float)
        self.assertIsInstance(binary_time, float)
        self.assertGreater(linear_time, 0)
        self.assertGreater(binary_time, 0)
        self.assertGreater(linear_time, binary_time)  # Binary search should be faster on average
    
    def test_random_int_list(self):
        length = 50
        min_value = 10
        max_value = 20
        lst = random_int_list(length, min_value, max_value)
        self.assertEqual(len(lst), length)
        for item in lst:
            self.assertGreaterEqual(item, min_value)
            self.assertLessEqual(item, max_value)

if __name__ == '__main__':
    unittest.main()