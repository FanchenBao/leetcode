# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        """Get all paths. As we gather a path, we keep track of the number of
        odd repeats in the path. For a path to have at least one permutation as
        palindrome, the requirement is that the number of odd repeats cannot
        exceed 1. When we hit the leaf, we compare whether the number of odd
        repeats is smaller or equal to one. If it is, the path qualifies,
        otherwise not. We use a simple array to keep count of the number of
        repeats of each value in the path.

        O(N), 420 ms, 58% ranking.
        """
        self.res = 0
        self.num_odd = 0
        count = [0] * 10

        def dfs(node: TreeNode):
            if not node:
                return
            count[node.val] += 1
            self.num_odd += 1 if count[node.val] % 2 else -1
            dfs(node.left)
            dfs(node.right)
            if not node.left and not node.right:  # leaf
                self.res += 1 if self.num_odd <= 1 else 0
            count[node.val] -= 1  # backtrack
            self.num_odd += 1 if count[node.val] % 2 else -1

        dfs(root)
        return self.res


class Solution2:
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        """Use bit magic according to the official solution.

        The bit magic has two aspects. First is to keep track of the current
        parity of each digit, i.e. record whether a digit has even or odd
        number of occurrence. This is done through path ^ (1 << node.val).
        1 << node.val put 1 in the position of node.val; XOR with path will
        keep the even number of occurrences as 0 and odd 1.

        The second trick is to check there is at most one ONE in the path. This
        can be done via path & (path - 1). If path has only one 1, the
        operation results in 0, otherwise non-zero.

        O(N), 328 ms, 96% ranking.
        """
        self.res = 0

        def dfs(node: TreeNode, path: int):
            if not node:
                return
            new_path = path ^ (1 << node.val)
            if not node.left and not node.right:  # leaf
                self.res += 1 if new_path & (new_path - 1) == 0 else 0
            else:
                dfs(node.left, new_path)
                dfs(node.right, new_path)

        dfs(root, 0)
        return self.res

# sol = Solution3()
# tests = [
#     # ([1, 2, 3, 1], 3, 0, True),
#     # ([1, 0, 1, 1], 1, 2, True),
#     ([1, 5, 9, 1, 5, 9], 2, 3, False),
#     # ([1, 4, 9, 1, 4, 9], 1, 3, True),
#     # ([-1, -1], 1, -1, False),
#     # ([1, 3, 6, 2], 1, 2, True),
# ]

# for i, (nums, k, t, ans) in enumerate(tests):
#     res = sol.containsNearbyAlmostDuplicate(nums, k, t)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
