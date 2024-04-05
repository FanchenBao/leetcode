# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        """
        I took two hints, one from the official website, and the other from
        a top solution in the forum which says to use DP on the digits.

        Hence, we have dp(number_of_digits, number_of_odd_remained, is_bounded, current_remainder, high_bound_str)
        to compute the number of integers with the given number of digits,
        number of odds allowed, etc. that MOD k returns the given remainder

        Then we develop a count function to actually count the number of
        beautiful integers from 1 to a given high bound. The count function
        decides the first digit, and then use dp to find the total number of
        beautiful integers starting with the given first digit.

        64 ms, faster than 98.58%
        """

        def get_next_remainder(cur_digit: int, nd: int, cur_r: int) -> int:
            return (cur_r - (cur_digit * 10 ** (nd - 1)) % k + k) % k

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
                next_r = get_next_remainder(d, nd, r)
                res += dp(
                    nd - 1,
                    no - d % 2,
                    is_bounded and d == max_allowed,
                    next_r,
                    high_bound_str,
                )
            return res

        def count(high_bound: int) -> int:
            """
            Count the number of beautiful integers from 1 to high_bound
            """
            high_bound_str = str(high_bound)
            res = 0
            nd = len(high_bound_str)
            if nd % 2 == 0:
                # bounded
                fd = int(high_bound_str[0])
                next_r = get_next_remainder(fd, nd, 0)
                res += dp(nd - 1, nd // 2 - fd % 2, True, next_r, high_bound_str)
                # unbounded
                for d in range(1, fd):
                    next_r = get_next_remainder(d, nd, 0)
                    res += dp(nd - 1, nd // 2 - d % 2, False, next_r, "")
                nd -= 2
            else:
                nd -= 1
            for next_nd in range(nd, 0, -2):
                # all unbounded
                for d in range(1, 10):
                    next_r = get_next_remainder(d, next_nd, 0)
                    res += dp(next_nd - 1, next_nd // 2 - d % 2, False, next_r, "")
            return res

        return count(high) - count(low - 1)


sol = Solution()
tests = [
    (10, 20, 3, 2),
]

for i, (low, hi, k, ans) in enumerate(tests):
    res = sol.numberOfBeautifulIntegers(low, hi, k)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
