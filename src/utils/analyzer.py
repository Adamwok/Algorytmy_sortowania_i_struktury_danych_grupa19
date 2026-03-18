import csv
from collections import defaultdict
import os

class DataAnalyzer:
    def __init__(self, raw_csv_path: str):
        self.raw_path = raw_csv_path
        self.summary_path = raw_csv_path.replace("raw_data.csv", "summary_data.csv")

    def calculate_averages(self):
        if not os.path.exists(self.raw_path):
            raise FileNotFoundError(f"Brak pliku: {self.raw_path}")
        
        data = defaultdict(lambda: {'time': 0.0, 'count': 0})

        with open(self.raw_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = (row['Algorytm'], row['Rozmiar_N'], row['Uklad_Danych'])
                data[key]['time'] += float(row['Czas_Sortowania'])
                data[key]['count'] += 1
            
        with open(self.summary_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Algorytm', 'Rozmiar_N', 'Uklad_Danych', 'Sredni_Czas_Sortowania'])

            for (algo, n, shape), stats in data.items():
                avg_time = stats['time'] / stats['count']
                writer.writerow([algo, n, shape, f"{avg_time:.6f}"])