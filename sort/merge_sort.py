import random

# The idea: 
# 1. split the array to subarrays (up to 1-len size each), 
# 2. then recursively merge subarrays back to single array, 
# 3. on each merge sort new subarrays

# Runtime complexity: O(n log n) + O(k) because of slicing
def merge_sort(items):
    print('splitting', items)
    if len(items) > 1:
        mid = len(items) // 2
        left_half = items[:mid]
        right_half = items[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                items[k] = left_half[i]
                i += 1
            else:
                items[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            items[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            items[k] = right_half[j]
            j += 1
            k += 1
    print('merging', items)


if __name__ == '__main__':
    to_sort = list(range(10))
    random.shuffle(to_sort)
    merge_sort(to_sort)
    assert to_sort == list(range(10))
