# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right
from itertools import accumulate


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        """LeetCode 2389

        Prefix sum of sorted nums, then binary search
        O((N + M)logN), 92 ms, faster than 99.90%
        """
        arr = list(accumulate(sorted(nums)))
        return [bisect_right(arr, q) for q in queries]


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
