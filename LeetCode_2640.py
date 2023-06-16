# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate


class Solution1:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        """Just a fancy way to produce prefix sum

        O(N), 527 ms, faster than 88.93%
        """
        pre_max = 0
        res = [0]
        for n in nums:
            pre_max = max(pre_max, n)
            res.append(res[-1] + pre_max + n)
        return res[1:]


class Solution2:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        """Two accumulate to solve the problem in one line.

        https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array/discuss/3420109/C++-Python3-Prefix-Sum/1864407

        533 ms, faster than 82.76%
        """
        return list(accumulate(n + premax for n, premax in zip(nums, accumulate(nums, max))))

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
