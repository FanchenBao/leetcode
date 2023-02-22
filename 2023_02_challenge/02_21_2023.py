# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution1:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """LeetCode 540

        O(N), 178 ms, faster than 69.41%
        """
        res = 0
        for n in nums:
            res ^= n
        return res


class Solution2:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """Use indices to do binary search. For each index, we examine whether
        the number of elements to the left is even or odd. From that we can
        determine on which side the target resides.

        Didn't think about it. Had to read my previous solution to get the idea.

        O(logN), 175 ms, faster than 78.27% 
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] == nums[mid - 1]:
                if mid % 2 == 0:
                    hi = mid - 2
                else:
                    lo = mid + 1
            else:
                if mid % 2 == 0:
                    lo = mid
                else:
                    hi = mid - 1
        return nums[lo]


sol = Solution2()
tests = [
    ([1,1,2,3,3,4,4,8,8], 2),
    ([3,3,7,7,10,11,11], 10),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.singleNonDuplicate(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
