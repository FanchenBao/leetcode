# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        """
        LeetCode 1239

        We use bitmask to represent each string in arr and the final
        concatenated string. The benefit of using bitmask is that we can
        determine whether there is duplicates in O(1) time.

        Then the problem is no different from a 0/1 Knapsack, which can be
        solved using DP.

        O(N * 2^26) 71 ms, faster than 88.77%
        """
        # create new arr that removes any string that contains duplicates
        newarr = []
        for a in arr:
            mask = 0
            for le in a:
                i = ord(le) - 97
                if (1 << i) & mask:
                    break
                mask |= (1 << i)
            else:
                newarr.append((mask, len(a)))

        @lru_cache(maxsize=None)
        def dp(idx: int, state: int) -> int:
            if idx == len(newarr):
                return 0
            res = dp(idx + 1, state)  # not taking newarr[idx]
            # or we take newarr[idx]
            if state & newarr[idx][0] == 0:
                res = max(res, newarr[idx][1] + dp(idx + 1, state | newarr[idx][0]))
            return res

        return dp(0, 0)



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
