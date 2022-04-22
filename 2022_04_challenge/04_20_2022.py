# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = [root]
        while self.stack and self.stack[-1].left:
            self.stack.append(self.stack[-1].left)

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.stack.append(node.right)
            while self.stack and self.stack[-1].left:
                self.stack.append(self.stack[-1].left)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    


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
