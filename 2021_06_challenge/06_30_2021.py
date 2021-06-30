# from pudb import set_trace; set_trace()
from typing import List, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """LeetCode 236

        Very naive solution. Two rounds of dfs to find all the ancestors of
        p and q, and save them in two lists. Then compare the two lists and
        return the last ancestor before the two lists diverge.

        O(N), 88 ms, 22% ranking.
        """
        anc_p = []
        anc_q = []

        def dfs(node: TreeNode, target: TreeNode, anc: List[TreeNode]) -> bool:
            if not node:
                return False
            if node == target:
                anc.append(node)
                return True
            if dfs(node.left, target, anc) or dfs(node.right, target, anc):
                anc.append(node)
                return True
            return False

        dfs(root, p, anc_p)
        dfs(root, q, anc_q)
        while anc_p and anc_q and anc_p[-1] == anc_q[-1]:
            ca = anc_q.pop()
            anc_p.pop()
        return ca


class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """This is the recursion solution. The idea is for a given node, if p
        and q can be found in its children, then the node is an ancestor. The
        challenge is to know whether this is the lowest ancestor. We can resolve
        this by having the dfs function to return the lowest ancestor. This
        means if a node is an ancestor, and dfs of both its branches do not
        return any ancestor, then the current node must be the lowest ancestor.
        It then returns itself to its parent, who upon seeing that the lowest
        ancestor has been found, will return the lowest ancestor instead of
        itself.

        O(N), 72 ms, 68% ranking.
        """

        def dfs(node: TreeNode) -> Tuple[bool, bool, TreeNode]:
            if not node:
                return False, False, None
            if node == p:
                _, lq, _ = dfs(node.left)
                _, rq, _ = dfs(node.right)
                if lq or rq:  # if q can be found, the current node must be LCA
                    return True, True, node
                else:
                    return True, False, None
            if node == q:  # if p can be found, the current node must be LCA
                lp, _, _ = dfs(node.left)
                rp, _, _ = dfs(node.right)
                if lp or rp:
                    return True, True, node
                else:
                    return False, True, None
            lp, lq, l_anc = dfs(node.left)
            rp, rq, r_anc = dfs(node.right)
            has_p = lp or rp
            has_q = lq or rq
            if has_p and has_q and l_anc is None and r_anc is None:
                return True, True, node
            else:
                return has_p, has_q, l_anc if l_anc is not None else r_anc

        _, _, res = dfs(root)
        return res


class Solution3:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """Better recursion solution. Ref:
        https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/

        The trick is to realize that only the LCA satisfies the following condition:

        1. LCA == p, and q is in LCA's left or right branch.
        2. LCA == q, and p is in LCA's left or right branch.
        3. p in LCA's left, q in LCA's right; or the other way around.
        """
        self.res = None

        def dfs(node: TreeNode) -> bool:
            if not node:
                return False
            found_left = dfs(node.left)
            found_right = dfs(node.right)
            found_self = node == p or node == q
            if found_left + found_right + found_self >= 2:
                self.res = node
            return found_left or found_right or found_self

        dfs(root)
        return self.res


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
