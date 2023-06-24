# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def sumOfMultiples(self, n: int) -> int:
        """O(N), 106 ms, faster than 23.66% 
        """
        return sum(i for i in range(1, n + 1) if i % 3 == 0 or i % 5 == 0 or i % 7 == 0)


class Solution2:
    def sumOfMultiples(self, n: int) -> int:
        """This is O(1), 53 ms, faster than 94.70%
        """

        def find_sum(v: int) -> int:
            s = 0
            if n >= v:
                s = (v + n // v * v) * ((n // v * v - v) // v + 1) // 2
            return s

        s3 = find_sum(3)
        s5 = find_sum(5)
        s7 = find_sum(7)
        s15 = find_sum(15)
        s21 = find_sum(21)
        s35 = find_sum(35)
        s105 = find_sum(105)

        return s3 + s5 + s7 - s15 - s21 - s35 + s105


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
