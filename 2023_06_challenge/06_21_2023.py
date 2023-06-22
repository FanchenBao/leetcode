# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate


class Solution1:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        """LeetCode 2448

        This is probably the smoothest hard problem I have ever done. Did not
        see the solution initially, but as I was going through the DP process,
        I realize that we can easily find the cost of moving the array towards
        any given value in O(1), IF we have the original nums sorted. And then
        it is just the proof that the optimal value we move to must be one of
        nums. Let's do this proof one more time.

        Suppose we can find a value P not in nums that yields the min cost. And
        also suppose that nums have been sorted. Then, we have the total of cost
        on the left side of P and the total of cost on the right side of P.

        Suppose the cost on the left side of P is bigger than the cost on the
        right, then as we move P towards the left, the reduction in cost on the
        left is bigger than the increase in cost on the right, until we land on
        one of the number in nums. Hence, we can achieve an even smaller cost
        when the value to end up on is one of the number in nums.

        Now that we have that cleared up, we just need to write out the formula
        to compute the total cost of moving numbers in nums to any value. It
        turns out this can be facilitated drastically by using two prefix sums,
        one is cost itself (after sorted with nums), and the other is the
        product of each number of its value.

        O(NlogN), 462 ms, faster than 77.94% 
        """
        sorted_nc = sorted(zip(nums, cost))
        presum_cost = list(accumulate((c for _, c in sorted_nc), initial=0))
        presum_nc = list(accumulate((n * c for n, c in sorted_nc), initial=0))
        res = math.inf
        for k, (n, _) in enumerate(sorted_nc):
            cur_cost = presum_cost[k] * n - presum_nc[k] + presum_nc[-1] - presum_nc[k + 1] - (presum_cost[-1] - presum_cost[k + 1]) * n
            res = min(res, cur_cost)
        return res


class Solution2:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        """Convex optimization! From the official solution.

        Linear combination of convex functions is convex. The function of each
        number is f(x) = |nums[i] - x|, which is convex. Thus, the total cost
        function F(x) must also be convex. It does not matter what it actually
        is.

        Convex function must have an optimal point. And the function must be
        decreasing to the left of the optimal point and increasing to the right
        of the optimal point. Thus, we can use binary search to find the optimal
        point, using the check for increasing or decreasing to determine whether
        the current point is on the left or right side.

        Brilliant!

        O(NlogK), 916 ms, faster than 41.18%
        """
        lo, hi = min(nums), max(nums) + 1

        def F(x: int) -> int:
            return sum(abs(n - x) * c for n, c in zip(nums, cost))

        while lo < hi:
            mid = (lo + hi) // 2
            fmid, fmid_p1 = F(mid), F(mid + 1)
            if fmid < fmid_p1:
                hi = mid
                res = fmid
            else:
                lo = mid + 1
                res = fmid_p1
        return res

sol = Solution2()
tests = [
    ([1,3,5,2], [2,3,1,14], 8),
    ([2,2,2,2,2], [4,2,8,1,3], 0),
]

for i, (nums, cost, ans) in enumerate(tests):
    res = sol.minCost(nums, cost)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
