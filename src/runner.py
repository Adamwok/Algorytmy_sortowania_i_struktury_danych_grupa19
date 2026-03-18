from src.generators import DataGenerator
from src.algorithms import BubbleSort, HeapSort, MergeSort, QuickSortIter, QuickSortRec, ShellSort
from src.utils import CSVExporter

class BenchmarkRunner:
    def __init__(self, results_path: str, n_values: list[int], iterations: int):
        self.exporter = CSVExporter(results_path)
        self.n_values = n_values
        self.iterations = iterations
        self.algorithms = [
            ("BubbleSort", BubbleSort()),
            ("HeapSort", HeapSort()),
            ("MergeSort", MergeSort()),
            ("QuickSortIter", QuickSortIter()),
            ("QuickSortRec", QuickSortRec()),
            ("ShellSort", ShellSort()),
        ]

    def _format_sequence(self, data: list) -> str:
        if len(data) <= 100:
            return str(data)
        
        front = data[:50]
        back = data[-50:]
        
        front_str = ", ".join(map(str, front))
        back_str = ", ".join(map(str, back))
        
        return f"[{front_str}, ..., {back_str}]"

    def execute_all(self):
        for n in self.n_values:
            print(f"Generowanie ciągów i sortowanie dla n = {n}...")
            datasets = DataGenerator.generate_datasets(n, self.iterations)
            for algo_name, sorter in self.algorithms:
                for shape, arrays in datasets.items():
                    for i, data in enumerate(arrays, start=1):
                        input_str = self._format_sequence(data)
                        
                        sorted_data = sorter.run_sort(data.copy())
                        output_str = self._format_sequence(sorted_data)
                        
                        is_sorted = all(sorted_data[k] <= sorted_data[k+1] for k in range(len(sorted_data)-1))
                        custom_data_str = str(sorter.custom_metrics) if sorter.custom_metrics else "Brak"
                        
                        self.exporter.append_result(
                            algorithm=algo_name,
                            n=n,
                            shape=shape,
                            iteration=i,
                            input_seq=input_str,
                            output_seq=output_str,
                            is_sorted=is_sorted,
                            time_val=sorter.execution_time,
                            comp=sorter.comparisons,
                            swaps=sorter.swaps,
                            custom=custom_data_str
                        )