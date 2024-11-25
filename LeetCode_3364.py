# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def slidingwindow(self, nums: List[int], size: int) -> int:
        """
        Absolutely brute force. O(N^2)
        """
        res = 1000000
        s = 0
        i = 0
        for j in range(len(nums)):
            s += nums[j]
            if j - i + 1 > size:
                s -= nums[i]
                i += 1
            if s > 0 and j - i + 1 == size:
                res = min(res, s)
        return res

    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        res = 1000000
        for size in range(l, r + 1):
            res = min(res, self.slidingwindow(nums, size))
        return res if res < 1000000 else -1


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
