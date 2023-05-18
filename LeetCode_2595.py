# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def evenOddBit(self, n: int) -> List[int]:
        """The indexing for the binary representation is from right to left.

        48 ms, faster than 6.85%
        """
        res = [0, 0]
        for i, d in enumerate(bin(n)[2:][::-1]):
            res[i % 2] += int(d == '1')
        return res


class Solution3:
    def evenOddBit(self, n: int) -> List[int]:
        """Very smart solution: https://leetcode.com/problems/number-of-even-and-odd-bits/discuss/3316862/Python-3-oror-2-lines-w-example-oror-TM%3A-31-ms-13.8-MB

        Since n <= 1000, we can use bitmask to identify the even and odd
        positions of n.
        """
        even_mask, odd_mask = int('0101010101', 2), int('1010101010', 2)
        return [(even_mask & n).bit_count(), (odd_mask & n).bit_count()]


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
