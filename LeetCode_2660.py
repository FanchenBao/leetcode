# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        """O(N), 270 ms, faster than 73.69%
        """

        def compute_score(pins: List[int]) -> int:
            s = good_for = 0
            for p in pins:
                s += p * (2 if good_for else 1)
                if good_for:
                    good_for -= 1
                if p == 10:
                    good_for = 2
            return s

        s1, s2 = compute_score(player1), compute_score(player2)
        if s1 > s2:
            return 1
        if s1 < s2:
            return 2
        return 0


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
