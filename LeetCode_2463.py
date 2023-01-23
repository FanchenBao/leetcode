# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        """Failed. I checked the solution from lee215

        https://leetcode.com/problems/minimum-total-distance-traveled/discuss/2783305/Python-DP-Solution

        The idea is to see this problem as a Knapsack. Each factory is a
        knapsack because it has a capacity. The question can be converted to
        finding the optimal way to fill all the factories with the given robots.
        The target optimization is the abs distance between each robot and its
        factory, but the general idea is the same: for each robot, we either
        let it be fixed by the current factory, or we skip to the next factory.

        The sort is important, because we can guarantee that when a robot skipps
        to the next factory, the next factory is always new (i.e. with no prior
        robots being fixed there)

        dfs(i, j, k) is the min total distance to fix robot[i:] with
        factory[j] having already fixed k robots

        Option 1: robot[i] skips factory[j], thus the total distance is
        dfs(i, j + 1, 0). Note that the new factory has not fixed any robot at
        the moment.

        Option 2: robot[i] is fixed at factory[j], thus the total distance is
        dfs(i + 1, j, k + 1) + abs(robot[i] - factory[j][0])

        We pick the smaller of the two.

        Edge cases: if i == len(robot), we have fit all robots to factory. Shall
        return 0.

        If j == len(factory), we have not fit all robots but have used up all
        factories. Shall turn math.inf

        If k > factory[j][1], we have used up all capacity of a factory. Shall return
        math.inf

        IMPORTANT: the condition for k < factory[j][1] shall be checked before
        calling dfs(i + 1, j, k + 1), because if we don't check it, it will be
        very complicated to check for the edge case. In the edge case when we
        check for i, we must also check for k. If i reaches the end, k is
        good, we are good. But if i reaches the end, k is not good, then we are
        bad. Plus when we check k, we need j. So we have to check for j as well.
        Yet, if we check for j, we need to make sure we also check for i,
        because it is allowed for both i and j to reach the end, but not just
        one of them. As you can see, there is a circular dependency to check
        for i, j, and k. It is doable, but very convoluted. The better solution
        is to check k in the body of the function and let the edge cases deal
        with only i and j.

        O(MNK), 3015 ms, faster than 50.56%
        """
        robot.sort()
        factory.sort()

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int, k: int) -> int:
            if i == len(robot):
                return 0
            if j == len(factory):
                return math.inf
            op1 = dfs(i, j + 1, 0)  # skip j
            if k < factory[j][1]:  # have more capacity
                op2 = dfs(i + 1, j, k + 1) + abs(robot[i] - factory[j][0])  # use j
            else:
                op2 = math.inf
            return min(op1, op2)

        return dfs(0, 0, 0)
        


sol = Solution()
tests = [
    ([0,4,6], [[2,2],[6,2]], 4),
    ([1,-1], [[-2,1],[2,1]], 2),
    ([79215383,708490359,-779179404,713376652,-368850098,573013032,195489859,121470584,916616893,327266713,950673412,410723622,538863648,170740409,753199490], [[-284344805,4],[349360740,6],[-360820857,2],[-493544411,13],[-28182860,4],[-117519725,13],[-294274103,9]], 5121930465),
    ([79,70,-79,72,-38,57,19,12,93,33,92,40,53,17,73], [[-24,4],[34,6],[-36,2],[-41,13],[-28,4],[-11,13],[-29,9]], 623),
    ([-9, -7, -6, 3, -20], [[1, 2], [-15, 1], [-17, 5]], 28),
]

for i, (robot, factory, ans) in enumerate(tests):
    res = sol.minimumTotalDistance(robot, factory)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
