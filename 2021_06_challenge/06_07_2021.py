# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """LeetCode 746

        Very basic DP. At each step, we compute the min overall cost of
        taking the current step. There are two ways to take the current step.
        One way is to take the step immediately before, and the other is to
        take the step two steps back. To compute the min cost of the current
        step, we take the min cost of taking the two possible previous steps.
        By doing this, we can create a DP table that lists the min cost of
        taking all steps. The answer is the min of the last two steps.

        Of course, we can simplify the space complexity by using only pre, cur
        to point to the min cost of the step right before and the step two steps
        before.

        O(N), 60 ms, 47% ranking.
        """
        pre, cur = 0, cost[0]
        for c in cost[1:]:
            cur, pre = c + min(cur, pre), cur
        return min(cur, pre)


sol = Solution()
tests = [
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
]

for i, (cost, ans) in enumerate(tests):
    res = sol.minCostClimbingStairs(cost)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
