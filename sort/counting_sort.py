"""
Counting Sort is kind of algorithm that works only to integers.

The idea is to pre-allocate array of arrays with the len of source list, 
then traverse unsorted list putting each num at correct place (index) using some key function (`j % len(src)-1` in my case),
finally traverse that array of arrays items in order and return them.

Given n keys are integers (fitting in a word) ∈ 0, 1, . . . , k − 1
Linear-time Sorting; Time and Space complexity both are Θ(n + k)

Implementation adopted from MIT 6.006 course. Here is more explanation about it
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec07.pdf
"""

def count_sort(src):
    L = [[] for _ in range(len(src))]  # e.g., [[], [], [], [], []]
    for j in src:
        L[j % len(src)-1].append(j)  # e.g., [[1, 1], [2], [], [4], [5]]
    output = []
    for i in L:
        output.extend(i)
    return output


if __name__ == '__main__':
    unsorted_int_list = [4, 1, 2, 5, 1]
    assert count_sort(unsorted_int_list) == [1, 1, 2, 4, 5]
