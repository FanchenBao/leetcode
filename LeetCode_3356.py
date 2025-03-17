# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        """
        This is inspired by the editorial. The method is linesweep but with
        only a single pass on nums and queries without additional sorting.

        The idea is that for each idx in nums, we go through queries from left
        to right until we are able to just have sufficient value to be not
        smaller than nums[idx]. During this traversal of queries, we update
        a delta array which indicates what the change will be at specific
        indices determined by the queries. As we move forward in nums, we make
        sure that each index can be fulfilled by queries. Whenever a nums[idx]
        does not work, return -1. Otherwise, we keep traversing queries until
        we hit a step where all the numbers in nums can be accounted for.

        O(M + N), 131 ms, 90.98%
        """
        N, M = len(nums), len(queries)
        cur = k = 0
        delta = [0] * (N + 1)
        for i, n in enumerate(nums):
            while k < M and cur + delta[i] < n:
                l, r, v = queries[k]
                if (
                    r >= i
                ):  # only consider the range that affects the current idx of nums
                    delta[max(i, l)] += v
                    delta[r + 1] -= v
                k += 1
            cur += delta[i]
            if cur < n:
                return -1
        return k


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
