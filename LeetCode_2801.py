# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        
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
                        print(is_low, d, dp(d, len(edge) - idx))
                queue = tmp
                idx += 1
            if idx == len(edge) and queue:
                count += 1
            return count

        res = count_edge_case(low, True) + count_edge_case(high, False)
        print(count_edge_case(low, True), count_edge_case(high, False))
        if len(low) == len(high):
            if int(low[0]) < 9:
                for st in range(int(low[0]) + 1, int(high[0])):
                    res += dp(st, len(low))
                    print('low', st, dp(st, len(low)))
        else:
            # count the rest of the stepping numbers with the same number of digits
            # as low
            if int(low[0]) < 9:
                for st in range(int(low[0]) + 1, 10):
                    res += dp(st, len(low))
                    print('low', st, dp(st, len(low)))
            # count the rest of the stepping numbers with the same number of digits
            # as high
            if int(high[0]) > 1:
                for st in range(int(high[0]) - 1, 0, -1):
                    res += dp(st, len(high))
                    print('high', st, dp(st, len(high)))
            # count the stepping numbers in between
            for num_digits in range(len(low) + 1, len(high)):
                for st in range(1, 10):
                    res += dp(st, num_digits)
                    print('between', st, num_digits, res)
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
