import unittest
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from src.generators import DataGenerator
from src.algorithms import BubbleSort

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.data_size = 100
        self.data = DataGenerator.generate_random(self.data_size)

    def test_bubble_sort(self):
        sorter = BubbleSort()
        expected = sorted(self.data)
        result = sorter.run_sort(self.data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
