# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        """
        Prepare a list of numbers for each max digit.
        Then return the max sum of the largest two numbers
        in each list.

        O(NlogN), 101 ms, faster than 88.64%
        """
        digit_num_map = defaultdict(list)
        for n in nums:
            digit_num_map[max(str(n))].append(n)
        res = -1
        for v in digit_num_map.values():
            if len(v) >= 2:
                v.sort()
                res = max(res, v[-1] + v[-2])
        return res


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]
#
# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
