import unittest
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from src.generators import DataGenerator
from src.algorithms import BubbleSort
from src.algorithms import HeapSort
from src.algorithms import MergeSort
from src.algorithms import QuickSortIter
from src.algorithms import QuickSortRec
from src.algorithms import ShellSort

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.data_size = 100
        self.data = DataGenerator.generate_random(self.data_size)

    def test_bubble_sort(self):
        sorter = BubbleSort()
        expected = sorted(self.data)
        result = sorter.run_sort(self.data)
        self.assertEqual(result, expected)
    
    def test_heap_sort(self):
        sorter = HeapSort()
        expected = sorted(self.data)
        result = sorter.run_sort(self.data)
        self.assertEqual(result, expected)
    
    def test_merge_sort(self):
        sorter = MergeSort()
        expected = sorted(self.data)
        result = sorter.run_sort(self.data)
        self.assertEqual(result, expected)
    
    def test_quick_sort_iter(self):
        sorter = QuickSortIter()
        expected = sorted(self.data)
        result = sorter.run_sort(self.data)
        self.assertEqual(result, expected)
    
    def test_quick_sort_rec(self):
        sorter = QuickSortRec()
        expected = sorted(self.data)
        result = sorter.run_sort(self.data)
        self.assertEqual(result, expected)
    
    def test_shell_sort(self):
        sorter = ShellSort()
        expected = sorted(self.data)
        result = sorter.run_sort(self.data)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
