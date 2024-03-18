# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def __init__(self):
        self.primes = [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
            101,
            103,
            107,
            109,
            113,
            127,
            131,
            137,
            139,
            149,
            151,
            157,
            163,
            167,
            173,
            179,
            181,
            191,
            193,
            197,
            199,
            211,
            223,
            227,
            229,
            233,
            239,
            241,
            251,
            257,
            263,
            269,
            271,
            277,
            281,
            283,
            293,
            307,
            311,
            313,
        ]

    def prime_score(self, n: int) -> int:
        score = 0
        for p in self.primes:
            if n % p == 0:
                score += 1
            while n and n % p == 0:
                n //= p
            if p > n:
                break
        return score if n == 1 else score + 1

    def maximumScore(self, nums: List[int], k: int) -> int:
        """
        It worked! First attempt! I am very happy.

        This is monotonic decreasing array. We use that to find the left and
        right bound that each number can extend. All subarrays within this
        range use the current number for multiplication. In other words, all
        the other numbers within the range have smaller (or equal if it is on
        the right hand side) prime score than the current number.

        Once we find the ranges for all the numbers, we only need to pick the
        largest number and exhaust all its possible subarrays. If there is
        still k left, we move on to the second largest number, and so on and
        so forth.

        O(NlogN), 2421 ms, faster than 89.74%
        """
        MOD = 10**9 + 7
        N = len(nums)
        scores = [self.prime_score(n) for n in nums]
        # find the left bound
        left_bound = [0] * N
        mono: List[int] = []
        for i in range(N):
            while mono and scores[mono[-1]] < scores[i]:
                mono.pop()
            if mono:
                left_bound[i] = mono[-1] + 1
            else:
                left_bound[i] = 0
            mono.append(i)
        # find the right bound
        right_bound = [N - 1] * N
        mono = []
        for i in range(N - 1, -1, -1):
            while mono and scores[mono[-1]] <= scores[i]:
                mono.pop()
            if mono:
                right_bound[i] = mono[-1] - 1
            else:
                right_bound[i] = N - 1
            mono.append(i)
        bound_comb = sorted(
            [
                [n, lb, rb, i]
                for i, (n, lb, rb) in enumerate(zip(nums, left_bound, right_bound))
            ],
            reverse=True,
        )
        res = 1
        for n, lb, rb, i in bound_comb:
            available = (i - lb + 1) * (rb - i + 1)
            res = (res * pow(n, min(available, k), MOD)) % MOD
            if k > available:
                k -= available
            else:
                break
        return res


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
