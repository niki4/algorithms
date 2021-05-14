"""
Quick Sort (QS) algorithm:
Following the divide-and-conquer algorithm, as we presented before, the quick sort algorithm can be implemented in three
steps, namely 1) dividing the problem, 2) solving the subproblems and 3) combining the results of subproblems.

In detail, given a list of values to sort, the quick sort algorithm works in the following steps:
1. First, it selects a value from the list, which serves as a pivot value to divide the list into two sublists.
   One sublist contains all the values that are less than the pivot value, while the other sublist contains the values
   that are greater than or equal to the pivot value. This process is also called partitioning. The strategy of choosing
   a pivot value can vary. Typically, one can choose the first element in the list as the pivot, or randomly pick an
   element from the list.
2. After the partitioning process, the original list is then reduced into two smaller sublists. We then recursively sort
   the two sublists.
3. After the partitioning process, we are sure that all elements in one sublist are less or equal than any element in
   another sublist. Therefore, we can simply concatenate the two sorted sublists that we obtain in step [2] to obtain
   the final sorted list.
"""

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
        items = items[:]
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


class Solution3(Solution2):
    """
    Sorts an array in the ascending order in O(N logN) time
    """

    def _qsort(self, items, low, high):
        if low < high:
            part = self._partition(items, low, high)
            self._qsort(items, low, part - 1)
            self._qsort(items, part + 1, high)

    def _partition(self, items, low, high):
        """
        Picks the last element hi as a pivot and returns the index of pivot value in the sorted array
        """
        pivot = items[high]
        i = low
        for j in range(low, high):
            if items[j] < pivot:  # place items below pivot from left side of it
                items[i], items[j] = items[j], items[i]
                i += 1
        # now when all items before i-th idx are less than pivot, we need to move pivot
        # so that from left side of it all values are less/equal pivot and from
        # right side all values are greater/equal than pivot.
        items[i], items[high] = items[high], items[i]
        return i


if __name__ == '__main__':
    solutions = [Solution(), Solution2(), Solution3()]
    for sol in solutions:
        to_sort = list(range(100))
        random.shuffle(to_sort)
        sorted_list = sol.quicksort(to_sort)

        assert sorted_list == list(range(100))
