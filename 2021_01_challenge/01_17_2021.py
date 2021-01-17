# from pudb import set_trace; set_trace()
from typing import List
import itertools
import math


class Solution1:
    def countVowelStrings(self, n: int) -> int:
        """The CS solution. The idea is when we increase n, we can always find
        the solution by using the solution already computed in n - 1. E.g. when
        n = 3, we know that there are 15 choices for n = 2 with the smallest
        letter being 'a', 10 choices with the smallest letter being 'e', 6 for
        'i', 3 for 'o', and 1 for 'u'. Thus, if we set the first letter in n = 3
        to 'a', then I can take all 15 choices when n = 2; set the first letter
        to 'e', then I can take all 10 choices, etc. The result is that when
        n = 3, we have 15 + 10 + 6 + 3 + 1 = 35 choices with the smallest letter
        being 'a', 10 + 6 + 3 + 1 = 20 choices with the smallest letter being
        'e', so on and so forth. Here we have found the DP pattern.

        Put in an easier to understand manner:

        u, o, i, e, a

        n = 1: 1, 2, 3, 4, 5
        n = 2: 1, 3, 6, 10, 15
        n = 3: 1, 4, 10, 20, 35
        .
        .
        .

        The result for each n is the last element of the cumulative sum array.

        I tried to figure out the math solution. The formula for "i" is still
        doable: i(n) = 3 + (n + 2)(n - 1) / 2 + n - 1

        But the formula for "e" and "a" would take too much time to come up and
        I decide not to pursue.

        O(N), 24 ms, 96% ranking.
        """
        base = list(range(1, 6))
        for _ in range(1, n):
            for i in range(1, 5):
                base[i] += base[i - 1]
        return base[-1]


class Solution2:
    def countVowelStrings(self, n: int) -> int:
        """Use itertools.accumulate() to faciliate the computation of cumulative
        sum.
        """
        base = [1] * 5
        for _ in range(n):
            base = itertools.accumulate(base)
        return list(base)[-1]


class Solution3:
    def countVowelStrings(self, n: int) -> int:
        """The REAL math solution.

        See my own post here: https://leetcode.com/problems/count-sorted-vowel-strings/discuss/918498/JavaC++Python-DP-O(1)-Time-and-Space/822478
        """
        return math.comb(n + 4, 4)


sol = Solution3()
tests = [
    (1, 5),
    (2, 15),
    (33, 66045),
]

for i, (n, ans) in enumerate(tests):
    res = sol.countVowelStrings(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
