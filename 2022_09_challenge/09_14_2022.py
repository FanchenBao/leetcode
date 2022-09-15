# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution1:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """LeetCode 1457

        We had a little bit hiccup when identifying what is a path. A path in
        binary tree has to end in a leaf. Therefore, we must identify a leaf
        in order to process the path. An improvement that we found was that we
        can use Counter directly to record the frequency of values instead of
        an actual path.

        O(N), 1081 ms, faster than 80.37%
        """
        self.res = 0

        def dfs(node: Optional[TreeNode], counter: Counter) -> None:
            counter[node.val] += 1
            if not node.left and not node.right and sum(val % 2 for val in counter.values()) <= 1:
                self.res += 1
            if node.left:
                dfs(node.left, counter)
            if node.right:
                dfs(node.right, counter)
            counter[node.val] -= 1

        dfs(root, Counter())
        return self.res


class Solution2:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        """Bit magic, from my previous solution.

        Use an integer to represent path. Each time a value is encountered, we
        do path ^ (1 << node.val). Since even frequency of a val results in bit
        0 in the path, we just need to verify at the end that path contains
        only one 1 bit.
        """
        self.res = 0

        def dfs(node: Optional[TreeNode], path: int) -> None:
            path ^= (1 << node.val)
            if not node.left and not node.right:
                self.res += path & (path - 1) == 0
            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

        dfs(root, 0)
        return self.res


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
