import random

# Note. Algorithm doesn't work well in case of duplicated values in list
def selection_sort(items):
    for i in range(len(items)-1, 0, -1):
        max_idx = items.index(max(items[0:i+1]))
        items[max_idx], items[i] = items[i], items[max_idx]


if __name__ == '__main__':
    to_sort = [x for x in range(10)]
    random.shuffle(to_sort)
    selection_sort(to_sort)
    assert to_sort == list(range(10))
