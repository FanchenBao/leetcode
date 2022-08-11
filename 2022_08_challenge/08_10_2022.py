# from pudb import set_trace; set_trace()
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """LeetCode 108

        O(N), 137 ms, faster than 38.74%
        """
        def helper(lo: int, hi: int) -> TreeNode:
            if lo == hi:
                return TreeNode(val=nums[lo])
            if lo + 1 == hi:
                return TreeNode(val=nums[hi], left=TreeNode(val=nums[lo]))
            mid = (lo + hi) // 2
            return TreeNode(val=nums[mid], left=helper(lo, mid - 1), right=helper(mid + 1, hi))

        return helper(0, len(nums) - 1)
        

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
