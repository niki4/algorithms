import random
from typing import List


class Solution:
    """
    Merge Sort, Top-down approach:
    1. In the first step, we divide the list into two sublists.  (Divide)
    2. Then in the next step, we recursively sort the sublists in the previous step.  (Conquer)
    3. Finally we merge the sorted sublists in the above step repeatedly to obtain the final list of sorted elements.  (Combine)

    Time complexity: O(N logN)
    """

    def merge(self, l_list: List[int], r_list: List[int]) -> List[int]:
        l_cursor = r_cursor = 0
        res = []
        while l_cursor < len(l_list) and r_cursor < len(r_list):
            if l_list[l_cursor] < r_list[r_cursor]:
                res.append(l_list[l_cursor])
                l_cursor += 1
            else:
                res.append(r_list[r_cursor])
                r_cursor += 1

        # add remaining elements from either of the lists
        res.extend(l_list[l_cursor:])
        res.extend(r_list[r_cursor:])
        return res

    def sort_array(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = int(len(nums) / 2)
        left_list = self.sort_array(nums[:pivot])
        right_list = self.sort_array(nums[pivot:])
        return self.merge(left_list, right_list)


if __name__ == '__main__':
    test_list = random.sample(range(1000), 10)
    sol = Solution()
    sorted_list = sol.sort_array(test_list)
    assert sorted_list != test_list
    assert sorted_list == sorted(test_list)
