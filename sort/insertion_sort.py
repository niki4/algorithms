import random
import timeit

# Runtime complexity: O(1) best case [insert in sorted list], O(n**2) worst case
def insertion_sort(items):
    for idx in range(1, len(items)):  # considering items[0] already sorted
        current_value = items[idx]
        pos = idx
        while pos > 0 and items[pos-1] > current_value:
            items[pos] = items[pos-1]
            pos -= 1
        items[pos] = current_value

# Slightly sugared version of the version above. Adds extra overhead!
def insertion_sort2(items):
    for idx in range(1, len(items)):
        pos = idx
        while pos > 0 and items[pos-1] > items[idx]:
            pos -= 1
        items.insert(pos, items.pop(idx))


if __name__ == '__main__':
    to_sort1 = list(range(10))
    to_sort2 = list(range(10))

    random.shuffle(to_sort1)
    random.shuffle(to_sort2)

    t1 = timeit.Timer('insertion_sort(to_sort1)',
        'from __main__ import insertion_sort, to_sort1')
    t2 = timeit.Timer('insertion_sort2(to_sort2)',
        'from __main__ import insertion_sort2, to_sort2')

    print(t1.timeit())  # 1.942524097 --> winner :)
    print(t2.timeit())  # 3.983949237

    insertion_sort(to_sort1)
    insertion_sort2(to_sort2)
    assert to_sort1 == to_sort2 == list(range(10))
