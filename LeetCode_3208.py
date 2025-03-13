# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        """
        This is from the editorial. We keep track of the length of an alter-
        nating stretch of numbers. The simplicity also allows us to easily
        wrap around using modulo.

        O(N), 702 ms 88.64%
        """
        res = 0
        length = 1
        N = len(colors)
        for i in range(1, N + k - 1):
            if colors[i % N] != colors[(i - 1) % N]:
                length += 1
            else:
                res += max(0, length - k + 1)
                length = 1
        return res + max(0, length - k + 1)


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
