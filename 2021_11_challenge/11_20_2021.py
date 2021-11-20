# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """LeetCode 540

        Binary search, satisfying O(logN) time and O(1) space.
        """
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if nums[mi - 1] == nums[mi]:
                if (hi - mi) % 2:
                    lo = mi + 1
                else:
                    hi = mi - 2
            elif nums[mi] == nums[mi + 1]:
                if mi % 2:
                    hi = mi - 1
                else:
                    lo = mi + 2
            else:
                return nums[mi]
        return nums[lo]


sol = Solution()
tests = [
    ([1,1,2,3,3,4,4,8,8],2),
    ([3,3,7,7,10,11,11],10),
    ([1,1,2,3,3],2),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.singleNonDuplicate(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
