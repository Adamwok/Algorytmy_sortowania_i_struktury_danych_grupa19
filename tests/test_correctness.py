import unittest
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from src.generators import DataGenerator
from src.algorithms import BubbleSort, HeapSort, MergeSort, QuickSortIter, QuickSortRec, ShellSort

class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.data_size = 100
        self.data = DataGenerator.generate_random(self.data_size)

    def test_bubble_sort(self):
        sorter = BubbleSort()
        self.assertEqual(sorter.run_sort(self.data.copy()), sorted(self.data))

    def test_heap_sort(self):
        sorter = HeapSort()
        self.assertEqual(sorter.run_sort(self.data.copy()), sorted(self.data))

    def test_merge_sort(self):
        sorter = MergeSort()
        self.assertEqual(sorter.run_sort(self.data.copy()), sorted(self.data))

    def test_quick_sort_iter(self):
        sorter = QuickSortIter()
        self.assertEqual(sorter.run_sort(self.data.copy()), sorted(self.data))

    def test_quick_sort_rec(self):
        sorter = QuickSortRec()
        self.assertEqual(sorter.run_sort(self.data.copy()), sorted(self.data))

    def test_shell_sort(self):
        sorter = ShellSort()
        self.assertEqual(sorter.run_sort(self.data.copy()), sorted(self.data))

if __name__ == '__main__':
    unittest.main()