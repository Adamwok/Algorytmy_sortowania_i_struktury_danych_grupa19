import random
from .base import BaseSort

class QuickSortRec(BaseSort):
    def sort(self, data: list) -> list:
        self.custom_metrics['pivots'] = []
        self.quick_sort(data, 0, len(data) - 1)
        return data
    
    def quick_sort(self, data: list, low: int, high: int):
        if low < high:
            pivot_index = self.partition(data, low, high)
            self.quick_sort(data, low, pivot_index - 1)
            self.quick_sort(data, pivot_index + 1, high)
    
    def partition(self, data: list, low: int, high: int) -> int:
        rand_idx = random.randint(low, high)
        data[high], data[rand_idx] = data[rand_idx], data[high]
        self.swaps += 1

        pivot = data[high]
        self.custom_metrics['pivots'].append(pivot) 

        i = low - 1
        for j in range(low, high):
            self.comparisons += 1
            if data[j] <= pivot:
                i += 1
                data[i], data[j] = data[j], data[i]
                self.swaps += 1

        data[i + 1], data[high] = data[high], data[i + 1]
        self.swaps += 1
        return i + 1
    