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

        Unfortunately, still cannot do it. TLE.
        I guess top down is not going to work in Python.
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


class Solution4:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """Bottom up version of Solution3

        max_score[i] is the max score achieved choosing players from 0 to i
        (must include i) in agescore

        O(N^2), 5609 ms, faster than 13.29%
        """
        agescore = sorted((a, s) for a, s in zip(ages, scores))
        max_score = [0] * len(agescore)
        for i in range(len(agescore)):  # current index
            cur_max = agescore[i][1]
            for j in range(i):  # previously selected index
                op1 = (max_score[j] + agescore[i][1]) * int(agescore[i][1] >= agescore[j][1])
                op2 = agescore[i][1]
                cur_max = max(cur_max, max(op1, op2))
            max_score[i] = cur_max
        return max(max_score)


class BIT:
    def __init__(self, N: int):
        """Initialize a binary indexed tree.

        :param N: The size of the range, including min and max.
        """
        # use 1-based BIT, thus array size must be one larger than the range.
        self.bit = [0] * (N + 1)

    def update(self, pos: int, cur: int) -> None:
        """Update the value at `pos` by changing it to cur if cur is larger.
        """
        # KEY POINT: BIT index is 1-based, thus its index is one larger
        # than the given position.
        i = pos + 1
        while i < len(self.bit):
            self.bit[i] = max(self.bit[i], cur)
            i += (i & -i)

    def query(self, max_r: int) -> int:
        """Query the max values in the range 0 to `max_r`.
        """
        # KEY POINT: Bit index is 1-based, thus its index is one larger
        # than the given max range.
        i, res = max_r + 1, 0
        while i:
            res = max(res, self.bit[i])
            i -= (i & -i)
        return res


class Solution5:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        """This is the BIT solution from the official solution.

        We sort based on score first, and then age.

        Then we iterate through scoreage. For each score s and its age a, we
        want to find the max score that can be obtained by all previous players
        with age <= a. Since we have sorted by score, it is guaranteed that all
        previous players have score smaller or equal to s, which means the
        current player is eligible if all previous players have age smaller or
        equal to a.

        To find the max of all ages up till a is a BIT problem. Thus, we create
        a BIT, with the total length being max age + 1. Then for each player
        (s, a), we get the max score up till a by bit.query(a). We then add s
        to it to form the current max score up till a. Then we do bit.update(a).

        We record all the max score along the way.

        O(NlogN), 248 ms, faster than 93.95%
        """
        min_age, max_age = min(ages), max(ages)
        bit = BIT(max_age - min_age + 1)
        res = 0
        for s, a in sorted((s, a) for a, s in zip(ages, scores)):
            cur_max = bit.query(a - min_age) + s
            bit.update(a - min_age, cur_max)
            res = max(res, cur_max)
        return res


sol = Solution5()
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
