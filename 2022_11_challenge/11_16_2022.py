# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def guessNumber(self, n: int) -> int:
        """LeetCode 374

        Binary search. O(logN), 64 ms, faster than 15.43%
        """
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            ver = guess(mid)
            if ver == 0:
                return mid
            if ver < 0:
                hi = mid
            else:
                lo = mid + 1
        return lo


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
