import random


class Solution:
    # Runtime complexity: O(n log n) + O(k) because of slicing.
    # Extra memory for slicing and creating arrays.
    def quicksort(self, items):
        if items:
            pivot = items[0]
            below = [i for i in items[1:] if i < pivot]
            above = [j for j in items[1:] if j >= pivot]
            return self.quicksort(below) + [pivot] + self.quicksort(above)
        else:
            return items


class Solution2:
    # Using 'Hoare partition scheme' allows to do sort in place.
    # https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
    def quicksort(self, items):
        self._qsort(items, 0, len(items) - 1)
        return items

    def _qsort(self, items, low, high):
        if low < high:
            part = self._partition(items, low, high)
            self._qsort(items, low, part)
            self._qsort(items, part + 1, high)

    def _partition(self, items, low, high):
        pivot = items[(low + high) // 2]  # pick mid element as a pivot
        while True:
            while items[low] < pivot:  # move left mark
                low += 1
            while items[high] > pivot:  # move right mark
                high -= 1
            if low >= high:  # found split point
                return high
            items[low], items[high] = items[high], items[low]
            low += 1
            high -= 1


if __name__ == '__main__':
    solutions = [Solution(), Solution2()]
    for sol in solutions:
        to_sort = list(range(100))
        random.shuffle(to_sort)
        sorted_list = sol.quicksort(to_sort)

        assert sorted_list == list(range(100))
