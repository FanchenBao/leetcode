# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def countQuadruplets(self, nums: List[int]) -> int:
        """TLE, because num_smaller and num_larger takes too long to build.
        """
        N = len(nums)
        # num_smaller[i][j] is the number of vals smaller than nums[i] to the
        # left of nums[j]
        num_smaller = [[0] * N for _ in range(N)]
        # num_larger[i][j] is the number of vals bigger than nums[i] to the
        # right of nums[j]
        num_larger = [[0] * N for _ in range(N)]
        for i in range(N):
            pre = 0
            for j in range(i + 1):
                num_smaller[i][j] = pre + int(nums[j] < nums[i])
                pre = num_smaller[i][j]
        for i in range(N - 1, -1, -1):
            pre = 0
            for j in range(N - 1, i - 1, -1):
                num_larger[i][j] = pre + int(nums[j] > nums[i])
                pre = num_larger[i][j]
        # find j, k of the triplet i, j, k, l, such that nums[j] > nums[k]

        # for j in range(1, N - 2):
        #     for k in range(j + 1, N - 1):
        #         if nums[j] > nums[k]:
        #             print(nums[j], nums[k], num_smaller[k], num_larger[j])
        return sum(num_smaller[k][j] * num_larger[j][k] for j in range(1, N - 2) for k in range(j + 1, N - 1) if nums[j] > nums[k])


class Solution2:
    def countQuadruplets(self, nums: List[int]) -> int:
        """Use a 2D array to handle num_smaller matrix. The observation is that
        if I am handling value 3. I check the idx of value 2. If value 2 is to
        my right, that means we don't have to do anything about value 3. The
        num_smaller of value 3 is the same as num_smaller of value 2.

        If value 2 is to my left, then I only need to fill the values from 2 to
        3, by adding 1 to the last num_smaller of value 2.

        num_larger can be handled in the same way. Thus, we can complete
        num_smaller and num_larger in O(N^2) time with some saveings and
        O(N^2) space.

        Once the prefix sum matrices for values smaller and values bigger are
        created, we pick any pair of nums[j] and nums[k] where j < k and 
        nums[j] > nums[k]. Then we just need to find the number of values to
        the left of nums[j] that is smaller than nums[k] (all of these values
        can serve as nums[i]) and the number of values to the right of nums[k]
        that is larger than nums[j] (all of these values can serve as nums[l]).

        The product of these two values are the total number of quadruplets
        that can be formed with the current pair of nums[j] and nums[k].

        O(N^2), 6504 ms, faster than 21.21%
        """
        N = len(nums)
        num_idx_map = {n: i for i, n in enumerate(nums)}
        # num_smaller[i][j] is the number of vals smaller than nums[i] to the
        # left of nums[j]
        num_smaller = {num_idx_map[1]: [0] * N}
        for n in range(2, N + 1):
            i, j = num_idx_map[n], num_idx_map[n - 1]
            if j > i:
                num_smaller[i] = num_smaller[j]
            else:
                num_smaller[i] = num_smaller[j][:]
                pre = num_smaller[j][j]
                for k in range(j, i + 1):
                    num_smaller[i][k] = pre + int(nums[k] < nums[i])
                    pre = num_smaller[i][k]
        # num_larger[i][j] is the number of vals bigger than nums[i] to the
        # right of nums[j]
        num_larger = {num_idx_map[n]: [0] * N}
        for n in range(N - 1, 0, -1):
            i, j = num_idx_map[n], num_idx_map[n + 1]
            if j < i:
                num_larger[i] = num_larger[j]
            else:
                num_larger[i] = num_larger[j][:]
                pre = num_larger[j][j]
                for k in range(j, i - 1, -1):
                    num_larger[i][k] = pre + int(nums[k] > nums[i])
                    pre = num_larger[i][k]
        return sum(num_smaller[k][j] * num_larger[j][k] for j in range(1, N - 2) for k in range(j + 1, N - 1) if nums[j] > nums[k])


class Solution3:
    def countQuadruplets(self, nums: List[int]) -> int:
        """Solution from: https://leetcode.com/problems/count-increasing-quadruplets/discuss/3111697/C%2B%2BorJavaorPython3-Cleanest-DP-with-Clarification-O(n2)

        This is just too rich, too good.

        Let dp[j] be the number of valid triplets i, j, k, such that i < j < k
        and nums[i] < nums[k] < nums[j], given an l > j.

        Thus, as we iterate j from 0 to l - 1, each time nums[j] < nums[l], we
        can add dp[j] to the answer.

        Also, we keep track of the number of vals smaller than nums[l] along the
        way. We use pre_small to keep track of this number.
        Thus, if nums[j] > nums[l], then the number of valid triplets centering
        in nums[j] increase by pre_small because we can include nums[l] into the
        triplet. This is to prepare the DP triplet count for the next round of
        l.

        O(N^2), 3045 ms, faster than 68.70%
        """
        N = len(nums)
        dp = [0] * N
        res = 0
        for l in range(N):
            pre_small = 0
            for j in range(l):
                if nums[j] < nums[l]:
                    res += dp[j]
                    pre_small += 1
                else:
                    dp[j] += pre_small
        return res


sol = Solution2()
tests = [
    ([1,3,2,4,5], 2),
    ([1,2,3,4], 0),
    ([1,3,5,2,4], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.countQuadruplets(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
