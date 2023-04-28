# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        """LeetCode 319

        I think I have improved, because I am able to arrive at the good
        solution by myself. The last time I did this problem was December, 2021
        and at that time I was not able to figure out the trick that the
        solution is the number of squared numbers smaller or equal to n.

        The intuition is this, given any num, we can write it as:

        num = a1 * b1
        num = a2 * b2
        ...
        num = ak * bk
        num = bk * ak
        ...
        num = b2 * a2
        num = b1 * a1

        In these breaking-downs, a1 < a2 < ... < ak < bk < bk - 1 < ... < b2 < b1

        Therefore, any non-square number always have even number of ways to
        break it down, which means they have even number of toggles. The result
        is that any non-square number will always remain turned off after all
        the rounds.

        Thus, we only need to find the number of squared numbers within n. That
        can be achieved by math.floor(math.sqrt(n))

        O(logN), 37 ms, faster than 17.04%
        """
        return math.floor(math.sqrt(n))


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
