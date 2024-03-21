# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left


class Solution1:
    def countPairs(self, nums: List[int], target: int) -> int:
        """
        Binary search

        O(NlogN) 47 ms, faster than 69.04%
        """
        nums.sort()
        res = 0
        for i, n in enumerate(nums):
            idx = bisect_left(nums, target - n)
            if idx - 1 <= i:
                break
            res += idx - 1 - i
        return res


class Solution2:
    def countPairs(self, nums: List[int], target: int) -> int:
        """
        From the title of the forum, try two pointer approach

        O(NlogN), 43 ms, faster than 87.08%
        """
        nums.sort()
        res = 0
        i, j = 0, len(nums) - 1
        while i < j:
            while i < j and nums[i] + nums[j] >= target:
                j -= 1
            if i < j:
                res += j - i
                i += 1
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
