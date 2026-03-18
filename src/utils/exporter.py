import csv
import os

class CSVExporter:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.initialize_file()
    
    def initialize_file(self):
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        with open(self.filepath, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Algorytm",
                "Rozmiar_N",
                "Uklad_Danych",
                "Iteracja",
                "Czy_Posortowano",
                "Czas_Sortowania",
                "Porownania",
                "Zamiany",
                "Wartości pośrednie"
            ])
    
    def append_result(self, algorithm: str, n: int, shape: str,iteration: int, is_sorted: bool, time_val: float, comp: int, swaps:int, custom: str):
        with open(self.filepath, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                algorithm,
                n,
                shape,
                iteration,
                is_sorted,
                f"{time_val:.6f}",
                comp,
                swaps,
                custom
            ])