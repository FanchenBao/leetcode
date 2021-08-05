# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
from collections import defaultdict
import math
from random import randint


class Solution0:
    def stoneGame(self, piles: List[int]) -> bool:
        """TLE"""
        total = sum(piles)

        @lru_cache(maxsize=None)
        def dfs(lo: int, hi: int, alex_turn: bool, alex_score: int) -> bool:
            if lo > hi:
                return alex_score > total - alex_score
            if lo == hi:
                return dfs(lo + 1, hi, not alex_turn, alex_score + (piles[lo] if alex_turn else 0))
            if alex_turn:
                return dfs(lo + 1, hi, not alex_turn, alex_score + piles[lo]) or dfs(lo, hi - 1, not alex_turn, alex_score + piles[hi])
            else:
                return dfs(lo + 1, hi, not alex_turn, alex_score) and dfs(lo, hi - 1, not alex_turn, alex_score)

        return dfs(0, len(piles) - 1, True, 0)


class Solution1:
    def stoneGame(self, piles: List[int]) -> bool:
        """The correct way to do DFS. From the official solution

        https://leetcode.com/problems/stone-game/solution/
        """

        @lru_cache(maxsize=None)
        def dfs(lo: int, hi: int) -> int:
            """The return value is the difference between Alex and Lee's score"""
            if lo + 1 == hi:
                return abs(piles[lo] - piles[hi])
            if (hi - lo + 1) % 2:  # Lee's turn, optimal move
                return min(dfs(lo + 1, hi) - piles[lo], dfs(lo, hi - 1) - piles[hi])
            else:  # Alex's turn, optimal move
                return max(dfs(lo + 1, hi) + piles[lo], dfs(lo, hi - 1) + piles[hi])

        return dfs(0, len(piles) - 1) > 0


class Solution2:
    def stoneGame(self, piles: List[int]) -> bool:
        """LeetCode 877

        We basically iterate through the optimal moves for all possible
        ranges in the piles for Alex and Lee. Note that Alex makes a move when
        there are even number of piles, Lee odd. We build it from bottom up and
        keep track of the max difference between Alex and Lee's scores for each
        range. Starting from two piles. It's always Alex's turn and he is always
        not going to lose because he can pick the larger pile. We record the
        score difference for all range of two. Then for each range, we expand
        one to the left or to the right, if possible. In Lee's turn, during
        expansion, we deduct the newly expanded value from the diff, and we keep
        the smallest diff if repeated range occurs. This is to say Lee is
        playing optimal for his part. Similarly, in Alex's turn, we expand and
        add the expanded value to the diff, and we keep the max diff for each
        range. This is to say that Alex is playing optimal for his part.

        The key trick is to NOT assum that taking the larger pile in each step
        is the optimal move. In other words, we have to expand on both ends,
        instead of picking the end with a higher stone count.

        We continue this until the range covers the entire piles. That's when
        we check whether the diff is positive. If it is, Alex is going to win
        otherwise lose.

        O(N^2), 840 ms, 10% ranking.

        UPDATE: it is so stupid to use a dict with tuple as keys. It can be
        simplified by using a 2D array.
        """
        memo = {(i, i + 1): abs(piles[i] - piles[i + 1]) for i in range(len(piles) - 1)}
        while len(memo) > 1:
            temp = {}
            for (lo, hi), diff in memo.items():
                if (hi - lo + 1) % 2:  # Alex's turn
                    if hi + 1 < len(piles):
                        temp[(lo, hi + 1)] = max(diff + piles[hi + 1], temp.get((lo, hi + 1), -math.inf))
                    if lo - 1 >= 0:
                        temp[(lo - 1, hi)] = max(diff + piles[lo - 1], temp.get((lo - 1, hi), -math.inf))
                else:  # Lee's turn
                    if hi + 1 < len(piles):
                        temp[(lo, hi + 1)] = min(diff - piles[hi + 1], temp.get((lo, hi + 1), math.inf))
                    if lo - 1 >= 0:
                        temp[(lo - 1, hi)] = min(diff - piles[lo - 1], temp.get((lo - 1, hi), math.inf))
            memo = temp
        return memo[(0, len(piles) - 1)] > 0


ref = Solution0()
sol = Solution1()
tests = [
    ([5, 3, 4, 5], True),
    ([1, 2], True),
    ([34, 100, 35, 29, 95, 3, 76, 26, 81, 48, 61, 4, 30, 90, 31, 21, 16, 70, 40, 46, 30, 76, 40, 25, 92, 99, 10, 12, 70, 82, 62, 98, 14, 68, 94, 5, 9, 64, 34, 89, 98, 54, 41, 56, 60, 30, 4, 38, 67, 76, 71, 40, 89, 83, 19, 49, 97, 97, 61, 95, 6, 55, 14, 34, 35, 44, 68, 51, 32, 93, 36, 98, 87, 79, 29, 46, 46, 8, 75, 18, 63, 9, 52, 60, 3, 76, 89, 86, 4, 22, 7, 30, 93, 31, 52, 28, 51, 74, 95, 60], True),
    ([171, 25, 41, 45, 93, 178, 106, 22, 200, 93, 187, 141, 116, 32, 36, 189, 157, 51, 15, 64, 186, 88, 140, 112, 99, 112, 83, 148, 84, 191, 45, 53, 86, 75, 16, 44, 10, 83, 128, 18, 122, 118, 51, 111, 136, 147, 102, 97, 145, 189, 196, 180, 184, 85, 129, 82, 60, 29, 30, 49, 28, 61, 52, 138, 155, 63, 30, 186, 29, 191, 17, 151, 188, 113, 150, 161, 18, 171, 104, 135, 168, 40, 196, 46, 166, 171, 32, 128, 37, 169, 19, 113, 18, 191, 125, 32, 115, 85, 44, 51, 83, 67, 55, 140, 147, 191, 17, 94, 65, 115, 31, 48, 65, 129, 181, 122, 128, 143, 200, 8, 66, 152, 195, 43, 198, 165, 154, 1, 91, 183, 46, 189, 14, 184, 148, 31, 129, 104, 2, 97, 39, 46, 156, 89, 58, 144, 27, 49, 162, 74, 163, 113, 8, 15, 27, 163, 65, 47, 91, 61, 55, 16, 45, 155, 119, 136, 172, 1, 193, 39, 153, 130, 66, 57, 140, 4, 183, 182, 26, 43, 105, 144, 185, 35, 84, 114, 39, 128, 31, 30, 24, 56, 187, 83, 133, 133, 79, 87, 161, 18], True),
    ([1, 4, 2, 1, 7, 2], True),
    ([2, 1, 2, 9, 3, 2], True),
    ([6, 5, 3, 9, 6, 6], True),
    ([4, 2, 7, 10, 4, 4], True),
    ([7, 1, 1, 8, 7, 7], True),
]
for i, (piles, ans) in enumerate(tests):
    res = sol.stoneGame(piles)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}: Fail. Ans: {ans}, Res: {res}')

# tests = [[randint(1, 10) for _ in range(6)] for _ in range(1000)]
# for i, test in enumerate(tests):
#     if sum(test) % 2:
#         ans = ref.stoneGame(test)
#         res = sol.stoneGame(test)
#         if ans != res:
#             print(f'Test {i}: Fail. Ans: {ans}, Res: {res}, Test: {test}')

