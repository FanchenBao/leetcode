# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        """LeetCode 665

        I was a bit paranoid at the beginning, thinking that this could be one
        of those tough medium ones. Fortunately, it was not. We check for the
        index where nums drop down. We only allow one such drop, thus if more
        than one drop is detected, we immediately return False. One a drop is
        identified, either the drop idx can be removed or the index right
        before drop can be removed. Check both situations, and we have it.

        O(N), 284 ms, faster than 45.59% 
        """
        if len(nums) <= 2:  # edge cases
            return True
        idx = -1
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if idx >= 0:  # two drops, impossible
                    return False
                idx = i
        if idx == len(nums) - 1 or idx == 1:
            return True
        return nums[idx - 1] <= nums[idx + 1] or nums[idx - 2] <= nums[idx]


sol = Solution()
tests = [
    ([4,2,3], True),
    ([4,2,1], False),
    ([1], True),
    ([1, 2, 3], True),
    ([1,1,1,1,1], True),
    ([1,1,1,2,1,1,1], True),
    ([1,1,1,2,2,1,1,1], False),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.checkPossibility(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
