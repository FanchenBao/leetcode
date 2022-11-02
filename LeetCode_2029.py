# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def stoneGameIX(self, stones: List[int]) -> bool:
        """First, turn all the vals in stones to remainder after divided by 3,
        and get their count. Then the problem becomes taking 0, 1, 2 in turn
        to avoid coming to multiple of three. Let's put the count into a counter
        c.

        We know that for A to play optimally, she cannot take 0. So she only
        has two choices, either 1 or 2, provided that they exist. If there is
        no 1 or 2, A loses because she has to take 0.

        If 1 exists and A takes 1. Then to prolong the game as much as possible,
        both A and B have to take 0, because it is always safe. If we have even
        number of zeros, We can have

        ABABABABABABA
        1000012121212

        Or

        ABABABABABABA
        1100002121212

        Thus in either situation, after zeros are exhausted, A always has to
        take 2 and B always has to take 1. If we want A to win in this scenario,
        we must force B to take 2, which means there has to be more 2s than 1s.
        Hence, if A takes 1 and the number of zeros is even, A is guaranteed to
        win if we have c[2] > c[1] - 1 (the one in the minus is to remove the
        first choice of A).

        Similarly, if 2 exists and A takes 2, and there are even number of
        zeros, we have

        ABABABABABABA
        2000021212121

        Or

        ABABABABABABA
        2200001212121

        To ensure that A wins, there has to be more 1s than 2s. Hence, A wins
        if we have c[1] > c[2] - 1 (the one in the minus is to remove the first
        choice of A).

        If the number of zeros is odd, and if 1 exists and A takes 1, we have:

        ABABABABABABA
        1000121212121

        Or

        ABABABABABABA
        1100021212121

        A wins if we have more 1s than 2s, i.e. c[1] - 1 > c[2] (the minus one
        is to count for A's first choice) and c[1] - 2 > c[2] (the minus two is
        to count for A's and B's first choices'). This amounts to
        c[1] - 2 > c[2]

        If the number of zeros is odd, and if 2 exists and A takes 2, we have:

        ABABABABABABA
        2000212121212

        Or

        ABABABABABABA
        2200012121212

        A wins if we have more 2s than 1s, i.e. c[2] - 1 > c[1] (the minus one
        is to count for A's first choice) and c[2] - 2 > c[1] (the minus two is
        to count for A's and B's first choices'). This amounts to
        c[2] - 2 > c[1]

        These are all the situations.

        O(N), 2521 ms, faster than 62.71%
        """
        c = Counter(s % 3 for s in stones)
        if c[1] == c[2] == 0:
            return False
        if c[0] % 2 == 0:
            if c[1] == 0:
                return c[1] > c[2] - 1  # A takes 2 first
            if c[2] == 0:
                return c[2] > c[1] - 1  # A takes 1 first
            return c[1] > c[2] - 1 or c[2] > c[1] - 1  # A can take either 1 or 2
        # number of zero is odd
        if c[1] == 0:
            return c[2] - 2 > c[1]  # A takes 2 first
        if c[2] == 0:
            return c[1] - 2 > c[2]  # A takes 1 first
        return c[2] - 2 > c[1] or c[1] - 2 > c[2]  # A can take either 1 or 2


class Solution2:
    def stoneGameIX(self, stones: List[int]) -> bool:
        """Inspired by lee215

        https://leetcode.com/problems/stone-game-ix/discuss/1500245/JavaC%2B%2BPython-Easy-and-Concise-6-lines-O(n)

        We see that if c[0] is even, if c[1] == 0, it is impossible to have
        c[1] > c[2] - 1. Similarly, if c[2] == 0, it is impossible to have
        c[2] > c[1] - 1. Thus, for A to win, c[1] and c[2] must both not be
        zero. On the other hand c[1] > c[2] - 1 => c[2] - c[1] < 1 =>
        c[2] <= c[1]. Similarly c[2] > c[1] - 1 is equivalent to c[1] <= c[2].
        This means, as long as c[1] and c[2] are not both zero, any value of
        c[1] and c[2] would work to let A win.

        If c[0] is odd, we see that c[1] is zero or not, or c[2] is zero or not
        does not affect the outcome. Thus, we only need to ensure either
        c[2] - 2 > c[1], which is equivalent to c[2] - c[1] > 2. Or
        c[1] - 2  > c[2], which is equivalent to c[1] - c[2] > 2.
        Hence, the condensed version is abs(c[1] - c[2]) > 2
        """
        c = Counter(s % 3 for s in stones)
        if c[0] % 2 == 0:
            return c[1] * c[2] > 0
        return abs(c[1] - c[2]) > 2


sol = Solution2()
tests = [
    ([2, 1], True),
    ([2], False),
    ([5, 1, 2, 3, 4], False),
]

for i, (stones, ans) in enumerate(tests):
    res = sol.stoneGameIX(stones)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
