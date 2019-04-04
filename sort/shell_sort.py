import random

# The Shell sort uses incremental sorting (of sub-arrays) 
# before the final insertion sort.

# Runtime complexity is between O(n) and O(n**2)
def shell_sort(items):
    increment = len(items) // 2

    while increment > 0:
        for start_pos in range(increment):
            gap_insertion_sort(items, start_pos, increment)
        print('After increments of size', increment,
            'array is', items)
        increment = increment // 2

def gap_insertion_sort(arr, start, gap):
    for i in range(start+gap, len(arr), gap):
        current_val = arr[i]
        pos = i

        while pos >= gap and arr[pos-gap] > current_val:
            arr[pos] = arr[pos-gap]
            pos = pos-gap
        
        arr[pos] = current_val


if __name__ == '__main__':
    to_sort = list(range(10))
    random.shuffle(to_sort)
    print('Before sorting\t\t\t   ', to_sort)

    shell_sort(to_sort)
    assert to_sort == list(range(10))
