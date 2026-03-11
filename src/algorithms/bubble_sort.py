from .base import BaseSort

class BubbleSort(BaseSort):
    def sort(self, data: list) -> list:
        n = len(data)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                self.comparisons += 1
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    self.swaps += 1
                    swapped = True
            if not swapped:
                break
        return data