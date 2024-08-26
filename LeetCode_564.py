# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def find_prev_palin(self, num: int) -> int:
        lo, hi = 0, num
        res = 0
        while lo < hi:
            mid = (lo + hi) // 2
            palin = self.convert(mid)
            if palin < num:
                res = palin
                lo = mid + 1
            else:
                hi = mid
        return res

    def find_next_palin(self, num: int) -> int:
        lo, hi = num + 1, 10**19
        res = 0
        while lo < hi:
            mid = (lo + hi) // 2
            palin = self.convert(mid)
            if palin <= num:
                lo = mid + 1
            else:
                res = palin
                hi = mid
        return res

    def convert(self, num: int) -> int:
        str_num = str(num)
        mid = len(str_num) // 2 - 1
        return int(
            str_num[: mid + 1]
            + str_num[mid + 1 : (len(str_num) + 1) // 2]
            + str_num[: mid + 1][::-1]
        )

    def nearestPalindromic(self, n: str) -> str:
        """
        This uses the binary search method from the official solution.
        O(len(n)logN)
        """
        num = int(n)
        prev = self.find_prev_palin(num)
        next = self.find_next_palin(num)
        if num == prev:
            return str(next)
        if num == next:
            return str(prev)
        if num - prev <= next - num:
            return str(prev)
        return str(next)


#
# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]
#
# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f"Test {i}: PASS")
#     else:
#         print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
