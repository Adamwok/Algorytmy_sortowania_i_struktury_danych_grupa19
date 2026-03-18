from .base import BaseSort

class HeapSort(BaseSort):
    def _heapify(self, data: list, n: int, i: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.comparisons += 1
            if data[left] > data[largest]:
                largest = left
        
        if right < n:
            self.comparisons += 1
            if data[right] > data[largest]:
                largest = right
        
        if largest != i:
            data[i], data[largest] = data[largest], data[i]
            self.swaps += 1
            self._heapify(data, n, largest)
    
    def sort(self, data: list) -> list:
        n = len(data)

        for i in range(n // 2 - 1, -1, -1):
            self._heapify(data, n, i)

        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            self.swaps += 1
            self._heapify(data, i, 0)
        
        return data