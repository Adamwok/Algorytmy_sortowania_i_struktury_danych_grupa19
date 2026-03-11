import random

class DataGenerator:
    @staticmethod
    def generate_base(n):
        return [random.randint(1, 10*n) for _ in range(n)]
    
    @staticmethod
    def generate_random(n):
        return DataGenerator.generate_base(n)
    
    @staticmethod
    def generate_ascending(n):
        return sorted(DataGenerator.generate_base(n))
    
    @staticmethod
    def generate_descending(n):
        return sorted(DataGenerator.generate_base(), reverse=True)
    
    @staticmethod
    def generate_a_shaped(n):
        data = sorted(DataGenerator.generate_base(n), reverse=True)
        return data[0::2][::-1] + data[1::2]
    
    @staticmethod
    def generate_v_shaped(n):
        data = sorted(DataGenerator.generate_base(n))
        return data[0::2][::-1] + data[1::2]
    
    @staticmethod
    def generate_datasets(n, iterations=10):
        return {
            "random": [DataGenerator.generate_random(n) for _ in range(iterations)],
            "ascending": [DataGenerator.generate_ascending(n) for _ in range(iterations)],
            "descending": [DataGenerator.generate_descending(n) for _ in range(iterations)],
            "a_shaped": [DataGenerator.generate_a_shaped(n) for _ in range(iterations)],
            "v_shaped": [DataGenerator.generate_v_shaped(n) for _ in range(iterations)]
        }