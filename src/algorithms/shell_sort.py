from .base import BaseSort

class ShellSort(BaseSort):
    def sort(self, data: list) -> list:
        n = len(data)
        self.custom_metrics['gaps'] = []

        gaps = [1]
        k = 1
        while True:
            gap = (2 ** k) + 1
            if gap >= n:
                break
            gaps.append(gap)
            k += 1
        gaps.reverse()

        for gap in gaps:
            self.custom_metrics['gaps'].append(gap)

            for offset in range(gap):
                sublist_len = len(range(offset, n, gap))

                for i in range(sublist_len):
                    swapped = False

                    for j in range(0, sublist_len - i - 1):
                        idx1 = offset + j * gap
                        idx2 = offset + (j + 1) * gap

                        self.comparisons += 1
                        if data[idx1] > data[idx2]:
                            data[idx1], data[idx2] = data[idx2], data[idx1]
                            self.swaps += 1
                            swapped = True
                    
                    if not swapped:
                        break
        return data