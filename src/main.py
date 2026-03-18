import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from src.runner import BenchmarkRunner
from src.utils import DataAnalyzer

def main():
    results_path = os.path.join(base_dir, 'results', 'raw_data.csv')
    n_values = [100, 200, 300, 400, 500, 1000, 2000, 3000, 4000, 5000]
    iterations = 10

    runner = BenchmarkRunner(results_path, n_values, iterations)
    runner.execute_all()

    analyzer = DataAnalyzer(results_path)
    analyzer.calculate_averages()

if __name__ == "__main__":
    main()