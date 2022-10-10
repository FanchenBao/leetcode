# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """LeetCode 653

        This is a cop-out solution using a set instead of binary search

        O(N), 193 ms, faster than 26.93%, but also O(N) additional space
        """
        nums = set()

        def dfs(node) -> None:
            if node:
                nums.add(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        for n in nums:
            if k - n in nums and k - n != n:
                return True
        return False


class Solution2:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """Using binary search naively

        O(NlogN) 242 ms, faster than 11.19%
        """
        def binary_search(node: Optional[TreeNode], cur_tar: int) -> Optional[TreeNode]:
            if not node:
                return None
            if node.val == cur_tar:
                return node
            if cur_tar < node.val:
                return binary_search(node.left, cur_tar)
            return binary_search(node.right, cur_tar)

        queue = [root]
        while queue:
            tmp = []
            for node in queue:
                pot_node = binary_search(root, k - node.val)
                if pot_node and pot_node is not node:
                    return True
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
        return False


class Solution3:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """Binary search as well and O(1) space

        O(NlogN), 247 ms, faster than 10.33%
        """
        def binary_search(node: Optional[TreeNode], cur_tar: int) -> Optional[TreeNode]:
            if not node:
                return None
            if node.val == cur_tar:
                return node
            if cur_tar < node.val:
                return binary_search(node.left, cur_tar)
            return binary_search(node.right, cur_tar)


        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return False
            if k - node.val < node.val:
                return False
            if dfs(node.left):
                return True
            pot_node = binary_search(root, k - node.val)
            if pot_node and pot_node is not node:
                return True
            return dfs(node.right)

        return dfs(root)


class Solution4:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """BST iterator. Treat the BST as a sorted array, and we go from both
        ends toward the middle. Then it is a standard two sum problem where if
        the sum of the two iterators is larger than k, we move the right left,
        otherwise the left right.

        We need to keep two stacks to manually create BST iterator

        O(N), 84 ms, faster than 93.33%
        """
        lstack, rstack = [], []

        def down_left(node: Optional[TreeNode]) -> Optional[TreeNode]:
            while node.left:
                lstack.append(node)
                node = node.left
            return node

        def down_right(node: Optional[TreeNode]) -> Optional[TreeNode]:
            while node.right:
                rstack.append(node)
                node = node.right
            return node

        def next_left(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node.right:
                return down_left(node.right)
            return lstack.pop()
        
        def next_right(node: Optional[TreeNode]) -> Optional[TreeNode]:
            if node.left:
                return down_left(node.left)
            return rstack.pop()

        lo, hi = down_left(root), down_right(root)
        while lo is not hi:
            if lo.val + hi.val < k:
                next_left(lo)
            elif lo.val + hi.val > k:
                next_right(hi)
            else:
                return True
        return False
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
