# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        """DP.

        O(N), 300 ms, faster than 50.32%
        """
        res, pre = 0, -math.inf
        indices = {le: i for i, le in enumerate(chars)}
        for le in s:
            c = vals[indices[le]] if le in indices else (ord(le) - 96)
            pre = max(pre + c, c)
            res = max(res, pre)
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
