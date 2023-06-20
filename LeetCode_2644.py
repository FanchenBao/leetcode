# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        """Brute force, because the size of nums and divisors are only 1000

        O(MN), 5766 ms, faster than 25.04%
        """
        counter = Counter(nums)
        res, ds = -1, -1
        for d in sorted(set(divisors)):
            cur_ds = sum(c for n, c in counter.items() if n % d == 0)
            if cur_ds > ds:
                res, ds = d, cur_ds
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
