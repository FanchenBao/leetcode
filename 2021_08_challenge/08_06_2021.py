# from pudb import set_trace; set_trace()
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        """LeetCode 429

        Nothing too fancy. Basic BFS suffices.

        O(N), 56 ms, 38% ranking.
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            res.append([])
            for node in queue:
                res[-1].append(node.val)
                for child in node.children:
                    temp.append(child)
            queue = temp   
        return res
        

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
