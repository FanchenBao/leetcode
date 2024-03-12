# from pudb import set_trace; set_trace()
from typing import List
import math
from sortedcontainers import SortedList


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        """
        Take advantage of SortedList and the problem become very doable.

        O(NlogN), 948 ms, faster than 89.47%
        """
        sorted_prefix = SortedList()
        N = len(nums)
        res = 10**9 + 7
        for i in range(x, N):
            sorted_prefix.add(nums[i - x])
            idx = sorted_prefix.bisect_right(nums[i])
            if idx > 0:
                res = min(res, nums[i] - sorted_prefix[idx - 1])
            if idx < len(sorted_prefix):
                res = min(res, sorted_prefix[idx] - nums[i])
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
