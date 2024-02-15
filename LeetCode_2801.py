# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        """
        The basic idea is to use DP to find the number of stepping numbers
        given the first digit and the total number of digits. For example,
        dp(3, 5) = the number of stepping numbers starting with 3 and having
        5 digits.
        
        Then we break down the problem into finding all the stepping numbers
        with the same starting digit as low and same length, finding the stepping
        numbers with the same starting digit as high and same length, and then
        finding all the stepping numbers in between.
        
        The tricky part is when low and high have the same number of digits and/or
        the same first digit. I used a separate function to handle that scenario.
        
        O(10 * 10 * len(high)) 134 ms, faster than 94.74%
        """
        
        @lru_cache(maxsize=None)
        def dp(st: int, num_digits: int) -> int:
            """
            dp(st, num_digit) returns the number of stepping numbers starting
            with digit st and having num_digits number of digits.
            """
            if num_digits < 0:
                return 0
            if num_digits <= 1:
                return 1
            if st == 9:
                return dp(8, num_digits - 1)
            if st == 0:
                return dp(1, num_digits - 1)
            return dp(st + 1, num_digits - 1) + dp(st - 1, num_digits - 1)

        
        def count_edge_case(edge: str, is_low: bool) -> int:
            """
            edge is either the str version of low or high.
            
            This function returns the count of stepping numbers with the
            same starting digit and same length as edge.
            """
            queue = [int(edge[0])]
            idx = 0
            count = 0
            while queue and idx < len(edge):
                tmp = []
                for d in queue:
                    cur = int(edge[idx])
                    if d == cur:
                        if d > 0:
                            tmp.append(d - 1)
                        if d < 9:
                            tmp.append(d + 1)
                    elif (is_low and d > cur) or (not is_low and d < cur):
                        count += dp(d, len(edge) - idx)
                queue = tmp
                idx += 1
            if idx == len(edge) and queue:
                count += 1
            return count
        
        def count_edge_case_both():
            """
            This function counts the number of stepping numbers between low
            and high when low and high have the same number of digits and the
            same first digit
            """
            queue = [int(low[0])]
            idx = 0
            count = 0
            while queue and idx < len(low):
                tmp = []
                for d in queue:
                    cur_low = int(low[idx])
                    cur_high = int(high[idx])
                    if d == cur_low == cur_high:
                        if d > 0:
                            tmp.append(d - 1)
                        if d < 9:
                            tmp.append(d + 1)
                    elif cur_low < d < cur_high:
                        count += dp(d, len(low) - idx)
                    elif cur_low == d and d < cur_high:
                        count += count_edge_case(low[idx:], True)
                    elif cur_low < d and d == cur_high:
                        count += count_edge_case(high[idx:], False)
                queue = tmp
                idx += 1
            if idx == len(low) and queue:
                count += 1
            return count

        if len(low) == len(high):
            if low[0] == high[0]:
                return count_edge_case_both()
            
            res = count_edge_case(low, True) + count_edge_case(high, False)
            if int(low[0]) < 9:
                for st in range(int(low[0]) + 1, int(high[0])):
                    res += dp(st, len(low))
        else:
            res = count_edge_case(low, True) + count_edge_case(high, False)
            # count the rest of the stepping numbers with the same number of digits
            # as low
            if int(low[0]) < 9:
                for st in range(int(low[0]) + 1, 10):
                    res += dp(st, len(low))
            # count the rest of the stepping numbers with the same number of digits
            # as high
            if int(high[0]) > 1:
                for st in range(int(high[0]) - 1, 0, -1):
                    res += dp(st, len(high))
            # count the stepping numbers in between
            for num_digits in range(len(low) + 1, len(high)):
                for st in range(1, 10):
                    res += dp(st, num_digits)
        return res % 1000000007


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        """
        This solution is inspired by 
        https://leetcode.com/problems/count-stepping-numbers-in-range/discuss/3836255/Python-Digit-DP-Clean-and-Concise

        The idea is to set dp(n) to be the total count of stepping numbers
        from 0 to n. Once we get this done, the answer is as simple as
        dp(high) - dp(low - 1)

        O(2 * 10 * N * 10), 367 ms.
        """
        
        def count(n_str: str) -> int:
            if n_str == '0':
                return 0

            @lru_cache(maxsize=None)
            def dp(idx: int, pre_digit: int, is_tight: bool) -> int:
                """
                If is_tight is true, that means the choice of the current digit
                cannot exceed n_str[idx]. Otherwise, we can choose any digit from
                0 to 9.
                """
                if idx == len(n_str):
                    return 1
                # we can always choose not to start from the current index
                res = 0
                digit_n = int(n_str[idx])
                if pre_digit == -1:
                    if idx == 0:
                        for cur_digit in range(1, digit_n):
                            res += dp(idx + 1, cur_digit, False)
                        res += dp(idx + 1, digit_n, True)
                    else:
                        for cur_digit in range(1, 10):
                            res += dp(idx + 1, cur_digit, False)
                else:
                    ops = []
                    if pre_digit < 9:
                        ops.append(pre_digit + 1)
                    if pre_digit > 0:
                        ops.append(pre_digit - 1)
                    for cur_digit in ops:
                        if not is_tight or cur_digit <= digit_n:
                            res += dp(idx + 1, cur_digit, is_tight and cur_digit == digit_n)
                return res
            
            # find stepping numbers of the same number of digits as n_str
            res = dp(0, -1, True)
            # find stepping numbers of fewer number of digits as n_str
            for i in range(1, len(n_str)):
                res += dp(i, -1, False)
            return res

        return (count(high) - count(str(int(low) - 1))) % 1000000007


sol = Solution()
tests = [
    ("12", "123", 19),
    ('12', '234', 23),
    ("12", "890", 45),
    ("26", "60", 6),
    # ("90", "101", 2),
]

for i, (low, high, ans) in enumerate(tests):
    res = sol.countSteppingNumbers(low, high)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
