# tests.py
# Unit tests to make sure your code works correctly
# Starter Code from CSC 210

import unittest
from city_reader import read_city_from_csv

class AllentownCase(unittest.TestCase):
    def setUp(self):
        self.city_data = read_city_from_csv('pop.csv', 'Allentown')
        return super().setUp()
    
    def test_name(self):
        self.assertEqual(self.city_data.name, 'Allentown')

    def test_start_year(self):
        self.assertEqual(self.city_data.start_year, 1991)

    def test_end_year(self):
        self.assertEqual(self.city_data.end_year, 2024)

    def test_1998_population(self):
        self.assertEqual(self.city_data[1998], 105402)

    def test_2004_population(self):
        self.assertEqual(self.city_data[2004], 106529)

    def test_max_population(self):
        self.assertEqual(self.city_data.max_year, 2024)

    def test_min_population(self):
        self.assertEqual(self.city_data.min_year, 1991)

    def test_growth_1991_2024(self):
        self.assertEqual(self.city_data.population_growth(1991, 2024),26978)

class ReadingCase(unittest.TestCase):
    def setUp(self):
        self.city_data = read_city_from_csv('pop.csv', 'Reading')
        return super().setUp()
    
    def test_name(self):
        self.assertEqual(self.city_data.name, 'Reading')

    def test_start_year(self):
        self.assertEqual(self.city_data.start_year, 1991)

    def test_end_year(self):
        self.assertEqual(self.city_data.end_year, 2024)

    def test_1998_population(self):
        self.assertEqual(self.city_data[1998], 79900)

    def test_2004_population(self):
        self.assertEqual(self.city_data[2004], 80400)

    def test_max_population(self):
        self.assertEqual(self.city_data.max_year, 2024)

    def test_min_population(self):
        self.assertEqual(self.city_data.min_year, 1992)

    def test_growth_1991_2024(self):
        self.assertEqual(self.city_data.population_growth(1991, 2024), 17895)

if __name__ == '__main__':
    unittest.main()