# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        
        @lru_cache(maxsize=None)
        def dp(nd: int, no: int, is_bounded: bool, r: int, high_bound_str: str) -> int:
            """
            nd: number of digits
            no: number of odds
            is_bounded: for the current digit, whether we can go all the way
            to 9
            r: the target remainder to reach for the current number
            high_bound: the max number allowed. We use this to determine the
            bound for a digit if applicable
            """
            if no < 0:
                return 0
            if nd == 0:
                return int(r == 0 and no == 0)
            max_allowed = 9
            if is_bounded:
                max_allowed = int(high_bound_str[-nd])
            res = 0
            for d in range(max_allowed + 1):
                next_r = (r - (d * 10**(nd - 1)) % k + k) % k
                res += dp(nd - 1, no - d % 2, is_bounded and d == max_allowed, next_r, high_bound_str)
            return res

        def count(high_bound: int) -> int:
            high_bound_str = str(high_bound)
            res = 0
            if len(high_bound_str) % 2 != 0:
                cur_nd = len(high_bound_str) - 1
                for d in range(10):
                    next_r = (0 - (d * 10**(cur_nd - 1)) % k + k) % k 
                    res += dp(cur_nd - 1, no - d % 2, False, nex_r, '')
            else:
                # to be contonued

        high_count = 0
        high_str = str(high)
        for d in range(1, int(high_str[0]) + 1):
            high_count += dp(len(high_str) - 1, )




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
