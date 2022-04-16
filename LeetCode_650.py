# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minSteps(self, n: int) -> int:
        """This is not working. Too complicated and takes too long.
        """
        if n == 1:
            return 0
        dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]
        for k in range(1, n + 1):
            dp[k][k] = [1, set([k])]
        for i in range(2, n + 1):
            for j in range(1, i // 2 + 1):
                temp = [math.inf, set()]
                for p in range(j, i // 2 + 1):
                    q = i - p
                    step_p = dp[p][j]
                    if not step_p:
                        break
                    # print(j, p, q, step_p)
                    min_steps_q = math.inf
                    end_copy = set()
                    for c in step_p[1]:
                        step_q = dp[q][c]
                        if step_q:
                            if step_q[0] < min_steps_q:
                                min_steps_q, end_copy = step_q
                            elif step_q[0] == min_steps_q:
                                end_copy.add(step_q[1])
                    if dp[q][p] and 1 + dp[q][p][0] < min_steps_q:
                        min_steps_q, end_copy = 1 + dp[q][p][0], dp[q][p][1]
                    ms = min_steps_q + step_p[0]
                    if ms < temp[0]:
                        temp = [ms, end_copy]
                    elif ms == temp[0]:
                        temp[1] = temp[1].union(temp[1])
                if temp[0] < math.inf:
                    dp[i][j] = temp
        # for row in dp:
        #     print(row)
        return dp[n][1][0]


sol = Solution()
tests = [
    (3, 3),
    (1, 0),
    (4, 4),
    (2, 2),
    (8, 6),
    (16, 8),
    (32, 10),
    (5, 5),
    (256, 16),
    (1000, 21),
]

for i, (n, ans) in enumerate(tests):
    res = sol.minSteps(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
