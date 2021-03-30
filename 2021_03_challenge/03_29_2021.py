# from pudb import set_trace; set_trace()
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        """LeetCode 971

        I don't know what happened, but my initial thinking process was
        extremely convoluted. After clearing my mind, I was able to reconsider
        the essense of the recursive relation. There are two keys. First, the
        index on voyage only increases. This is because all values are unique,
        so there is no need to backtrack. Second, any empty node shall be
        considered a match, because empty nodes do not contribute to the match-
        ing of voyage. With these two keys, the recursion is easier to implement.
        We check the node's value with the current value specified by the index
        in voyage. If they are not the same, we return False. If they are the
        same, we proceed by traversing on the left. If left traverse fails, we
        have a second chance of swapping and then traversing the left again. If
        the second left traverse also fails, we return False. Any time a left
        traverse succeeds, we proceed to traverse the right branch.

        O(N), 36 ms, 61% ranking.
        """
        self.idx = 0
        res = []

        def traverse(node: TreeNode) -> bool:
            if not node:
                return True
            if node.val != voyage[self.idx]:
                return False
            self.idx += 1
            if traverse(node.left):
                return traverse(node.right)
            res.append(node.val)
            if traverse(node.right):  # swapping
                return traverse(node.left)
            return False

        return res if traverse(root) else [-1]

        

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
