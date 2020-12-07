# from pudb import set_trace; set_trace()
from typing import List



# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution1:
    def connect(self, root: Node) -> Node:
        """BFS, using a temp node to remember the most recent node that does
        not have its next field set. O(n), 56 ms, 11% ranking

        HOWEVER, this is not O(1) space as I used a queue.
        """
        if root is None:
            return root
        queue = [(root, 0)]
        temp_n, temp_l = Node(), -1
        for node, lvl in queue:
            left, right = node.left, node.right
            if left is not None:
                left.next = right
                queue.append((left, lvl + 1))
            if right is not None:
                queue.append((right, lvl + 1))
            if temp_n.next is None and temp_l == lvl:
                temp_n.next = node
            if node.next is None:
                temp_n, temp_l = node, lvl
        return root


class Solution2:
    def connect(self, root: Node) -> Node:
        """O(1) space solution. O(n), 68 ms, no ranking"""
        pre_row_tail = root
        cur_row_tail = None
        cur_row_head = None
        while pre_row_tail:
            while pre_row_tail:
                left, right = pre_row_tail.left, pre_row_tail.right
                if left:
                    left.next = right
                if cur_row_tail:
                    cur_row_tail.next = left if left else right
                else:  # new row
                    cur_row_head = left if left else right
                    cur_row_tail = cur_row_head
                while cur_row_tail and cur_row_tail.next:  # walk cur_row_tail to end
                    cur_row_tail = cur_row_tail.next
                pre_row_tail = pre_row_tail.next
            pre_row_tail = cur_row_head
            cur_row_tail = None
        return root


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
