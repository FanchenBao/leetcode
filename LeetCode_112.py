# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """DFS, O(N), 57 ms, 18% ranking.
        """

        def dfs(node: Optional[TreeNode], pathsum: int) -> bool:
            pathsum += node.val
            if not node.left and not node.right and pathsum == targetSum:
                return True
            return (node.left and dfs(node.left, pathsum)) or (node.right and dfs(node.right, pathsum))

        return dfs(root, 0) if root else False
        


class Solution2:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """BFS. O(N), 35 ms, 94% ranking.
        """
        if not root:
            return False
        queue = [(root, 0)]
        while queue:
            temp = []
            for node, pathsum in queue:
                pathsum += node.val
                if not node.left and not node.right and pathsum == targetSum:
                    return True
                if node.left:
                    temp.append((node.left, pathsum))
                if node.right:
                    temp.append((node.right, pathsum))
            queue = temp
        return False


class Solution3:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """Better DFS
        
        Ref: https://leetcode.com/problems/path-sum/discuss/36367/3-lines-of-c%2B%2B-solution
        """
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
