# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """LeetCode 474

        I know that this is a knapsack problem, but I don't remember how
        knapsack is solved. I should, but I just couldn't remember the algorithms
        that I have seen before. Anyway, even after I have read through the
        solutions, I still struggle tremendously putting together this solution.

        The intuition is to tabulate all possible combinations of m and n, and
        find the maximum number of strings that can fit into each combination of
        m and n from the first to the ith string. Then for any ith string tring
        to fit into p zeros and q ones, we choose the max between these two:

        1. Do not add the ith string. Then dp[i][p][q] = dp[i - 1][p][q]
        2. We add the ith string. Then dp[i][p][q] = dp[i - 1][p - zeros][q - ones] + 1
        This is to find the best situation to fit the current string.

        The catch for me is that when a string does not fit into p and q,
        we should do dp[i][p][q] = dp[i - 1][p][q], which essentially says we
        cannot include the current string.

        O(KMN), where K is the length of the input strs. 5108 ms, 21% ranking.
        """
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len(strs) + 1)]
        for i, s in enumerate(strs, start=1):
            ones = s.count('1')
            zeros = s.count('0')
            for p in range(m + 1):
                for q in range(n + 1):
                    if p >= zeros and q >= ones:
                        dp[i][p][q] = max(dp[i - 1][p][q], dp[i - 1][p - zeros][q - ones] + 1)
                    else:
                        dp[i][p][q] = dp[i - 1][p][q]
        return dp[len(strs)][m][n]


sol = Solution()
tests = [
    (['10', '0001', '111001', '1', '0'], 5, 3, 4),
    (['10', '0', '1'], 1, 1, 2),
    (['111', '1000', '1000', '1000'], 9, 3, 3),
    (['1100', '0111111', '00111', '100', '0'], 7, 6, 4),
]

for i, (strs, m, n, ans) in enumerate(tests):
    res = sol.findMaxForm(strs, m, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
