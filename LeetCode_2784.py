# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def isGood(self, nums: List[int]) -> bool:
        """
        O(N), 55 ms, faster than 42.88%
        """
        N = len(nums) - 1
        counter = Counter(nums)
        return len(counter) == N and counter[N] == 2 and max(counter) == N


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        """
        O(NlogN), 48 ms, faster than 77.98%
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] != i + 1:
                return False
        return nums[-1] == len(nums) - 1



sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
