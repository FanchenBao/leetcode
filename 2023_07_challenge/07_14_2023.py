# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """LeetCode 1218

        O(N), standard DP solution. 632 ms, faster than 13.72%

        UPDATE: we don't need the first max, because a later value will always
        have subsequence length not shorter than a previous occurrence of the
        same value.

        581 ms, faster than 43.56%
        """
        dp = defaultdict(int)
        res = 0
        for a in arr:
            dp[a] = dp[a - difference] + 1
            res = max(res, dp[a])
        return res


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
