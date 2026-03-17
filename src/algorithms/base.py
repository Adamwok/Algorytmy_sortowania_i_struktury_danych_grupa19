import time
from abc import ABC, abstractmethod

class BaseSort(ABC):
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.execution_time = 0.0
        self.custom_metrics = {}
    
    def reset_stats(self):
        self.comparisons = 0
        self.swaps = 0
        self.execution_time = 0.0
        self.custom_metrics = {}
    
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

    def run_sort(self, data: list) -> list:
        self.reset_stats()
        data_copy = data.copy()
        start_time = time.perf_counter()
        sorted_data = self.sort(data_copy)
        self.execution_time = time.perf_counter() - start_time
        return sorted_data
    