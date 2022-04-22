# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution1:
    def findClosestNumber(self, nums: List[int]) -> int:
        """189 ms
        """
        dis, res = math.inf, -math.inf
        for n in nums:
            absn = abs(n)
            if absn < dis:
                dis, res = absn, n
            elif absn == dis and n > res:
                res = n
        return res


class Solution2:
    def findClosestNumber(self, nums: List[int]) -> int:
        """
        155 ms, 80.98%
        """
        nums.sort()
        nums.append(math.inf)
        i = bisect_right(nums, 0)
        if nums[i] <= abs(-nums[i - 1]):
            return nums[i]
        if nums[i] > abs(-nums[i - 1]):
            return nums[i - 1]


# sol = Solution()
# tests = [
#     ([4,2,1,3], [[1,2],[2,3],[3,4]]),
#     ([1,3,6,10,15], [[1,3]]),
#     ([3,8,-10,23,19,-4,-14,27], [[-14,-10],[19,23],[23,27]]),
# ]

# for i, (arr, ans) in enumerate(tests):
#     res = sol.minimumAbsDifference(arr)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
