# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left


class Solution:
    def get_lis_lengths(self, nums: List[int]) -> List[int]:
        aux: List[int] = []
        res = [0] * len(nums)
        for i, n in enumerate(nums):
            idx = bisect_left(aux, n)
            if idx == len(aux):
                aux.append(n)
            else:
                aux[idx] = n
            res[i] = len(aux)
        return res

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        """
        This is the official solution that uses O(NlogN) to produce longest
        increasing sequence (LIS).

        The problem can be solved by finding the longest LIS from left to
        right and right to left for a subarray ending at each index i.

        Then the longest mountain array that can be formed with nums[i] as its
        peak is lrlis[i] + rllis[i] - 1.

        The naive way to compute lrlis and rllis is through O(N^2). But there
        is a O(NlogN) way to do it, which involves a very ingenious method
        of building the optimal LIS at each step: replace the smallest value
        that is bigger than the current number in the LIS.

        O(NlogN), 19 ms, faster than 86.77%
        """
        lrlis = self.get_lis_lengths(nums)
        rllis = self.get_lis_lengths(nums[::-1])[::-1]
        longest_mountain = 0
        for i, lrlen in enumerate(lrlis):
            rllen = rllis[i]
            if lrlen > 1 and rllen > 1:
                longest_mountain = max(longest_mountain, lrlen + rllen - 1)
        return len(nums) - longest_mountain


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
