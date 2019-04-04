import random

# Runtime complexity: O(n**2)
# Note. Uncomment prints to visualize the algorithm
def bubble_search(items):
    for i in range(len(items)-1, 0, -1):
        # print('')
        for j in range(i):
            # print(j, end='.')
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]

if __name__ == '__main__':
    src = [random.randint(1, 20) for _ in range(20)]
    bubble_search(src)
    print(src)
