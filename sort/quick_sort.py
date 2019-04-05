import random
import timeit

# Runtime complexity: O(n log n) + O(k) because of slicing.
# Extra memory for slicing and creating arrays.
def qsort_simple(items):
    if items:
        pivot = items[0]
        below = [i for i in items[1:] if i < pivot]
        above = [j for j in items[1:] if j >= pivot]
        return qsort_simple(below) + [pivot] + qsort_simple(above)
    else:
        return items

# Using 'Hoare partition scheme' allows to do sort in place.
# https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
def qsort_hoare(items):
    def _qsort(items, low, high):
        if low < high:
            part = _partition(items, low, high)
            _qsort(items, low, part)
            _qsort(items, part + 1, high)
    
    def _partition(items, low, high):
        pivot = items[(low + high) // 2]
        while True:
            while items[low] < pivot:  # move left mark
                low += 1
            while items[high] > pivot: # move right mark
                high -= 1
            if low >= high:            # found split point
                return high
            items[low], items[high] = items[high], items[low]
            low += 1
            high -= 1
    
    _qsort(items, 0, len(items)-1)
    return items


if __name__ == '__main__':
    to_sort1 = list(range(10))
    to_sort2 = list(range(10))

    random.shuffle(to_sort1)
    random.shuffle(to_sort2)

    t1 = timeit.Timer('qsort_simple(to_sort1)', 
        'from __main__ import qsort_simple, to_sort1')
    t2 = timeit.Timer('qsort_hoare(to_sort2)',
        'from __main__ import qsort_hoare, to_sort2')

    print('qsort_simple rate:', t1.timeit())
    print('qsort_hoare rate: ', t2.timeit())
    
    sorted1 = qsort_simple(to_sort1)
    qsort_hoare(to_sort2)
    
    assert sorted1 == to_sort2 == list(range(10))
