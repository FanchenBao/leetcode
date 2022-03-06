# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        h = {}
        pos_root = set()
        children = set()
        for nv, cv, is_left in descriptions:
            if nv not in h:
                h[nv] = TreeNode(val=nv)
            if cv not in h:
                h[cv] = TreeNode(val=cv)
            if is_left:
                h[nv].left = h[cv]
            else:
                h[nv].right = h[cv]
            children.add(cv)
            if cv in pos_root:
                pos_root.remove(cv)
            if nv not in children:
                pos_root.add(nv)
        return h[list(pos_root)[0]]


        
        
        
# sol = Solution()
# tests = [
#     ([1, 2, 3], 5, 3),
#     ([2], 1, 2),
# ]

# for i, (time, totalTrips, ans) in enumerate(tests):
#     res = sol.minimumTime(time, totalTrips)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
