# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        """Wow, we solved it!!!

        I did take a look at related topics, and saw that my trajectory was
        correct. It is DP + prefix sum.

        The idea is we keep a dp list where dp[i] is the max money we can get
        by taking i number of coins from the first pile to the pile right
        before the current pile. Then we produce a prefix sum on the current
        pile (ps). After that, we want to update dp. Thus, we let i go from 1
        to k. However, there is a trick here. In order to avoid using an
        update dp value (the dp value used must be from the previous round,
        i.e. not updated, otherwise we are double counting the current pile),
        we need i to go from k to 1.

        For each i, we can compose this i by taking j number of coins from the
        current pile, and i - j number of coins from all the previous piles.
        The max money we can earn by taking i number of coins is to compute the
        max value of ps[j - 1] + dp[i - j] where j goes from 1 to
        min(i, len(ps)).

        We keep updating the dp array with each new pile. Once all piles are
        considered, the answer is the max value in dp.

        O(NKM), where N = len(piles), K = k, M is the average lenght of one
        pile. 5848 ms, 73% ranking.
        """
        dp = [0] * (k + 1)
        for p in piles:
            ps = list(accumulate(p))
            for i in range(k, 0, -1):  # right to left to avoid a temp array
                for j in range(1, min(i + 1, len(ps) + 1)):
                    dp[i] = max(dp[i], ps[j - 1] + dp[i - j])
        return max(dp)


sol = Solution()
tests = [
    ([[1,100,3],[7,8,9]], 2, 101),
    ([[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7, 706),
    ([[37,88],[51,64,65,20,95,30,26],[9,62,20],[44]], 9, 494),
]

for i, (piles, k, ans) in enumerate(tests):
    res = sol.maxValueOfCoins(piles, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
