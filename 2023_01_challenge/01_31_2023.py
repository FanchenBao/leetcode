# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """TLE
        """
        scoreage = sorted((s, a) for a, s in zip(ages, scores))

        @lru_cache(maxsize=None)
        def dp(idx: int, max_age: int) -> int:
            if idx == len(scoreage):
                return 0
            if scoreage[idx][1] >= max_age:
                op1 = scoreage[idx][0] + dp(idx + 1, scoreage[idx][1])
            else:
                op1 = 0
            op2 = dp(idx + 1, max_age)
            return max(op1, op2)

        return dp(0, 0)


class Solution2:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """LeetCode 1626

        The runtime of this is the same as Solution1, both O(MN), where M is
        len of scores and N is the max age. But I guess a bottom up solution
        has lower overhead.

        3536 ms, faster than 24.12%
        """
        scoreage = sorted((s, a) for a, s in zip(ages, scores))
        M, N = len(scoreage), max(ages)
        dp = [0] * (N + 1)
        # first row
        for j in range(scoreage[0][1], N + 1):
            dp[j] = scoreage[0][0]
        for i in range(1, M):
            dp[scoreage[i][1]] += scoreage[i][0]
            for j in range(scoreage[i][1] + 1, N + 1):
                dp[j] = max(dp[j], dp[scoreage[i][1]])
        return max(dp)


class Solution3:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """Another attempt at top down, following the official solution.

        Sort by age and then score. The different from solution 1 is that the
        state is current idx and the index of the player chosen previously. The
        key is that the previously chosen player must have the highest age and
        highest score so far. Thus to determine whether the current player
        should be chosen, we only need to compare to the score of the previously
        chosen player
        """
        agescore = sorted((a, s) for a, s in zip(ages, scores))

        @lru_cache(maxsize=None)
        def dp(idx: int, pre: int) -> int:
            if idx == len(agescore):
                return 0
            if pre < 0 or agescore[idx][1] >= agescore[pre][1]:
                op1 = agescore[idx][1] + dp(idx + 1, idx)
            else:
                op1 = 0
            op2 = dp(idx + 1, pre)
            return max(op1, op2)

        return dp(0, -1)


sol = Solution3()
tests = [
    ([1,3,5,10,15], [1,2,3,4,5], 34),
    ([4,5,6,5], [2,1,2,1], 16),
    ([1,2,3,5], [8,9,10,1], 6),
]

for i, (scores, ages, ans) in enumerate(tests):
    res = sol.bestTeamScore(scores, ages)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
