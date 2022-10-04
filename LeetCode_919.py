# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import deque


class CBTInserter1:
    """
    Keep two arrays that point to the current level of the tree, and the
    previous level. Use the length of the current level to determine the next
    parent on the previous level. Don't forget to switch levels when the
    current level is filled up.

    123 ms, faster than 57.88% 
    """
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.pre_q = [root]
        while self.pre_q:
            self.cur_q = []
            for node in self.pre_q:
                if node.left:
                    self.cur_q.append(node.left)
                if node.right:
                    self.cur_q.append(node.right)
                else:
                    break
            else:
                self.pre_q = self.cur_q
                continue
            break

    def insert(self, val: int) -> int:
        idx, r = divmod(len(self.cur_q), 2)
        if idx == len(self.pre_q):
            self.pre_q = self.cur_q
            self.cur_q = []
            idx = 0
        node = TreeNode(val=val)
        if r:
            self.pre_q[idx].right = node
        else:
            self.pre_q[idx].left = node
        self.cur_q.append(node)
        return self.pre_q[idx].val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


class CBTInserter2:
    """
    Use deque as in the official solution.

    O(N), but a lot faster, 62 ms, faster than 98.59%
    """
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = deque([root])
        while self.queue:
            node = self.queue[0]
            if node.left:
                self.queue.append(node.left)
            if node.right:
                self.queue.append(node.right)
                self.queue.popleft()
            else:
                break

    def insert(self, val: int) -> int:
        par = self.queue[0]
        self.queue.append(TreeNode(val=val))
        if not par.left:
            par.left = self.queue[-1]
        else:
            par.right = self.queue[-1]
            self.queue.popleft()
        return par.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root

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
