# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0] * N
        dp[-1] = questions[-1][0]
        for i in range(N - 2, -1, -1):
            dp[i] = max(
                questions[i][0] + (dp[i + questions[i][1] + 1] if i + questions[i][1] + 1 < N else 0),
                dp[i + 1],
            )
        return max(dp)


sol = Solution()
tests = [
    ([[3,2],[4,3],[4,4],[2,5]], 5),
    ([[1,1],[2,2],[3,3],[4,4],[5,5]], 7),
    ([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]], 157),
]

for i, (questions, ans) in enumerate(tests):
    res = sol.mostPoints(questions)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
