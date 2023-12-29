# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache
from collections import Counter


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        """
        LeetCode 1531

        A nightmare problem, and I failed to solve it again. Just read
        the two comments I made to understand the very very brilliant
        solution

        https://leetcode.com/problems/string-compression-ii/discuss/756022/C++-Top-Down-DP-with-explanation-64ms-short-and-clear/1645542

        O(NK), 2318 ms, faster than 46.00%
        """
        def encoded_len(l: int) -> int:
            if l == 1:
                return 1
            if l < 10:
                return 2
            if l < 100:
                return 3
            return 4

        @lru_cache(maxsize=None)
        def dp(idx: int, rem: int) -> int:
            if rem < 0:  # cannot remove anymore
                return math.inf
            if len(s) - idx <= rem:  # we can remove everything
                return 0
            # try to go through all possible ways to form the first
            # group in the final solution by removing all the letters
            # from idx to some i such that the remaining letters are
            # all the same but with different lengths
            max_count = 0
            counter = Counter()
            res = math.inf
            for i in range(idx, len(s)):
                counter[s[i]] += 1
                max_count = max(max_count, counter[s[i]])
                to_remove = i - idx + 1 - max_count
                res = min(res, encoded_len(max_count) + dp(i + 1, rem - to_remove))
            return res

        return dp(0, k)



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
