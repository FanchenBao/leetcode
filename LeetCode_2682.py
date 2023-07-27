# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        """MOD

        65 ms, faster than 79.65%
        """
        seen = set()
        cur, rnd = 0, 1
        while cur not in seen:
            seen.add(cur)
            cur = (cur + rnd * k) % n
            rnd += 1
        return [i + 1 for i in range(n) if i not in seen]


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
