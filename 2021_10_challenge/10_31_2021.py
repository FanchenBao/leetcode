# from pudb import set_trace; set_trace()
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: Node) -> Node:
        """LeetCode 430

        We traverse the linked list until we encounter a node that has a
        child. We flatten the linked list rooted at the child, and return its
        tail. Then we insert the flattened child linked list, and continue.

        One tricky part is that a child linked list could have its tail being
        its own child linked list. Thus, we need to reassign tail each time we
        process a child linked list.

        O(N), 36 ms, 76% ranking.
        """

        def helper(head: Node) -> Node:
            node, tail = head, head
            while node:
                tail = node
                if node.child:
                    tail = helper(node.child)  # reassign tail in case child linked list has the real tail
                    temp = node.next
                    node.next = node.child
                    node.child.prev = node
                    node.child = None
                    tail.next = temp
                    if temp:
                        temp.prev = tail
                    node = temp
                else:
                    node = node.next
            return tail

        helper(head)
        return head


        


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
