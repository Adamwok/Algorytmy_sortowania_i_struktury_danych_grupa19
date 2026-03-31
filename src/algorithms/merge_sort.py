from .base import BaseSort

class MergeSort(BaseSort):
    def sort(self, data: list) -> list:
        self.custom_metrics['merges'] = 0
        self.merge_sort(data, 0, len(data) - 1)
        return data

    def merge_sort(self, data: list, left: int, right: int):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(data, left, mid)
            self.merge_sort(data, mid + 1, right)
            self.merge(data, left, mid, right)
        
    def merge(self, data: list, left: int, mid: int, right: int):
        self.custom_metrics['merges'] += 1

        left_part = data[left:mid + 1]
        right_part = data[mid + 1:right + 1]

        i = 0
        j = 0
        k = left

        while i < len(left_part) and j < len(right_part):
            self.comparisons += 1
            if left_part[i] <= right_part[j]:
                data[k] = left_part[i]
                i += 1
            else:
                data[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            data[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            data[k] = right_part[j]
            j += 1
            k += 1
            
        
