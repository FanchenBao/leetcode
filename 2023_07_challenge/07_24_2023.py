# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """LeetCode 50

        I have always had problems with the fast power (or fast multiply) algo.
        Still didn't get it the first try, but it was pretty close. Keep in mind
        that the fast method is doubling the base. Whenever the power is odd,
        we apply the current base to the result. Then we continue doubling the
        base.

        45 ms, faster than 67.85%
        """
        
        def pow(a: int, b: int) -> int:
            """a to the power of b"""
            res = 1
            while b:
                if b % 2 == 1:
                    res *= a
                a *= a
                b //= 2
            return res

        res = pow(x, abs(n))
        return res if n >= 0 else 1 / res


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
