from .base import BaseSort

class QuickSortIter(BaseSort):
    def sort(self, data: list) -> list:
        if not data:
            return data
        
        self.custom_metrics['pivots'] = []
        stack = [(0, len(data) - 1)]

        while stack:
            low, high = stack.pop()
            if low < high:
                pivot_index = self._partition(data, low, high)
                stack.append((low, pivot_index - 1))
                stack.append((pivot_index + 1, high))

        return data
    
    def _median_of_three(self, data: list, low: int, high: int):
        mid = (low + high) // 2

        self.comparisons += 1
        if data[mid] < data[low]:
            data[mid], data[low] = data[low], data[mid]
            self.swaps += 1
        
        self.comparisons += 1
        if data[high] < data[low]:
            data[high], data[low] = data[low], data[high]
            self.swaps += 1

        self.comparisons += 1
        if data[high] < data[mid]:
            data[high], data[mid] = data[mid], data[high]
            self.swaps += 1
        
        data[mid], data[high] = data[high], data[mid]
        self.swaps += 1

    
    def _partition(self, data: list, low: int, high: int) -> int:
        self._median_of_three(data, low, high)
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