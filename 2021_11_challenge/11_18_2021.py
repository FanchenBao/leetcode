# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """LeetCode 448

        Swapping. O(N), 416 ms, 26% ranking.
        """
        i = 0
        while i < len(nums):
            while nums[i] and nums[i] != i + 1:
                pos = nums[i] - 1
                if nums[i] == nums[pos]:
                    nums[i] = 0
                else:
                    nums[i], nums[pos] = nums[pos], nums[i]
            i += 1
        return [i + 1 for i, n in enumerate(nums) if n == 0]


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """Better while loop condition. No need to set a sentinel.

        From: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/discuss/1583736/C%2B%2BPython-All-6-Solutions-w-Explanations-or-Binary-Search%2B-Hashset-%2B-2x-O(1)-Space-Approach
        """
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        return [i + 1 for i, n in enumerate(nums) if n != i + 1]
        


sol = Solution2()
tests = [
    ([4,3,2,7,8,2,3,1], [5, 6]),
    ([1, 1], [2]),
    ([1], []),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findDisappearedNumbers(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
