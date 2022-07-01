# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate


class Solution1:
    def minMoves2(self, nums: List[int]) -> int:
        """LeetCode 462

        Just try out each number, and compute how many changes are needed. We
        can sort the nums and use prefix sum to simplify the process of finding
        the sum in a range.

        O(NlogN), 133 ms, faster than 29.60%
        """
        nums.sort()
        presum = list(accumulate(nums))
        res = math.inf
        N = len(nums)
        for i, n in enumerate(nums):
            if i and nums[i - 1] == n:
                continue
            chng = i * n - (presum[i - 1] if i else 0) + (presum[-1] - presum[i]) - (N - i - 1) * n
            res = min(chng, res)
        return res


class Solution2:
    def minMoves2(self, nums: List[int]) -> int:
        """Easier solution, which I actually came up with myself last time.

        Read this explanation:
        https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94937/Java(just-like-meeting-point-problem)/173569

        Basically, the idea is that no matter which value we choose to converge
        to, as long as it is located inside the array, the change is the same.
        If we use a value on the edge, it is always worse.
        """
        # use Mr. Pochmann's trick where ~i = (-i) - 1 points to the element
        # at the same position counting from the other side of the array
        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums) // 2))


sol = Solution2()
tests = [
    ([1, 2, 3], 2),
    ([1, 10, 2, 9], 16),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minMoves2(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
