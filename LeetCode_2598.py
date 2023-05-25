# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter, defaultdict


class Solution1:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        """Use a counter to find the total number of values in nums that share
        the same remainder when mod value.

        Then these numbers can form r, r + value, r + 2 * value, ...
        
        We use a set to record what values can be formed. Then the first value
        missing in this set is the answer.

        O(N), 1123 ms, faster than 15.50% 
        """
        rem_counter = Counter()
        for n in nums:
            rem_counter[n % value] += 1
        exists = set()
        for i in range(value):
            for j in range(rem_counter[i]):
                exists.add(i + value * j)
            if i not in exists:
                return i
        i = value
        while True:
            if i not in exists:
                return i
            i += 1


class Solution2:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        """Inspired by https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/discuss/3313988/Count-Moduli

        The answer cannot be larger than len(nums). And we don't have to
        prefill the exists set. We just need to iterate through len(nums)
        and find the first whose remainder after MOD value has no count in the
        rem_counter

        O(N), 1135 ms, faster than 14.32%
        """
        rem_counter = Counter()
        for n in nums:
            rem_counter[n % value] += 1
        for i in range(len(nums) + 1):
            if not rem_counter[i % value]:
                return i
            rem_counter[i % value] -= 1


sol = Solution2()
tests = [
    ([1,-10,7,13,6,8], 5, 4),
    ([1,-10,7,13,6,8], 7, 2),
    ([0,-3], 4, 2),
]

for i, (nums, value, ans) in enumerate(tests):
    res = sol.findSmallestInteger(nums, value)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
