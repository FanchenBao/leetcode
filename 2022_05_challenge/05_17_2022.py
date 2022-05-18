# from pudb import set_trace; set_trace()
from typing import List



class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """LeetCode 1379

        Just traverse it, however you want.

        O(N), 625 ms, faster than 90.04%
        """
        
        def dfs(on: Optional[TreeNode], cn: Optional[TreeNode]) -> Optional[TreeNode]:
            if on:
                if on == target:
                    return cn
                res_left = dfs(on.left, cn.left)
                if res_left:
                    return res_left
                return dfs(on.right, cn.right)
            return None

        return dfs(original, cloned)



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
