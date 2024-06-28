# from pudb import set_trace; set_trace()
from collections import deque
from typing import List
import math


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        We will use monotonic increasing array to keep track of the min of the
        current sliding window, and monotonic decreasing array for the max.

        O(N), 463 ms, faster than 43.47%
        """
        mon_inc = deque()
        mon_dec = deque()
        res = 0
        lo = 0
        for hi, n in enumerate(nums):
            while mon_inc and mon_inc[-1] > n:
                mon_inc.pop()
            mon_inc.append(n)

            while mon_dec and mon_dec[-1] < n:
                mon_dec.pop()
            mon_dec.append(n)

            while lo < len(nums) and mon_dec[0] - mon_inc[0] > limit:
                if nums[lo] == mon_dec[0]:
                    mon_dec.popleft()
                if nums[lo] == mon_inc[0]:
                    mon_inc.popleft()
                lo += 1
            res = max(res, hi - lo + 1)
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
