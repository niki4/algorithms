"""
Radix Sort is kind of algorithm that works only to integers.
It's more powerful than Counting sort.

The idea is to sort nums by their place, from least significant digit first toward most significant one.

Assuming each integer in base b
=⇒ d = logb k digits ∈ {0, 1, . . . , b − 1}

E.g., having [329, 457, 657, 839, 436, 720, 355] as a source,
1. [720, 355, 436, 457, 657, 329, 839] # sorted by the last digit in each num
2. [720, 329, 436, 839, 355, 457, 657] # using result from prev. step, sorted by the second last digit in each num
3. [329, 355, 436, 457, 657, 720, 839] # finally, using result from prev. step, sorted by first digit in each num

Implementation adopted from MIT 6.006 course. Here is more explanation about it
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec07.pdf
"""

def radix_sort(src):
    for dig_order in range(len(str(src[0]))-1, -1, -1):
        src = sorted(src, key=lambda n: str(n)[dig_order])  # use list's .sort() method if you need in-place sort
    return src

if __name__ == '__main__':
    unsorted_int_list = [329, 457, 657, 839, 436, 720, 355]
    assert radix_sort(unsorted_int_list) == [329, 355, 436, 457, 657, 720, 839]
