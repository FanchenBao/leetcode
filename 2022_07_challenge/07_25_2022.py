# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right, bisect_left


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """LeetCode 35

        Two binary search.

        O(logN), 105 ms, faster than 73.41% 
        """
        if not nums:
            return [-1, -1]
        il = bisect_left(nums, target)
        if il == len(nums) or nums[il] != target:
            return [-1, -1]
        return [il, bisect_right(nums, target) - 1]


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
