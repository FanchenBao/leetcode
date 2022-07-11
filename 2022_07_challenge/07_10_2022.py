# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """LeetCode 746

        Top down O(N), 77 ms, faster than 69.60%
        """
        N = len(cost)

        @lru_cache(maxsize=None)
        def helper(idx: int) -> int:
            if idx <= 1:
                return cost[idx]
            return min(helper(idx - 1), helper(idx - 2)) + (cost[idx] if idx < N else 0)

        return helper(N)


class Solution2:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """bottom up

        O(N), 74 ms, faster than 73.75%
        """
        cost.append(0)
        N = len(cost)
        if N <= 2:
            return min(cost)
        pp, p = cost[0], cost[1]
        for i in range(2, N):
            pp, p = p, min(p, pp) + cost[i]
        return p



sol = Solution()
tests = [
    ([4,2,1,3], [[1,2],[2,3],[3,4]]),
    ([1,3,6,10,15], [[1,3]]),
    ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
]

for i, (arr, ans) in enumerate(tests):
    res = sol.minimumAbsDifference(arr)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
