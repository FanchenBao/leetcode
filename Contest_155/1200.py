#! /usr/bin/env python3
from typing import List
from random import randint

"""09/29/2019

Solution:

Sort the list first, then one pass to check each consecutive pair. Keep
updating the result array when a pair with smaller difference is found.

This solution clocks in at 408 ms, 81%.
"""


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sorted_arr: List[int] = sorted(arr)
        res: List[List[int]] = [[sorted_arr[0], sorted_arr[1]]]
        min_diff = sorted_arr[1] - sorted_arr[0]
        for i in range(2, len(sorted_arr)):
            curr_diff = sorted_arr[i] - sorted_arr[i - 1]
            if curr_diff < min_diff:
                res = [[sorted_arr[i - 1], sorted_arr[i]]]
                min_diff = curr_diff
            elif curr_diff == min_diff:
                res.append([sorted_arr[i - 1], sorted_arr[i]])
        return res


def gen_random_arr(LEN: int, MIN: int, MAX: int) -> List[int]:
    return [randint(MIN, MAX) for _ in range(LEN)]


sol = Solution()
arr = gen_random_arr(10 ** 5, -10 ** 6, 10 ** 6)
print(arr)
# print(sol.minimumAbsDifference(arr))
