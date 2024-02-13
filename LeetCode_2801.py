# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
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


sol = Solution()
tests = [
    # ("12", "123", 19),
    # ('12', '234', 23),
    # ("12", "890", 45),
    ("26", "60", 6),
]

for i, (low, high, ans) in enumerate(tests):
    res = sol.countSteppingNumbers(low, high)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
