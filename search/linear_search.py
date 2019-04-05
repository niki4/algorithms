# Runtime complexity: O(n)
def search_index(items, value):
    for idx in range(0, len(items)):
        if items[idx] == value:
            return idx
    else:
        return -1  # no such value in sequence

if __name__ == '__main__':
    src = 'Hello, world'
    assert search_index(src, 'w') == 7
    assert search_index(src, 'x') == -1
